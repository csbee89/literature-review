# [예시] 문헌 1쪽 정리 — 종합 대상 p115 (한국 논문, 거래량–가격 선행성)

**작성** Claude(AI 초안) · **작성일** 2026-10-13 · **검증** 이원석이 W1에 원문과 한 줄씩 대조 후 `checker_note`에 서명 · **원문** `papers/p115.pdf` (오픈액세스, CC BY-NC-ND, PDF 20쪽: 본문 pp. 53–69, 부록 pp. 70–71, 국문초록 p. 72)
**이 예시의 용도**: 한국 논문 주간(W2~W5)의 기준선. 한국 논문 대부분이 이 논문처럼 "거래량과 가격의 선후행"을 다루므로, 이 정리를 그대로 따라 하면 된다. 영문 논문의 기준선은 `example_Famiglietti2020.md`.

---

## 0. 서지와 분류 코드
- **저자(전원)**: Ma, Seungryul (마승렬)
- **연도**: 2021
- **제목**: Frequency domain analysis to detect common cycle in housing price and trading volume (빈도영역 분석법을 통한 주택가격과 거래량의 공통 사이클 분석)
- **학술지 권(호):쪽**: 주택도시금융연구 (Journal of Housing and Urban Finance), 6(2): 53–73
- **DOI**: 10.38100/jhuf.2021.6.2.53
- **문헌 유형**: 동료심사 학술지 (접수 2021.12.11, 게재확정 2021.12.20, p. 69)
- **실존 확인**: Y (DOI 열어 봄)
- **분류 코드(배정표 초기값 → 확인 결과)**: `stage` S4 체결 → **S4 맞음** / `function` F3 선행성·관계 → **F3 맞음** / `regime` 비MLS → **맞음**(한국, 매물 단위 자료 없음, 집계 거래량만 사용)

## 1. 한 줄 요약
한국부동산원 월별 아파트 가격지수와 거래량(2007.01–2018.10, 4개 권역)으로 스펙트럼 분석과 VAR를 함께 써서, 두 시계열이 20(또는 24)개월·48개월 공통 주기를 가지며 그 주기에서 거래량이 가격상승률보다 약간 앞선다고 보였다.

## 2. 지표 정의 (원문 인용, 쪽수)

| 지표명 | 층 | 역할 | 정의 원문 | 단위 | 시작 사건 | 종료 사건 | 미거래·철회 처리 | 재등록 처리 |
|---|---|---|---|---|---|---|---|---|
| 12개월 누적 아파트 거래량 (VolN) | C | VAR·교차스펙트럼의 한쪽 변수(설명·피설명 모두) | "as the proxy variable of trading volume, we used the twelvemonth accumulated monthly apartment trading volume" (p. 57) | 건수 → HP 필터로 추세 제거 후 표준화한 무단위 값(p. 57, 각주 3) | NA | NA | NA | NA |

- **가공 절차**: 추세 제거 "eleminating the trends in these two variables using Hodrick-Prescott filtering method" (p. 57) → 표준화 "subtracting mean value from the raw value and then dividing it by standard deviation" (각주 3, p. 57). **HP 필터의 λ 값은 `NR`**.
- **비교 대상 변수(지표 아님)**: 가격상승률 gN = "the year-on-year increase rates of apartment price index" (p. 57). 같은 방식으로 HP 필터·표준화.
- **자료원**: "monthly time series data of apartment price index and apartment trading volume from the database of Korea Real Estate Board" (p. 57). 거래량이 **신고 기준인지 등기 기준인지 `NR`**. 가격지수가 **조사(동향) 지수인지 실거래가격지수인지 `NR`**.
- **주택유형**: 아파트만. "we used apartment data as the proxy of house data considering it's absolute weight in the trading volume" (각주 2, p. 57).
- **집계 방식**: 12개월 이동 합계(`aggregation` = rolling-sum). 품질 통제 `none`. 중복 등재 `NA`.

## 3. 자료와 방법
- **국가·지역·기간**: 한국, 월별 2007.01–2018.10 (p. 57). 4개 권역: "① Total (Whole country), ② Seoul Metropolitan (Seoul, Incheon, Gyunggi), ③ 5 Big Cities (Busan, Daegu, Gwangju, Daejeon, Ulsan), ④ Non Metropolitan" (p. 57). **MLS**: N
- **N**: 월별 관측 약 142개월 × 4권역 (기간에서 계산한 값. 원문에 N 명시 없음 → `NR`로 적고 비고에 계산값)
- **방법 가족**: `spectral`(periodogram, 교차스펙트럼의 squared coherence·phase, 조화분석) + `VAR-Granger`. VAR 시차: Total VAR(2), SMetro VAR(4), 5Cities·NMetro VAR(3), 시차 선택 기준에 따름 (Table 7 주 1, p. 64)
- **내생성 처리**: `none` (축약형 VAR·그랜저, 구조 식별 없음)
- **이질성 축**: `region` (4권역)

