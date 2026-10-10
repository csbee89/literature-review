# 규칙 선별의 정의 (재현용)

모든 정규식은 `scripts/merge2.py`(단계 A), `scripts/stageB.py`(단계 B)에 있다. 아래는 사람이 읽을 수 있게 옮긴 것이다.

## 단계 A (통과 조건: 모두 충족)
1. **주택 맥락어** (제목 또는 초록): hous*, home*, residential, dwelling*, apartment*, condo*, real estate, realt*, propert*, MLS, multiple listing, listing*, seller*, homeowner*, mortgage, land market
2. **유동성 관련어** (넓게): time on (the) market, TOM, days on market, DOM, marketing time/duration/period, selling time, time to sale, listing duration, probability of sale, withdraw*, relist*, list(ing) price, asking price, price cut/reduction/revision/dispersion, sale-to-list, overpricing, reservation price, liquidity, illiquid*, tightness, hot/cold market, months of supply/inventory, absorption rate, inventory, sales-to-listings, turnover, transaction/trading/sales volume, vacancy, search, matching, bargaining, broker*, agent*, auction, foreclosure, seller motivation, anchoring, loss aversion
3. **노이즈 제외** (제목에 주택 단어가 없을 때만 적용): stock/bond/REIT/interbank/funding liquidity/monetary/crypto/options/futures/labor market/medical/materials science 등
4. 1986년 이후

## 단계 B (통과 조건: 강한 지표어 1개 이상)
time on (the) market, TOM, days on market, DOM, marketing time/duration/period/span, selling time/duration, time to sale/sell, listing duration, probability/likelihood of sale, withdrawal of listing, relist*, list(ing) price change/reduction/cut/revision/strategy/setting/premium, asking price, sale-to-list, list-to-sale, over/underpricing, price dispersion, housing/property/real estate (…) liquidity, illiquid*, market tightness, hot and/or cold market, months' supply/inventory, absorption rate, for-sale/unsold/housing inventory, sales-to-listings, housing/home turnover, transaction/sales/trading volume, housing search index/activity/duration, search index/volume/activity (+주택어), vacancy duration

## 복구 패스 (B′)
- D층 어휘: google, internet, online search/interest/listing/attention, search volume/activity/index/queries, clicks, page views, web-scraping, listing(s) data, zillow/redfin/funda/rightmove, nowcast, real-time house price, leading/early indicator, turning point, sell-to-list, days-to-sell, time-to-contract/close, stale listing, listing/inventory age, for-sale/housing inventory, new listings
- 하이픈 변형과 "제목에 주택어 없음" 사례: 단계 A의 맥락어 요건을 풀고 강한 지표어만으로 재검색 (169건 재검토 → 36편 추가)

## 판독 코드
| 코드 | 의미 |
|---|---|
| I | 포함 (지표가 종속변수·핵심 설명변수·구축 대상) |
| I? | 포함 후보 — 초록만으로 지표 측정 여부 불확실, 전문 확인 후 확정 |
| E1 | 범위 밖 유동성 (증권·통화·가구 제약·자금) 또는 비주택 주제 |
| E2 | 유동성 지표가 측정되지 않음 (가격·가치평가·선호 등) |
| E3 | 대상 시장 범위 밖 (임대·상업용·토지·분양·강제매각 경매) |
| E4 | 문헌 유형 범위 밖 (워킹페이퍼·학위논문·학술대회·연준 리뷰·북챕터·서평) |
| V | 프리프린트/학술지명 누락 — 게재본 확인 필요 (→ I 또는 E4) |
| M | 보류 — 판정 근거 부족 (→ 게재본·초록 확인 후 I/E) |
| R | 선행 리뷰 (코퍼스 제외, 서론에서 인용) |
| DUP | 다른 레코드와 동일 논문 |

## 층(layer)과 작업량 구분
- **core**: 지표 자체가 연구 대상(정의·측정·분포·시장 지표·호가 전략·탐색 지표·선행성·이론) → 완전 추출(2시간)
- **peripheral**: 특정 요인 X(어메니티·재난·중개사 특성·기술·정책)의 효과를 보기 위해 TOM·가격을 결과변수로 쓴 연구 → 경량 추출(30분: 서지 + 지표 정의 표(2절)만). RQ3(정의 변형) 자료로 쓴다
- **theory**: 탐색·매칭·경매 이론 → 완전 추출(이론 절 전용 양식), 박사 담당
