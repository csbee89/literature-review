# Scopus·Web of Science 보완 검색 — 실행 안내 (교수 직접, 약 1시간)

Scopus와 WoS는 가천대 구독 DB라 **학교 계정으로 로그인한 사람만** 검색할 수 있다. Claude는 로그인할 수 없으므로, 교수가 아래 식을 붙여 넣고 결과 파일을 내보내 저장소에 올리면 나머지(기존 37,104건과 중복 제거, 규칙 선별, 판독, PRISMA 숫자 갱신)는 Claude가 한다.

## 0. 준비
- 학교 밖이면 가천대 도서관 홈페이지 로그인 → 학술DB → Scopus / Web of Science 로 들어간다(교내 IP로 연결됨).
- 저장소에 폴더 `search/supp/`를 만든다. 내보낸 파일은 모두 여기에 넣는다.
- 각 검색의 **실행 날짜와 결과 건수**를 `templates/search_log.csv`에 한 줄씩 적는다(아래 표의 이름 그대로).

## 1. Scopus — Advanced search 칸에 그대로 붙여 넣기

**S1 (매물 체류시간)**
```
TITLE-ABS-KEY(("time on market" OR "time on the market" OR "time-on-market" OR "time-on-the-market" OR "days on market" OR "days-on-market" OR "marketing time" OR "marketing duration" OR "selling time" OR "time to sale" OR "listing duration" OR "probability of sale" OR "withdrawn listing*" OR relist* OR "listing survival") AND (hous* OR home* OR residential OR dwelling* OR apartment* OR condominium* OR "real estate" OR "multiple listing")) AND PUBYEAR > 1985 AND (LIMIT-TO(DOCTYPE,"ar") OR LIMIT-TO(DOCTYPE,"re")) AND (LIMIT-TO(LANGUAGE,"English") OR LIMIT-TO(LANGUAGE,"Korean"))
```

**S2 (호가 조정)**
```
TITLE-ABS-KEY(("list price" OR "listing price" OR "asking price" OR "price cut*" OR "price reduction*" OR "price revision*" OR "sale-to-list" OR "list-to-sale" OR overpricing OR "degree of overpricing" OR "price dispersion" OR "reservation price") AND (hous* OR home* OR residential OR dwelling* OR apartment* OR "real estate" OR "multiple listing") AND (liquidity OR "time on market" OR "time on the market" OR "days on market" OR "selling time" OR "probability of sale")) AND PUBYEAR > 1985 AND (LIMIT-TO(DOCTYPE,"ar") OR LIMIT-TO(DOCTYPE,"re")) AND (LIMIT-TO(LANGUAGE,"English") OR LIMIT-TO(LANGUAGE,"Korean"))
```

**S3 (시장 유동성·거래량)**
```
TITLE-ABS-KEY(("housing market liquidity" OR "housing liquidity" OR "real estate liquidity" OR "liquidity index" OR "liquidity measure*" OR "market tightness" OR "market heat" OR "hot market*" OR "cold market*" OR "months of inventory" OR "months supply" OR "absorption rate" OR "inventory age" OR "sales-to-listings" OR "housing turnover" OR "transaction volume" OR "trading volume" OR "sales volume") AND (hous* OR home* OR residential OR dwelling* OR apartment* OR "real estate") AND NOT (stock* OR bond* OR REIT* OR interbank OR "funding liquidity" OR monetary OR "central bank" OR crypto* OR "bid-ask")) AND PUBYEAR > 1985 AND (LIMIT-TO(DOCTYPE,"ar") OR LIMIT-TO(DOCTYPE,"re")) AND (LIMIT-TO(LANGUAGE,"English") OR LIMIT-TO(LANGUAGE,"Korean"))
```

