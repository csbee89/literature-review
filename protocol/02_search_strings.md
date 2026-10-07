# 검색식 (DB별)

구조: **[유동성 개념 블록] AND [주택·부동산 맥락 블록]**, 하위 블록 ①②③을 따로 실행해 결과 수를 각각 기록한 뒤 합집합.
스코핑 근거: `scans/liq.md` — "housing market liquidity index"로 Crossref 199편을 받았을 때 주택 관련은 약 25편, 나머지는 주식·채권·은행 유동성. 맥락 블록 없이는 못 쓴다.

## 0. 개념 블록

### ① 매물 체류시간 계열
```
"time on market" OR "time on the market" OR "time-on-market" OR "time-on-the-market"
OR "days on market" OR "days-on-market" OR "marketing time" OR "marketing duration"
OR "marketing period" OR "selling time" OR "time to sale" OR "time-to-sale"
OR "duration of marketing" OR "listing duration" OR "probability of sale"
OR "withdrawal" OR "withdrawn listing*" OR "relist*" OR "re-list*" OR "listing survival"
```

### ② 호가 조정 계열
```
"list price" OR "listing price" OR "asking price" OR "price cut*" OR "price reduction*"
OR "price revision*" OR "list price change*" OR "sale-to-list" OR "sales-to-list"
OR "list-to-sale" OR "overpricing" OR "degree of overpricing" OR "underpricing"
OR "price dispersion" OR "reservation price"
```

### ③ 시장 유동성·긴장도 계열
```
"housing market liquidity" OR "housing liquidity" OR "real estate liquidity"
OR "market liquidity index" OR "liquidity index" OR "liquidity measure*"
OR "market tightness" OR "market heat" OR "hot market*" OR "cold market*"
OR "months of inventory" OR "months' supply" OR "absorption rate" OR "inventory age"
OR "sales-to-listings" OR "sale-to-inventory" OR "turnover rate" OR "transaction volume"
OR "liquidity-adjusted" OR "constant-liquidity" OR "variable liquidity"
```

### 맥락 블록 (모든 하위 블록에 공통 AND)
```
hous* OR home* OR residential OR dwelling* OR apartment* OR condominium* OR "real estate" OR property OR MLS OR "multiple listing"
```

### 제외 블록 (NOT) — 선별 단계에서 적용해도 되지만 ③에는 검색 단계에서 적용 권장
```
NOT (stock* OR bond* OR equit* OR REIT* OR "interbank" OR "funding liquidity"
     OR "monetary" OR "central bank" OR crypto* OR "order book" OR "bid-ask")
```
> 주의: REIT 제외는 ③에서만. ①②에서는 REIT가 거의 안 나온다. "Property market liquidity and REIT liquidity"(Real Estate Economics, 2022)처럼 자산 유동성과 증권 유동성을 연결한 논문은 NOT에 걸릴 수 있으므로 ③ 실행 시 NOT 없는 버전 결과 수도 함께 기록해 둔다.

---

## 1. Scopus (TITLE-ABS-KEY)

블록 ①:
```
TITLE-ABS-KEY( ( "time on market" OR "time on the market" OR "time-on-market" OR "time-on-the-market" OR "days on market" OR "days-on-market" OR "marketing time" OR "marketing duration" OR "selling time" OR "time to sale" OR "listing duration" OR "probability of sale" OR "withdrawn listing*" OR relist* OR "listing survival" )
AND ( hous* OR home* OR residential OR dwelling* OR apartment* OR condominium* OR "real estate" OR "multiple listing" ) )
AND PUBYEAR > 1985 AND ( LIMIT-TO ( LANGUAGE , "English" ) OR LIMIT-TO ( LANGUAGE , "Korean" ) )
AND ( LIMIT-TO ( DOCTYPE , "ar" ) OR LIMIT-TO ( DOCTYPE , "re" ) )   -- 문서유형 제한은 ②③에도 동일 적용 (학술지 논문만)
```
블록 ②:
```
TITLE-ABS-KEY( ( "list price" OR "listing price" OR "asking price" OR "price cut*" OR "price reduction*" OR "price revision*" OR "sale-to-list" OR "list-to-sale" OR overpricing OR "degree of overpricing" OR "price dispersion" OR "reservation price" )
AND ( hous* OR home* OR residential OR dwelling* OR apartment* OR "real estate" OR "multiple listing" )
AND ( liquidity OR "time on market" OR "time on the market" OR "days on market" OR "selling time" OR "probability of sale" ) )
AND PUBYEAR > 1985
```
> ②는 호가 논문이 너무 많아 유동성·TOM 연결어를 세 번째 AND로 걸었다. 결과가 300건 미만이면 세 번째 AND를 제거한 버전도 돌려 비교한다.

블록 ③:
```
TITLE-ABS-KEY( ( "housing market liquidity" OR "housing liquidity" OR "real estate liquidity" OR "liquidity index" OR "liquidity measure*" OR "market tightness" OR "market heat" OR "months of inventory" OR "absorption rate" OR "inventory age" OR "sales-to-listings" OR "turnover rate" OR "liquidity-adjusted" OR "constant-liquidity" OR "variable liquidity" )
AND ( hous* OR home* OR residential OR dwelling* OR apartment* OR "real estate" )
AND NOT ( stock* OR bond* OR interbank OR "funding liquidity" OR monetary OR "central bank" OR crypto* OR "bid-ask" ) )
AND PUBYEAR > 1985
```

