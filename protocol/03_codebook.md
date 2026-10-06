# 추출 양식 코드북 (`templates/extraction_form.csv`)

**분석 단위 = 지표(indicator)**. 한 논문이 지표를 셋 쓰면 세 행. `study_id`로 묶는다.
모든 셀은 **원문에서 확인한 것만** 적는다. 원문에 없으면 `NR`(not reported), 판단이 필요하면 `?`를 붙이고 `notes`에 쪽수와 함께 이유를 쓴다. 추측해서 채우지 않는다.

## A. 서지 (논문 단위, 지표 행마다 반복)

| 열 | 정의 | 코드/형식 |
|---|---|---|
| `study_id` | 제1저자 성 + 연도 (동일 시 a/b) | `Knight2002` |
| `authors` | 전 저자, 세미콜론 구분 | |
| `year` | 게재 연도 | YYYY |
| `title` | 원제 | |
| `journal` | 학술지·기관 (워킹페이퍼는 시리즈명) | |
| `vol_issue_pages` | 권(호):쪽 | `30(2):125-160` |
| `doi` | DOI (없으면 URL) | |
| `pub_type` | `journal` / `wp` / `report` / `chapter` | |
| `language` | `en` / `ko` / other | |
| `verified` | Crossref/KCI 실존 확인 여부 | `Y` / `N` / `manual` |

## B. 맥락

| 열 | 정의 | 코드 |
|---|---|---|
| `country` | 자료 국가 | ISO2 (`US`,`KR`,`NL`,`CA`,`CN`,`JP`...) |
| `region_scale` | 공간 범위 | `national` / `metro` / `city` / `neighborhood` / `multi-country` |
| `market_type` | 시장 | `owner-sale` / `rental` / `commercial` / `mixed` |
| `housing_type` | 주택 유형 | `SFH` / `condo-apt` / `mixed` / `NR` |
| `period_start`, `period_end` | 자료 기간 | YYYY |
| `market_phase` | 저자가 명시한 국면 | `boom` / `bust` / `mixed` / `NR` |
| `mls_market` | MLS 또는 중앙화된 매물 등록 체계 존재 여부 | `Y` / `N` / `partial` |

## C. 지표 정의 (핵심)

| 열 | 정의 | 코드 |
|---|---|---|
| `indicator_name` | 저자 표기 그대로 | `TOM`, `DOM`, `CDOM`, `price cut`, `sale-to-list ratio`, `liquidity index`... |
| `indicator_tier` | 프로토콜 §3 층 | `A` 시간 / `B` 가격조정 / `C` 집계 / `D` 대안데이터 |
| `indicator_role` | 모형 내 역할 | `DV` / `IV`(설명변수) / `constructed`(구축 대상) / `instrument` |
| `definition_verbatim` | **원문 정의 인용** (쪽수 포함) | 예: "the number of days between the listing date and the contract date (p. 7)" |
| `unit` | 단위 | `days` / `weeks` / `months` / `%` / `ratio` / `index` / `probability` |
| `start_event` | 시간 지표의 시작 사건 | `listing` / `first-listing(cumulative)` / `NR` / `NA` |
| `end_event` | 종료 사건 | `contract` / `closing` / `delisting` / `withdrawal` / `NR` / `NA` |
| `censoring` | 미거래·철회 매물 처리 | `excluded` / `right-censored(survival)` / `competing-risk` / `NR` / `NA` |
| `relisting_handling` | 재등록 처리 | `reset` / `cumulative` / `linked-by-algorithm` / `excluded` / `NR` / `NA` |
| `duplicate_handling` | 중복 등재 처리 | `NA(MLS unique)` / `dedup-rule` / `NR` |
| `aggregation` | 집계 방식 | `individual` / `mean` / `median` / `quality-adjusted` / `index-model` |
| `quality_adjustment` | 품질 통제 | `hedonic` / `repeat` / `none` / `NR` |

## D. 자료·방법

| 열 | 정의 | 코드 |
|---|---|---|
| `data_source` | 자료원 유형 | `MLS` / `platform-scrape` / `platform-provided` / `registry-transaction` / `survey` / `search-volume` / `news` / `admin` |
| `data_source_name` | 명칭 | `Zillow`, `Funda`, `NVM`, `네이버부동산`... |
| `n_obs` | 관측치 수 | 정수 |
| `method_family` | 방법 | `descriptive` / `hedonic-OLS` / `survival(Cox/Weibull/KM)` / `simultaneous(2SLS/3SLS/SUR)` / `structural-search` / `index-construction` / `panel-FE` / `VAR-Granger` / `ML` / `theory-only` |
| `endogeneity_treatment` | TOM↔가격 동시성 처리 | `none` / `IV` / `simultaneous` / `structural` / `NA` |
| `heterogeneity_dims` | 보고된 이질성 축 | `price-tier; type; region; phase; seller-type` 중 해당 (세미콜론) |

## E. 결과 (선행성·관계)

| 열 | 정의 | 코드 |
|---|---|---|
| `outcome_var` | 지표가 관계 맺는 변수 | `sale price` / `price index` / `volume` / `probability of sale` / `other` |
| `effect_direction` | 방향 | `+` / `-` / `0` / `mixed` |
| `effect_size_verbatim` | 크기 원문 (계수·탄력성·% 등) 쪽수 포함 | 예: "10% longer TOM → 0.8% lower price (2SLS, p. 15)" |
| `lead_lag` | 선행 시차 (가격·거래량 대비) | 예: `leads price by 2-3 quarters` / `contemporaneous` / `NA` |
| `lead_test` | 선행성 검정 방법 | `Granger` / `cross-corr` / `forecast-eval` / `event-study` / `none` |
| `phase_dependence` | 국면별 차이 보고 | 자유 서술 (짧게) |

## F. 평가·메모

| 열 | 정의 |
|---|---|
| `q1_definition` ... `q6_reproducibility` | 프로토콜 §9의 6항목, 각 0/1/2 |
| `limitations_author` | 저자 한계 절 요약 2문장 이내 |
| `gap_axis` | 다섯 축 중 비어 있는 것: `data` / `region` / `period` / `group` / `mechanism` (복수 가능) |
| `relevance_to_KR` | 한국 적용 함의 1문장 (비MLS·중복등재·재등록 관점) |
| `extractor`, `checker`, `date_extracted` | |
| `notes` | 그 외 전부 |

## 기재 예시

`templates/extraction_form.csv`의 첫 두 행은 학생 정리 예시(Tucker et al., 2013; Dubé & Legros, 2016)를 이 양식으로 옮긴 것이다. 정리문에 없던 항목은 `NR`로 두었다. **이 `NR`들이 곧 "요약문만으로는 추출이 안 된다"는 증거다** — 전문을 열어 채워야 한다.