**내보내기**: 결과 화면 → 전체 선택(Select all) → Export → **CSV** → 항목에서 *Citation information* 전체 + *Bibliographical information* + **Abstract & keywords** 체크 → Export.
한 번에 안 나가면 연도로 나눠서(예: 1986–2010, 2011–2026) 여러 파일로 내보낸다.
파일 이름: `search/supp/scopus_S1.csv`, `scopus_S2.csv`, `scopus_S3.csv` (나눴으면 `scopus_S3_a.csv`, `_b.csv`).

## 2. Web of Science — Advanced Search 칸에 붙여 넣기

데이터베이스는 **Web of Science Core Collection**, 색인은 SSCI·SCIE·ESCI 모두 포함(ESCI에 IJHMA·JERER가 있다).

**W1**
```
TS=(("time on market" OR "time on the market" OR "time-on-market" OR "time-on-the-market" OR "days on market" OR "days-on-market" OR "marketing time" OR "marketing duration" OR "selling time" OR "time to sale" OR "listing duration" OR "probability of sale" OR "withdrawn listing*" OR relist* OR "listing survival") AND (hous* OR home* OR residential OR dwelling* OR apartment* OR condominium* OR "real estate" OR "multiple listing")) AND PY=(1986-2026)
```

**W2**
```
TS=(("list price" OR "listing price" OR "asking price" OR "price cut*" OR "price reduction*" OR "price revision*" OR "sale-to-list" OR "list-to-sale" OR overpricing OR "degree of overpricing" OR "price dispersion" OR "reservation price") AND (hous* OR home* OR residential OR dwelling* OR apartment* OR "real estate" OR "multiple listing") AND (liquidity OR "time on market" OR "time on the market" OR "days on market" OR "selling time" OR "probability of sale")) AND PY=(1986-2026)
```

**W3**
```
TS=(("housing market liquidity" OR "housing liquidity" OR "real estate liquidity" OR "liquidity index" OR "liquidity measure*" OR "market tightness" OR "market heat" OR "hot market*" OR "cold market*" OR "months of inventory" OR "months supply" OR "absorption rate" OR "inventory age" OR "sales-to-listings" OR "housing turnover" OR "transaction volume" OR "trading volume" OR "sales volume") AND (hous* OR home* OR residential OR dwelling* OR apartment* OR "real estate") NOT (stock* OR bond* OR REIT* OR interbank OR "funding liquidity" OR monetary OR "central bank" OR crypto* OR "bid-ask")) AND PY=(1986-2026)
```

검색 후 왼쪽 필터에서 **Document Types = Article, Review Article, Early Access**만 남긴다.

**내보내기**: Export → **Tab delimited file** → Record Content **Full Record** → 1~1,000건씩(WoS는 한 번에 1,000건까지). 1,000건이 넘으면 1–1000, 1001–2000 … 으로 나눠 여러 번.
파일 이름: `search/supp/wos_W1_1.txt`, `wos_W1_2.txt` …

## 3. 올리고 Claude에게 알리기
1. 파일을 Claude 대화창에 첨부한다(또는 `search/supp/`에 넣고 커밋·푸시).
2. Claude가 다음을 실행한다.
```
python3 scripts/import_scopus_wos.py search/supp/* --out review/supp_scopus_wos_new.csv
```
기존 37,104건과 겹치는 것은 자동으로 빠지고, 남은 신규 건 중 주택 맥락어와 유동성 지표어가 함께 있는 것만 판독 대상으로 남는다. Claude가 판독하고, 새로 들어올 논문이 있으면 교수 O/X를 거쳐 종합 목록에 추가한다. 흐름도에는 "Scopus·WoS 보완 검색" 행이 추가된다.

## 4. 예상
이미 5개 경로(52,006건)를 돌렸고 핵심 학술지 16종은 전수 검색했으므로, 신규로 들어올 논문은 많지 않을 것이다. 그래도 PRISMA와 JHE 심사에서 "Scopus·WoS를 썼는가"는 거의 반드시 묻는 항목이라 실행 기록을 남기는 것이 목적이다.
