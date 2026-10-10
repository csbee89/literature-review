# PRISMA 2020 흐름도 수치와 선별 방법 (검색 실행 2026-10-10)

> 이 문서의 숫자는 `scripts/*.py` 파이프라인이 산출한 파일(`review/screening_all_records.csv`, `review/screening_read_set.csv`, `review/included_studies.csv`)에서 그대로 집계한 것이다. 논문 3장과 흐름도(Figure 1)에 들어간다.

## 1. 식별 (Identification)

| 경로 | 데이터베이스·방법 | 레코드 |
|---|---|---|
| 데이터베이스 검색 | Semantic Scholar bulk search API — 블록 ①②③ 불리언 검색 (1986~) | 4,351 |
| 데이터베이스 검색 | Crossref — 28개 구문 × 관련도 상위 600 (journal-article, 1986~) | 16,800 |
| 핵심 저널 수작업 검색 | Crossref ISSN 전수 — 16개 학술지 (REE, JREFE, JHE, JUE, RSUE, JHR, JRER, Housing Studies, IJHMA, JPR, JREL, HPD, JHBE, Urban Studies, JERER, REMV), 1986~ 전체 논문 | 26,581 |
| 인용 추적 | Semantic Scholar 전방 인용 — Kluger & Miller 1990, Haurin 1988, Carrillo 2013, Knight 2002, Sirmans et al. 2010 (후방 인용은 S2에 참고문헌 미등록) | 876 |
| **합계** | | **48,608** |

중복 제거(DOI → 정규화 제목; 프리프린트·게재본은 게재본 우선): **35,397**건.

**사용하지 못한 DB**: Scopus, Web of Science, EconLit(기관 구독 필요), KCI(OpenAPI 키 미발급), OpenAlex(공용 IP 일일 한도 소진). → §5 보완 검색 참조.

## 2. 선별 (Screening)

| 단계 | 방법 | 제외 | 잔여 |
|---|---|---|---|
| A. 규칙 선별 | 제목·초록에 (i) 주택 맥락어 (ii) 유동성 관련어가 모두 있어야 통과. 금융·재료과학 등 노이즈 어휘 제외. 1986년 이전 제외 | 맥락어 없음 17,271 / 지표어 없음 12,185 / 노이즈 2,164 / 프리프린트 표식 78 | 3,777 |
| B. 강한 지표어 규칙 | TOM·DOM·marketing time·list price change·sale-to-list·housing liquidity·tightness·months' supply 등 '강한' 용어가 있어야 통과(`review/screening_rules.md`) | 약한 용어만 2,847 / 과학 저널 86 | 844 |
| B′. 복구 패스 | 규칙 A·B가 놓친 것 재검색: (a) 검색량·온라인 매물 데이터(D층) 어휘, (b) 하이픈 표기(list-price), (c) 제목에 주택 단어가 없는 TOM 논문(예: "Selling price, time on the market, and contractual contingencies") | — | +51 후보 → 36 포함 |
| C. 제목·초록 판독 | 844건 전수 판독, 판정 코드 부여 (I 포함 / E1~E4 제외 / V 게재본 확인 / M 보류 / R 선행 리뷰) | E1 332, E2 75, E3 67, E4 30, R 2 | I 227, V 76, M 35 |
| D. 게재본 확인 | V·M 111건을 Crossref 제목 검색으로 학술지 게재본 확인 | V→E4(게재본 없음) 55, 중복 25 / M→E 12 | V→I 12, M→I 32 |
| E. 다른 방법으로 식별 | 앵커 문헌(검색 미회수 21편: AER·JPE·REStud·IER 등 일반 경제학 저널), 복구 패스 36편, 게재본 전환 10편 | | +67 |

판독 단계 판정자: Claude(AI 보조) 1인 — **반드시 인간 2인 재판독으로 보완**(§4). 모든 판정과 사유는 `review/screening_read_set.csv`(열 `decision`, `note`)에 있다.

## 3. 포함 (Included)

| 구분 | 편수 |
|---|---|
| **포함 총계** | **340** (이 중 15편은 `I?` — 초록만으로 지표 측정 여부가 불확실, 전문 확인 후 확정) |
| 층(layer) | core 216 / peripheral 96 / theory 28 |
| 지표 tier | A(매물 시간) 131 · B(호가) 65 · C(시장 집계) 57 · D(대안 데이터) 14 · T(이론) 26 · 복합 47 |
| 연대 | 1986–89: 6 · 1990s: 25 · 2000s: 51 · 2010s: 134 · 2020s: 124 |
| 출처 | DB 선별 258 · 앵커 21 · 복구 36 · 게재본 전환 10 → 중복 제거 후 340 |
| DOI 미확정 | 4편 (IRER 2003·2011, AAFSJ 2003, J. Econ. Sustainable Dev. 2015) |

앵커 회수율(검색 단계, 진짜 앵커 40편 기준): 37/40 = 92.5%. 미회수 3편(Head et al. 2014 AER, Ngai & Tenreyro 2014 AER, Guren 2018 JPE)은 일반 경제학 저널로 핵심 저널 수작업 검색 범위 밖 → "다른 방법" 경로로 추가.

## 4. 논문에 써야 할 한계와 보완 (반드시 기재)

1. **DB 범위**: Scopus·WoS·EconLit·KCI 미사용. Semantic Scholar·Crossref는 초록 커버리지가 불완전(판독 844건 중 초록 보유 688건)해 제목만으로 판정한 건이 있다. → **보완 검색**(§5)을 W1~W3에 실행하고 추가 식별 건수를 흐름도에 "추가 검색" 행으로 넣는다.
2. **AI 보조 선별**: 규칙 선별(A·B)은 재현 가능한 정규식이고, 판독(C)은 AI 1인이 했다. PRISMA 2020 항목 8(선별 과정)에 "자동화 도구 사용"으로 기재하고, **인간 2인(이원석·석사①)이 (a) 판독 844건 중 무작위 10%(85건) (b) `I?` 15건 (c) E2·E3 판정 142건 전수를 독립 재판독**해 κ를 보고한다. 불일치는 연구책임자가 결정.
3. **국문 문헌**: KCI 미검색. Crossref에 등록된 국문 학술지 논문 4편만 포함(주택연구 2, 도시정책연구 1, 부동산학보 1, 부동산·도시연구 1). KCI 키 발급 후 `protocol/02_search_strings.md` §6 동의어로 검색해 추가.
4. **저널 품질**: 동료심사 학술지만 포함했으나 색인 수준은 통제하지 않았다. 저품질 추정 저널 논문 6편(AAFSJ, IISTE J. Econ. Sust. Dev., Jurnal Ilmu Manajemen, Lapai J., UNIOSUN J. Eng., Dinasti=제외)이 있다. → **결정 필요**: "Scopus·WoS·KCI 색인 학술지"로 기준을 좁힐지.

## 5. 보완 검색 지시 (원석, W1~W3)

- Scopus·WoS: `protocol/02_search_strings.md` §1~2 식 그대로 실행 → RIS 내보내기 → `scripts/slr_tools.py dedupe`로 기존 35,397건과 합쳐 **신규 레코드만** 추출 → 신규분만 규칙 A·B 적용 후 판독. 결과를 `review/supplementary_search.md`에 기록.
- KCI: 키 발급 즉시 §6 동의어 전수 검색.
- OpenAlex: 교수님 API 키(무료) 발급 시 `scripts/slr_tools.py openalex`로 블록 ①②③ 재실행해 교차 확인.