## 2. Web of Science (TS=)

Scopus 식에서 `TITLE-ABS-KEY(...)` → `TS=(...)`, `PUBYEAR > 1985` → 타임스팬 1986–현재, 문서유형 Article/Review/Early Access. 와일드카드 `*` 동일. 인용색인: SSCI, SCIE, ESCI 모두 포함(ESCI에 IJHMA·JERER 등이 있음).

## 3. EconLit (EBSCO) / RePEc IDEAS

- EconLit: 위 식을 `AB` 필드로. JEL 코드 보조 필터 `R21 OR R31 OR R32 OR D83`.
- IDEAS: 불리언 지원이 약하다. 핵심 구 7개를 개별 검색: `"time on the market" housing`, `"days on market"`, `"housing market liquidity"`, `"liquidity index" housing`, `"list price" "time on market"`, `"market tightness" housing`, `"months of inventory"`. 결과는 수작업으로 Zotero에 넣고 `source=IDEAS`로 태그.

## 4. SSRN — 사용하지 않음 (범위 '좁게': 동료심사 학술지만)

## 5. OpenAlex / Crossref (API, 재현 가능 로그)

```bash
# OpenAlex (429 오류 시 mailto 파라미터 추가하고 1초 간격)
python3 scripts/slr_tools.py openalex --query '"time on the market" housing' --from 1986 --out raw/oa_tom.csv
python3 scripts/slr_tools.py openalex --query '"housing market liquidity"' --from 1986 --out raw/oa_liq.csv
# Crossref (skill 스크립트 재사용)
python3 <sb-paper>/scripts/scan_journal.py --topic "time on market housing" --engine crossref --from 1986 --limit 500 --out raw/cr_tom.json
```
> OpenAlex는 `search=` 파라미터가 제목·초록·전문을 모두 뒤져 민감도가 높고 정밀도가 낮다. 보조 DB로만.

## 6. 국내: KCI / RISS / DBpia / ScienceON

한국어 용어가 통일돼 있지 않다. 아래 동의어를 **전부** 개별 검색한다.

| 개념 | 국문 검색어 |
|---|---|
| TOM/DOM | 매물 소진기간, 매물소진기간, 시장체류기간, 매각기간, 판매기간, 매도기간, 매매 소요기간, 거래 소요기간, 매물 체류, 소진 기간 아파트 |
| 호가 조정 | 호가, 호가 조정, 호가 인하, 매도호가, 매물가격, 희망가격, 호가와 실거래가 격차 |
| 시장 유동성 | 주택 유동성, 부동산 유동성, 환금성, 거래 회전율, 주택 거래량 지표, 거래활동지표, 매물 적체, 매물 잠김, 거래절벽, 매수우위지수, 매매거래지수 |
| 자료원 | 매물 데이터, 매물 정보 크롤링, 네이버 부동산 매물, 직방, 호갱노노, 아실 |

KCI OpenAPI(`articleSearch`, 인증키 필요)로 제목·초록·키워드 검색 후 CSV 저장. 키가 없으면 RISS 웹 검색 결과를 RIS로 내보내 Zotero에 적재한다.

> 스코핑에서 Crossref에 잡힌 국내 문헌 예: 고진수·최성호·노승철(2019, 주택연구 27(1), doi:10.24957/hsr.2019.27.1.05) 서울 주거용 부동산 매물소진기간 결정요인; 양재영·고진수(2019, 도시정책연구 10(3), doi:10.21447/jup.2019.10.3.101) 아파트 특성과 DOM; 오윤경(2026, 부동산학보 44(3), doi:10.37407/kres.2026.44.3.315) 부산 가격차별화·거래유동성 유형화. 저자 표기는 Crossref 로마자 표기를 역변환한 것이므로 **원문 확인 필요**.

## 7. 회색문헌 (코퍼스 외 — RQ5 한국 현황 서술의 배경자료)

| 기관 | 검색어 | 비고 |
|---|---|---|
| 국토연구원 | 거래활동지표, 매물, 유동성 | 권건우(2025) 거래활동지표 보고서 포함 |
| LH 토지주택연구원 | 매물 소진기간, 매도 소요기간 | 2022년 매물 소진기간(주 단위) 집계 보도 있음(경향신문 2022-10-25) — 원보고서 확인 필요 |
| KDI | 주택 거래량, 양도소득세, 잠김 | 문윤상(2024) KDI FOCUS |
| 한국은행 | 주택시장 유동성, 거래 | |
| 한국부동산원·KB·주산연 | 매수우위지수, 매매거래활발지수, 매물 지수 | 서베이 기반 지표의 정의 수록 |
| 해외 기관 | Zillow Research(DOM 정의), Redfin Data Center, NAR(months supply), Fed Notes(Anenberg) | 플랫폼 지표 정의 비교 |

## 8. 기록 규칙

`templates/search_log.csv`에 한 행씩: 실행일, DB, 블록, 검색식 전문, 필터, 결과 수, 내보낸 파일명, 실행자. 검색식을 바꾸면 새 행을 추가하고 이전 행은 지우지 않는다.
