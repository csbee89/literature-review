#!/usr/bin/env python3
"""체계적 문헌고찰 보조 도구 (표준 라이브러리만 사용).

  dedupe   여러 CSV/JSON 서지 파일을 합쳐 DOI → 정규화 제목+연도 순으로 중복 제거
  kappa    두 선별자의 include/exclude 판정 CSV에서 Cohen's kappa 산출
  openalex OpenAlex works 검색을 CSV로 저장 (재현 가능한 검색 로그)

예:
  python3 scripts/slr_tools.py dedupe raw/*.csv scans/*.json --out merged.csv
  python3 scripts/slr_tools.py kappa templates/screening_log.csv --col1 decision_1 --col2 decision_2
  python3 scripts/slr_tools.py openalex --query '"time on the market" housing' --from 1986 --out raw/oa_tom.csv --mailto you@univ.ac.kr
"""
import argparse, csv, json, re, sys, time, urllib.parse, urllib.request

def norm_title(t):
    t = re.sub(r"<[^>]+>", "", t or "")
    t = t.lower()
    t = re.sub(r"[^a-z0-9가-힣 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d

def load_records(path):
    recs = []
    if path.endswith(".json"):
        data = json.load(open(path, encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("records") or data.get("results") or data.get("items") or []
        for r in data:
            recs.append({
                "title": r.get("title") or "",
                "year": r.get("year") or r.get("publication_year") or "",
                "doi": r.get("doi") or "",
                "journal": r.get("journal") or r.get("source") or "",
                "authors": "; ".join(r.get("authors", [])) if isinstance(r.get("authors"), list) else r.get("authors", ""),
                "source_file": path,
            })
    else:
        with open(path, encoding="utf-8-sig", newline="") as f:
            rd = csv.DictReader(f)
            for r in rd:
                low = {k.lower(): v for k, v in r.items() if k}
                recs.append({
                    "title": low.get("title") or low.get("article title") or low.get("document title") or "",
                    "year": low.get("year") or low.get("publication year") or low.get("py") or "",
                    "doi": low.get("doi") or low.get("di") or "",
                    "journal": low.get("journal") or low.get("source title") or low.get("so") or "",
                    "authors": low.get("authors") or low.get("author") or low.get("au") or "",
                    "source_file": path,
                })
    return recs

def cmd_dedupe(a):
    recs = []
    for p in a.files:
        recs.extend(load_records(p))
    n0 = len(recs)
    seen_doi, seen_tit, out = set(), set(), []
    for r in recs:
        d = norm_doi(r["doi"])
        key_t = (norm_title(r["title"]), str(r["year"])[:4])
        if d:
            if d in seen_doi:
                continue
            seen_doi.add(d)
        if key_t[0]:
            if key_t in seen_tit:
                continue
            seen_tit.add(key_t)
        out.append(r)
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "year", "doi", "journal", "authors", "source_file"])
        w.writeheader(); w.writerows(out)
    print(f"입력 {n0}건 → 중복 제거 후 {len(out)}건 (제거 {n0-len(out)}건). 저장: {a.out}")
    print("PRISMA 흐름도용: 식별(identification) = %d, 중복 제거 = %d, 선별 대상 = %d" % (n0, n0-len(out), len(out)))

def cmd_kappa(a):
    pairs = []
    with open(a.file, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            x, y = (r.get(a.col1) or "").strip().lower(), (r.get(a.col2) or "").strip().lower()
            if x in ("include", "exclude") and y in ("include", "exclude"):
                pairs.append((x, y))
    n = len(pairs)
    if n == 0:
        sys.exit("판정 쌍이 없습니다 (값은 include/exclude 여야 함)")
    po = sum(1 for x, y in pairs if x == y) / n
    p1 = sum(1 for x, _ in pairs if x == "include") / n
    p2 = sum(1 for _, y in pairs if y == "include") / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    k = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    print(f"N={n}, 관측 일치율={po:.3f}, 기대 일치율={pe:.3f}, Cohen's kappa={k:.3f}")
    print("해석: <0.4 낮음 / 0.4–0.6 보통 / 0.6–0.8 상당 / >0.8 거의 완전. 프로토콜 기준 0.6 이상에서 본 선별 시작")

def cmd_openalex(a):
    base = "https://api.openalex.org/works"
    params = {"search": a.query, "filter": f"from_publication_date:{a.dfrom}-01-01,type:article", "per-page": 200, "cursor": "*"}
    if a.mailto:
        params["mailto"] = a.mailto
    rows = []
    while True:
        url = base + "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={"User-Agent": f"slr_tools ({a.mailto or 'no-mailto'})"})
        try:
            data = json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            print("요청 실패:", e, "— 10초 후 재시도", file=sys.stderr); time.sleep(10); continue
        for w in data.get("results", []):
            rows.append({
                "title": w.get("title") or "",
                "year": w.get("publication_year") or "",
                "doi": norm_doi(w.get("doi") or ""),
                "journal": ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "",
                "authors": "; ".join(x.get("author", {}).get("display_name", "") for x in w.get("authorships", [])[:6]),
                "cited_by": w.get("cited_by_count"),
                "openalex_id": w.get("id"),
            })
        nxt = (data.get("meta") or {}).get("next_cursor")
        if not nxt or len(rows) >= a.limit:
            break
        params["cursor"] = nxt; time.sleep(1.0)
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["title"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)}건 저장: {a.out}  (검색식: {a.query}; from {a.dfrom}; 실행 {time.strftime('%Y-%m-%d')})")
    print("→ templates/search_log.csv에 이 줄을 기록하십시오.")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    d = sp.add_parser("dedupe"); d.add_argument("files", nargs="+"); d.add_argument("--out", required=True); d.set_defaults(fn=cmd_dedupe)
    k = sp.add_parser("kappa"); k.add_argument("file"); k.add_argument("--col1", default="decision_1"); k.add_argument("--col2", default="decision_2"); k.set_defaults(fn=cmd_kappa)
    o = sp.add_parser("openalex"); o.add_argument("--query", required=True); o.add_argument("--from", dest="dfrom", default="1986"); o.add_argument("--limit", type=int, default=2000); o.add_argument("--out", required=True); o.add_argument("--mailto", default=""); o.set_defaults(fn=cmd_openalex)
    a = ap.parse_args(); a.fn(a)

if __name__ == "__main__":
    main()
