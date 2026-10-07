# [예시] 문헌 1쪽 정리 — 이 수준으로 가져오면 된다

**작성** 최승비 · **작성일** 2026-10-07 · **원문** `examples/Famiglietti_Garriga_Hedlund_2020_StLouisFedReview.pdf` (공개 자료, 28쪽)
**이 예시의 용도**: 매주 1편 정리의 기준선. 아래 항목이 모두 채워지고, 따옴표 안은 원문 그대로이며, 모든 수치와 인용에 쪽수가 붙어 있다. 원문에 없는 항목은 `NR`로 두었다. 이보다 짧으면 반려, 이보다 길 필요는 없다.

---

## 0. 서지
- **저자(전원)**: Famiglietti, Mathew; Garriga, Carlos; Hedlund, Aaron
- **연도**: 2020
- **제목**: The Geography of Housing Market Liquidity During the Great Recession
- **학술지 권(호):쪽**: Federal Reserve Bank of St. Louis *Review*, 102(1): 51–77
- **DOI**: 10.20955/r.102.51-77
- **문헌 유형**: 연방준비은행 리뷰 논문(동료심사 학술지 아님). **범위 '좁게'(2026-10-07) 기준으로는 코퍼스 밖(E4)**. 이 파일은 정리 양식의 기준 예시이며, 논문 본문에서는 2장 배경 인용으로만 쓴다
- **실존 확인**: Y (Crossref에서 DOI 열어 봄, 2026-10-06)

## 1. 한 줄 요약
CoreLogic MLS 매물 자료로 ZIP 코드 단위 TOM과 재고소진월수를 만들어, 대침체기(2005~2011) 유동성 악화가 지역별로 시점·크기가 달랐고 소득 감소·연체율 상승과 강하게 상관됨을 OLS로 보였다.

## 2. 지표 정의 (원문 인용, 쪽수)

| 지표명 | 층 | 역할 | 정의 원문 | 단위 | 시작 사건 | 종료 사건 | 미거래·철회 처리 | 재등록 처리 |
|---|---|---|---|---|---|---|---|---|
| TOM (time on the market) | A | 핵심 설명변수(ΔTOM) + 기술통계 | "our main measure of housing liquidity is time on the market (TOM), the number of days between listing a property and selling a property" (p. 51–52) | days (ZIP 코드 연평균) | listing | sale (closing) | 미거래 매물은 자료에 관측됨("both failed and successful listings are observed", p. 55)이나 회귀의 ΔTOM은 매각 건 기준. 철회 매물의 TOM 포함 여부 `NR` | **알고리즘으로 연결**: "we reconstruct the variable TOM by following the property from the initial listing to a complete sale or withdrawal from the market, allowing relistings or withdrawal from the market for less than three months. This three-month threshold seems to capture more than 75 percent of such incidences." (p. 72) |
| Months' supply | C | 보조 지표(결과는 TOM과 "very similar", 미보고) | "a market-level measure of housing liquidity that comes from dividing the stock of unsold listings by the number of houses sold in a given geography and month" (p. 59); "Months' supply is the ratio of houses for sale to houses sold" (endnote 5, p. 73) | months (월별 산출 후 연평균, p. 59) | NA | NA | NA | NA |

- **중복 등재 처리**: MLS 단일 체계라 해당 없음(`NA(MLS unique)`). 단 중개사 변경 시 TOM 리셋 문제를 명시: "The reported variable of TOM gets reset if the property is relisted with a different realtor." (p. 72)
- **이상치 처리**: 음수·1,460일 초과·결측 제거(p. 72); 회귀에서는 ΔTOM 상·하위 10% 윈저화 — "we winsorize the top and bottom 10 percent of the liquidity change measures" (p. 66)
- **품질 통제**: 없음(ZIP 평균, 헤도닉 보정 없음) → `none`

## 3. 자료와 방법
- **국가·지역·기간·주택유형**: 미국 전역 ZIP 코드(2006년 16,954개 → 2011년 20,109개, 인구 커버리지 74%→85%, p. 55). 분석 창 2005~2011(지역별 상이). 단독주택 + 콘도 한정(p. 55). **MLS 시장**: Y
- **자료원**: `MLS` — CoreLogic RADAR Data Warehouse의 MLS 매물 자료(등록일·호가·거래가·거래일·상태 변화 추적, p. 54–55, 71–72) + FRBNY CCP/Equifax 연체 + IRS SOI 소득
- **N**: ZIP 코드 9,356(소득 회귀)·9,410(연체 회귀), 전국 기준(Table 3·4, p. 67–68)
- **방법 가족**: `descriptive`(히트맵·커널밀도·KS 검정) + `panel-FE` 아님 → 장기차분 OLS: ΔOutcome = B0 + B1·ΔLiquidity + B2·ΔHousePrice, 2006년 납세자 수 가중(식 (1), p. 66)
- **내생성 처리**: `none`. 저자 명시: "this analysis uses ordinary least-square regression models that do not imply causality ... due to endogeneity of the dependent and independent variables" (p. 67–68)
- **이질성 축**: `region`(캘리포니아 / 선벨트 AZ·NV·FL / 기타), `price-tier`(분포 분위, p. 64), `supply-elasticity`(Saiz 탄력성 상·하위 사분위, p. 69)