## 4. 결과 (방향·크기·쪽수 분리)

| 지표 → 결과변수 | 방향 | 크기(원문) | 선행 시차 | 검정 | 국면·집단별 차이 |
|---|---|---|---|---|---|
| 공통 주기 존재 | — | "the idenfied common cycles embedded in gN and VolN were 20 month and 48 month in Total, Smetro, and Nmetro area. But, the idenfied common cycles in 5Cities were 24 month and 48 month." (p. 61; Table 3) | — | periodogram | 5Cities만 24개월 |
| 거래량 → 가격상승률 (주기 영역) | 거래량 선행 | 위상(phase) 대부분 작은 음수: Total 20개월 −0.3, 48개월 −0.2; SMetro −0.3, 0.0; 5Cities −0.2, −0.5 (Table 4, p. 62). 결맞음(squared coherence) "0.58-0.87" (p. 61) | **Total 48개월 주기 약 3개월, 20개월 주기 약 1.9개월**: "precedes about 3 months (=(–0.2/π)×48)", "about 1.9 months (=–0.3/π)×20)" (p. 61) | cross-spectral | 비수도권: "could not say that the movement of trading volume precedes that of housing price change rates" (p. 67) |
| 거래량 ↔ 가격상승률 (시간 영역) | 양방향 | 그랜저 F검정 p값(Table 2, p. 60). **VolN↛gN 기각(5%)**: Total 시차 2·3만(0.0291, 0.0493), SMetro 시차 2–5, 5Cities 시차 2만(0.0007), NMetro 시차 2·3만. **gN↛VolN 기각**: Total·5Cities·NMetro는 시차 2–6 전부, SMetro는 시차 4·5만 | 짧은 시차에서만 거래량→가격 | Granger | 저자: "there are two-way causation between the time series of gN and VolN regardless of regions" (p. 60) |
| 단기에서 선후행 역전 가능성 | — | "the lead-lag relationship between the time series of gN and VolN could be reversed as time goes on in the aspect of short-term movements" (p. 63) | — | VAR | — |
| 예측(부가 결과) | — | 2019년 이후 거래량 감소·가격상승률 둔화, 2020년 말 이후 재상승 전환 예측 (p. 65, p. 68) | — | harmonic + VAR 예측 | 수도권 하락 속도가 전국보다 빠름 (p. 66) |

### 원문 대조에서 발견한 것 (checker가 확인할 곳)
1. **저자 문장과 표의 차이**: 저자는 "regardless of regions" 양방향이라고 썼지만(p. 60), Table 2를 보면 가격→거래량은 대부분 시차에서 유의하고 거래량→가격은 짧은 시차(2–3개월)에서만 유의하다. **결과 칸에는 표를 적고, 저자 문장은 따옴표로 따로 적는다.** 리뷰 표 4에서 "거래량 선행"으로 셀 것인지가 이 차이에 달려 있다.
2. **표의 지역 이름 오기**: Table 4(p. 62)에 "SMetro"가 두 번 나온다. 두 번째 행(20개월 −0.5/0.77, 48개월 −0.2/0.87)은 순서상 NMetro로 보인다. 부록 2(p. 71)에서도 패널 이름 "SMetro"가 두 번 나오는데, 여기서는 셋째 패널이 5Cities로 보인다. `notes`에 "Table 4 둘째 SMetro = NMetro 추정, 부록 2 셋째 패널 = 5Cities 추정"이라고 남긴다.
3. **위상→개월 환산식 `[확인 필요]`**: 저자는 위상÷π×주기로 환산했다(p. 61). 위상을 라디안으로 쓸 때 흔히 쓰는 식은 위상÷2π×주기이며, 그러면 약 1.5개월·0.95개월이 된다. 위상의 단위가 원문에 없어 어느 쪽이 맞는지 판단할 수 없다. `lead_lag`에는 **저자 값(약 3개월·1.9개월)을 그대로 적고**, `notes`에 이 점을 적어 교수 판정으로 넘긴다.
4. **위상의 부호 규약**: 각주 6이 "Phase indicates the timing of peaks in the time series [x] relative to peaks in the time series [y]"라고 하는데 PDF에서 x·y 기호가 깨져 어느 변수가 기준인지 읽을 수 없다(p. 61). 저자의 해석 문장을 따른다.

