#!/usr/bin/env python3
"""Scopus·Web of Science 내보내기 파일을 기존 검색 결과와 합쳐 '새로 나온 것'만 골라낸다.

사용 (저장소 최상위에서):
  python3 scripts/import_scopus_wos.py search/supp/scopus_B1.csv search/supp/wos_B1.txt ... \
      --out review/supp_scopus_wos_new.csv

입력 형식(자동 판별)
- Scopus: Export → CSV (쉼표 구분, 열 이름 Title/Year/Source title/DOI/Abstract/Authors/Document Type)
- WoS:    Export → Tab delimited file (열 이름 TI/PY/SO/DI/AB/AU/DT) 또는 Excel(.xls)을 CSV로 저장한 것

처리
1. DOI → 정규화 제목 순으로 기존 레코드(review/screening_all_records.csv, OpenAlex 판독분
   review/screening_openalex.csv, 포함 438편)와 대조해 중복 제거
2. 남은 '신규'에 1차 선별과 같은 규칙 적용(주택 맥락어 + 유동성 지표어, 노이즈 제외, 1986년 이후, 학술지 논문)
3. 결과를 --out 에 쓴다. decision 열이 비어 있는 행을 Claude가 판독한다.
"""
import argparse, csv, re, sys, html
csv.field_size_limit(10**9)

CTX = re.compile(r"\b(hous\w*|home\w*|residential|dwelling\w*|apartment\w*|condo\w*|real estate|realt\w*|propert\w*|mls|multiple listing|listing\w*|seller\w*|homeowner\w*)\b", re.I)
H = r"(hous\w*|home\w*|residential|dwelling\w*|apartment\w*|condo\w*|real estate|realt\w*|propert\w*|mls|listing\w*|seller\w*)"
STRONG = re.compile(r"time[- ]on[- ](the[- ])?market|\btom\b|days[- ]on[- ](the[- ])?market|\bdom\b|marketing (time|duration|period|span)|selling (time|duration|period)|time[- ]to[- ](sale|sell)|listing duration|duration of (the )?(listing|marketing|sale)|probability of (a )?(sale|selling)|likelihood of (a )?sale|withdraw\w* (from|of|listing)|listing\w* withdraw\w*|relist\w*|re-list\w*|list(ing)? price (change|reduction|cut|revision|adjustment|strateg|setting|premium)\w*|(change|reduction|cut|revision)s? (in|of|to) (the )?(list|listing|asking) price|asking price|sale[s]?[- ]to[- ]list|list[- ]to[- ]sale|over[- ]?pric\w*|under[- ]?pric\w*|price dispersion|(" + H + r"\W+(\w+\W+){0,4})?liquidity|liquidity(\W+\w+){0,4}\W+" + H + r"|illiquid\w*|market tightness|tightness of (the )?" + H + r"|hot (and|or) cold|\b(hot|cold) (housing |real estate |property )?market|months.? (of )?(supply|inventory)|absorption rate|(for-sale|unsold|housing|home) inventor\w*|inventory of (unsold|homes|houses)|sales?[- ]to[- ](listing|inventory)s?|(housing|home|house) (sales )?turnover|turnover (rate|of (housing|homes|houses))|(transaction|sales|trading) volume|housing search (index|activity|duration|behavio)|search (index|volume|activity|behavio)\w*(\W+\w+){0,6}\W+(hous|home|real estate)", re.I)
NOISE = re.compile(r"\b(stock market|stock price|stocks?|equit(y|ies) market|bond\w*|REIT\w*|interbank|bank(ing)? liquidity|funding liquidity|liquidity (risk|creation|provision|premium)|monetary|central bank|crypto\w*|bitcoin|ETF|futures|derivative\w*|order book|bid-ask)\b", re.I)
ARTICLE = re.compile(r"^(ar|article|review|re|early access|article; early access)$", re.I)


def norm_title(t):
    t = html.unescape(re.sub(r"<[^>]+>", "", t or "")).lower()
    t = re.sub(r"[^a-z0-9가-힣 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def norm_doi(d):
    d = (d or "").strip().lower()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", d)


def read_any(path):
    raw = open(path, "rb").read()
    txt = raw.decode("utf-8-sig", errors="replace")
    first = txt.splitlines()[0] if txt else ""
    delim = "\t" if first.count("\t") > first.count(",") else ","
    rows = list(csv.DictReader(txt.splitlines(), delimiter=delim))
    out = []
    for r in rows:
        g = lambda *ks: next((r[k] for k in ks if k in r and r[k]), "")
        out.append(dict(
            source="WoS" if "TI" in r else "Scopus",
            file=path,
            title=g("Title", "TI", "Article Title"),
            year=g("Year", "PY", "Publication Year"),
            venue=g("Source title", "SO", "Source Title"),
            doi=norm_doi(g("DOI", "DI")),
            abstract=g("Abstract", "AB"),
            authors=g("Authors", "AU", "Author full names"),
            doctype=g("Document Type", "DT"),
            language=g("Language of Original Document", "LA", "Language"),
        ))
    return out


def load_existing():
    dois, titles = set(), set()
    for path, dcol, tcol in [("review/screening_all_records.csv", "doi", "title"),
                             ("review/screening_openalex.csv", "doi", "title"),
                             ("review/included_studies.csv", "doi", "title")]:
        try:
            for r in csv.DictReader(open(path, encoding="utf-8")):
                if r.get(dcol):
                    dois.add(norm_doi(r[dcol]))
                if r.get(tcol):
                    titles.add(norm_title(r[tcol]))
        except FileNotFoundError:
            print("주의: 없음", path, file=sys.stderr)
    return dois, titles


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    recs = []
    for f in a.files:
        recs += read_any(f)
    dois, titles = load_existing()
    seen = set()
    counts = dict(read=len(recs), dup_existing=0, dup_within=0, not_article=0, pre1986=0, noise=0, no_context=0, weak=0, to_read=0)
    out = []
    for r in recs:
        k = r["doi"] or norm_title(r["title"])
        if k in seen:
            counts["dup_within"] += 1
            continue
        seen.add(k)
        if (r["doi"] and r["doi"] in dois) or norm_title(r["title"]) in titles:
            counts["dup_existing"] += 1
            continue
        text = (r["title"] or "") + " || " + (r["abstract"] or "")
        code = ""
        if r["doctype"] and not ARTICLE.match(r["doctype"].strip()):
            code = "E2-doctype"; counts["not_article"] += 1
        elif r["year"].isdigit() and int(r["year"]) < 1986:
            code = "E4-pre1986"; counts["pre1986"] += 1
        elif NOISE.search(r["title"] or "") and not re.search(r"hous|home|real estate|residential|propert", r["title"] or "", re.I):
            code = "E1-noise"; counts["noise"] += 1
        elif not CTX.search(text):
            code = "E3-nocontext"; counts["no_context"] += 1
        elif not STRONG.search(text):
            code = "E2-weak-only"; counts["weak"] += 1
        else:
            counts["to_read"] += 1
        r["rule"] = code
        r["decision"] = "" if not code else code
        r["note"] = ""
        out.append(r)
    out.sort(key=lambda r: (r["rule"] != "", r["year"]))
    w = csv.DictWriter(open(a.out, "w", encoding="utf-8", newline=""), fieldnames=list(out[0].keys()) if out else ["title"])
    w.writeheader()
    w.writerows(out)
    for k, v in counts.items():
        print(f"{k:14s} {v}")
    print("→", a.out, "(decision 빈 행 = 판독 대상)")


if __name__ == "__main__":
    main()