## 4. 결과 (방향·크기·단위·쪽수 분리)

| 지표 → 결과변수 | 방향 | 크기(원문) | 선행 시차 | 검정 | 국면·집단별 차이 |
|---|---|---|---|---|---|
| ΔTOM → Δ실질소득(%) | − | 전국 B1 = −0.035*** (SE 0.006), "a one-month increase in TOM is associated with approximately a 1 percent decline in real income" (Table 3, p. 67) | 동시(장기차분, 선행성 검정 없음) | none | 선벨트 −0.021*, 캘리포니아 0.026(유의하지 않음), 기타 −0.020** (Table 3, p. 67) |
| ΔTOM → Δ연체율(%p) | + | 전국 0.043*** (SE 0.001); 캘리포니아 "a one-month increase in TOM is associated with a 2.0 percent increase in the mortgage delinquency rate" (0.066***, Table 4, p. 68) | 동시 | none | 선벨트 0.073***, 기타 0.020*** |
| TOM 수준 변화(기술통계) | ↑ | "the TOM, increased 40 percent, from 117 days to 164 days" 2006→2011 전국 평균; ΔTOM 평균 47.4일(Table 1, p. 55) | — | KS 검정 1% 유의(p. 60) | 선벨트 ΔTOM 92.9일 vs 캘리포니아 42.1일 vs 기타 34.8일(Table 2, p. 56); 캘리포니아·선벨트는 2007~08에 먼저 악화, 기타 지역은 2011에 최악(p. 59) |
| 가격 분위별 | — | "The deterioration in housing liquidity was uniform across all house price tiers" (초록, p. 51); 가격 하락도 분위 간 "strikingly uniform" (p. 64) | — | — | 분위 간 차이 없음 |
| 공급탄력성별 | — | 저탄력 지역에서 유동성 효과가 크고, 고탄력 지역에서는 "significant but had a smaller effect" (p. 53; Tables 5–6, p. 69–70) | — | — | 탄력성 |

## 5. 저자의 한계 · 내가 보는 "남긴 것"
- **저자 한계**: OLS라 인과 해석 불가(p. 67–68). 지역 창(2005–09 등)이 "somewhat arbitrary"(p. 66). MLS 수기 입력 오류로 윈저화 필요(p. 66).
- **남긴 것(다섯 축)**: `mechanism` — TOM이 소득·연체에 **선행**하는지(시차) 검정하지 않음, 동시 상관만. `data` — months' supply 결과를 "very similar"라고만 하고 미보고(endnote 6, p. 73) → 두 지표의 차이를 볼 수 없음. `group` — 가격 분위는 분포 그림으로만, 분위별 회귀 없음.

## 6. 한국 적용 함의 (1문장)
재등록·철회를 3개월 창으로 이어 붙여 "유효 TOM"을 복원한 규칙(p. 72)은 네이버·직방 매물의 재등록 연결 알고리즘의 **직접 벤치마크**이며, 이 논문이 MLS에서도 리셋 문제를 겪었다는 점이 한국 비MLS 시장에서 더 큰 문제임을 보여준다.

## 7. (선택) 후속 아이디어 → `students/idea_log.md`로
- 3개월 임계값을 한국 데이터에서 분포로 재추정(재등록 간격의 75% 분위).

## 8. 질 평가 (0/1/2)
q1 정의 명확성 2 · q2 선택편의(철회 포함) 1 · q3 내생성 0 · q4 국면 통제 1(지역 창) · q5 이질성 2 · q6 재현성 1(자료 상용, 코드 없음) = **7/12 (중)**

---

### 이 예시에서 눈여겨볼 것
1. 2절 표가 핵심이다. 정의 원문·시작/종료 사건·재등록 처리가 없으면 리뷰 표 4(측정 쟁점 매트릭스)에 넣을 수 없다.
2. 4절은 계수·표준오차·표 번호·쪽수를 분리해 적었다. "효과가 있었다"는 결과가 아니다.
3. `NR`을 두 군데 두었다(철회 매물의 TOM 포함 여부, 품질 통제). 모르면 비워 두는 것이 맞다.
4. 지표가 둘(TOM, months' supply)이라 추출 CSV에는 **두 행**이 된다(`templates/extraction_form.csv` 3·4행).
5. 이 한 편에 약 1.5~2시간이 든다. 28쪽 중 읽어야 할 곳은 초록·자료 절·방법 절·결과 표·결론·부록으로, 문헌고찰 절(II)은 훑기만 한다.