## 5. 저자 한계 · 남긴 것
- **저자 한계**: 자료가 2018.10까지라 "it is necessary to conduct the analysis periodically with updated data" (p. 69). 금리 등 다른 변수를 함께 보는 분석이 필요하다 (p. 69).
- **남긴 것(다섯 축)**: `data` — 거래량이 신고·등기 중 어느 기준인지, 가격지수가 어느 지수인지 밝히지 않아 측정 쟁점 표에서 비교가 어렵다. `mechanism` — 거래량이 왜 앞서는지(매도자 손실회피, 계약–신고 시차 등) 검정하지 않았다. `group` — 아파트만, 가격대·규모별 차이 없음.

## 6. 한국 적용 함의 (1문장)
매물 시간(DOM) 자료가 없는 한국에서는 이런 집계 거래량이 매칭 단계(S3)의 대리 지표로 쓰여 왔는데, 12개월 누적·HP 필터처럼 가공을 거치면 선행 길이가 몇 개월씩 달라질 수 있으므로, 조기경보 지표를 만들 때 가공 규칙(누적 창, 추세 제거, 신고·등기 기준)을 먼저 고정해야 한다.

## 7. (선택) 후속 아이디어 → `students/idea_log.md`로
- 같은 자료를 신고 기준과 등기 기준으로 각각 돌려 선행 길이가 얼마나 달라지는지 비교.

## 8. 질 평가 (0/1/2, 프로토콜 §9)
q1 정의 명확성 **1**(조작적 정의는 있으나 자료 기준·HP λ 미기재) · q2 선택편의 **NA**(집계 지표라 철회·미거래 매물 문제가 없음) · q3 내생성 **0** · q4 국면 통제 **0**(국면 구분 없음, 예측에서만 서술) · q5 이질성 **1**(권역 4개) · q6 재현성 **1**(공개 자료, 코드 없음) = **3/10 (하)**. NA 항목은 분모에서 뺀다(코드북 §F 규칙).

## 9. 추출 CSV로 옮기면 (1행)
`study_id`=Ma2021 · `pid`=p115 · `stage`=S4 · `function`=F3 · `regime`=NML · `stage_changed`=N · `country`=KR · `region_scale`=national+metro · `market_type`=owner-sale · `housing_type`=condo-apt · `period_start`=2007 · `period_end`=2018 · `market_phase`=NR · `mls_market`=N · `indicator_name`=twelvemonth accumulated apartment trading volume · `indicator_tier`=C · `indicator_role`=DV;IV(VAR) · `definition_verbatim`="the twelvemonth accumulated monthly apartment trading volume" (p. 57) · `unit`=standardized(HP-detrended) · `start_event`=NA · `end_event`=NA · `censoring`=NA · `relisting_handling`=NA · `duplicate_handling`=NA · `aggregation`=rolling-sum(12m) · `quality_adjustment`=none · `data_source`=NR(KREB; 신고/등기 미기재) · `data_source_name`=Korea Real Estate Board · `n_obs`=NR · `method_family`=spectral;VAR-Granger · `endogeneity_treatment`=none · `heterogeneity_dims`=region · `outcome_var`=price index(YoY growth) · `effect_direction`=+ (co-movement), volume leads · `lead_lag`=leads price by ~3 months (48m cycle), ~1.9 months (20m cycle), author's conversion · `lead_test`=cross-spectral;Granger · `phase_dependence`=NR

---

### 이 예시에서 눈여겨볼 것
1. **한국 논문에서 가장 자주 비는 칸**은 자료 기준(신고·등기, 조사지수·실거래지수)이다. 원문에 없으면 `NR`이고, 그 `NR` 자체가 리뷰의 결과(측정 쟁점 표)가 된다.
2. **결과는 표에서 읽는다.** 저자 결론 문장과 표가 어긋나면 둘 다 적는다(4절 "원문 대조" 1번).
3. **선행 길이는 숫자와 단위로** 적는다. "거래량이 선행한다"만 쓰면 표 4에 넣을 수 없다.
4. 이 논문은 질 평가가 낮지만 **빼지 않는다.** 질 평가는 민감도 분석에만 쓴다.
5. 21쪽 논문에 약 1.5시간. 수식 절(pp. 55–56)은 훑고, 자료 절(p. 57)·표 1–4(pp. 60–62)·결론(pp. 68–69)을 꼼꼼히 본다.
