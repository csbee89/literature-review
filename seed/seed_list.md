# 시드(앵커) 문헌 목록 — 검색식 민감도 점검용 + 후방 스노볼링 출발점

작성 2026-10-06. 판정은 `scripts/verify_citations.py`(sb-paper 스킬, Crossref/OpenAlex) 결과이며 원본 리포트는 `seed_verification_report.md`.
**이 목록은 문헌의 실존만 확인한 것이다.** 각 문헌이 어떤 지표 정의를 썼는지는 전문을 열어 추출 양식에 적어야 한다.
`[미검증]` 항목은 삭제하지 말고 사용자가 원문을 확인한 뒤 결정한다.

용도:
1. Scopus/WoS 검색식 실행 후 **이 목록의 회수율**을 계산한다 (목표 ≥ 90%). 놓친 문헌의 제목·초록 용어를 검색식에 추가한다.
2. Sirmans et al.(2010), Benefield et al.(2014), Han & Strange(2015)의 참고문헌을 전수 검토한다(후방 스노볼링).
3. 각 문헌의 OpenAlex `cited_by`를 훑는다(전방 스노볼링).

## A. 고전·이론·측정 (Crossref 자동 검증 결과)

| # | 판정 | 입력 서지 | DOI |
|---|---|---|---|
| 1 | [미검증] Crossref 미등록(JSTOR 시대). 수동 확인 | Lippman, S. A., & McCall, J. J. (1986). An operational measure of liquidity. American Economic Review, 76(1), 43-55. | 10.2139/ssrn.5417260 |
| 2 | VERIFIED | Haurin, D. (1988). The duration of marketing time of residential housing. AREUEA Journal, 16(4), 396-410. | 10.1111/1540-6229.00463 |
| 3 | VERIFIED | Kluger, B. D., & Miller, N. G. (1990). Measuring residential real estate liquidity. AREUEA Journal, 18(2), 145-159. | 10.1111/1540-6229.00514 |
| 4 | VERIFIED | Forgey, F. A., Rutherford, R. C., & Springer, T. M. (1996). Search and liquidity in single-family housing. Real Estate Economics, 24(3), 273-292. | 10.1111/1540-6229.00691 |
| 5 | VERIFIED | Genesove, D., & Mayer, C. J. (1997). Equity and time to sale in the real estate market. American Economic Review, 87(3), 255-269. | 10.3386/w4861 |
| 6 | VERIFIED | Glower, M., Haurin, D. R., & Hendershott, P. H. (1998). Selling time and selling price: The influence of seller motivation. Real Estate Economics, 26( | 10.1111/1540-6229.00763 |
| 7 | VERIFIED | Taylor, C. R. (1999). Time-on-the-market as a sign of quality. Review of Economic Studies, 66(3), 555-578. | 10.1111/1467-937x.00098 |
| 8 | VERIFIED | Anglin, P. M., Rutherford, R., & Springer, T. M. (2003). The trade-off between the selling price of residential properties and time-on-the-market: The | 10.1023/a:1021526332732 |
| 9 | VERIFIED | Fisher, J., Gatzlaff, D., Geltner, D., & Haurin, D. (2003). Controlling for the impact of variable liquidity in commercial real estate price indices. | 10.1111/1540-6229.00066 |
| 10 | VERIFIED | Merlo, A., & Ortalo-Magné, F. (2004). Bargaining over residential real estate: Evidence from England. Journal of Urban Economics, 56(2), 192-216. | 10.2139/ssrn.306119 |
| 11 | VERIFIED | Goetzmann, W. N., & Peng, L. (2006). Estimating house price indexes in the presence of seller reservation prices. Review of Economics and Statistics, | 10.1162/003465306775565783 |
| 12 | VERIFIED | Lin, Z., & Vandell, K. D. (2007). Illiquidity and pricing biases in the real estate market. Real Estate Economics, 35(3), 291-330. | 10.1111/j.1540-6229.2007.00191.x |
| 13 | VERIFIED | Fisher, J., Geltner, D., & Pollakowski, H. (2007). A quarterly transactions-based index of institutional real estate investment performance and moveme | 10.15396/eres2005_174 |
| 14 | VERIFIED | Johnson, K. H., Benefield, J. D., & Wiley, J. A. (2007). The probability of sale for residential real estate. Journal of Housing Research, 16(2), 131- | 10.1080/10835547.2007.12091978 |
| 15 | VERIFIED | Clayton, J., MacKinnon, G., & Peng, L. (2008). Time variation of liquidity in the private real estate market: An empirical investigation. Journal of R | 10.1080/10835547.2008.12091217 |
| 16 | VERIFIED | Cheng, P., Lin, Z., & Liu, Y. (2008). A model of time-on-market and real estate price under sequential search with recall. Real Estate Economics, 36(4 | 10.1111/j.1540-6229.2008.00231.x |
| 17 | VERIFIED | Levitt, S. D., & Syverson, C. (2008). Market distortions when agents are better informed: The value of information in real estate transactions. Review | 10.3386/w11053 |
| 18 | VERIFIED | Novy-Marx, R. (2009). Hot and cold markets. Real Estate Economics, 37(1), 1-22. | 10.1111/j.1540-6229.2009.00232.x |
| 19 | VERIFIED | Hendel, I., Nevo, A., & Ortalo-Magné, F. (2009). The relative performance of real estate marketing platforms: MLS versus FSBOMadison.com. American Eco | 10.3386/w13360 |
| 20 | VERIFIED | Benefield, J. D., Cain, C. L., & Johnson, K. H. (2011). On the relationship between property price, time-on-market, and photo depictions in a multiple | 10.4108/eai.5-9-2018.2281277 |
| 21 | VERIFIED | Bokhari, S., & Geltner, D. (2011). Loss aversion and anchoring in commercial real estate pricing: Empirical evidence and price index implications. Rea | 10.2139/ssrn.1599382 |
| 22 | VERIFIED | Carrillo, P. E. (2012). An empirical stationary equilibrium search model of the housing market. International Economic Review, 53(1), 203-234. | 10.1111/j.1468-2354.2011.00677.x |
| 23 | VERIFIED(재확인) | Genesove, D., & Han, L. (2012). Search and matching in the housing market. Journal of Urban Economics, 72(1), 31-45. | 10.1016/j.jue.2012.01.002 |
| 24 | VERIFIED | de Wit, E. R., & van der Klaauw, B. (2013). Asymmetric information and list-price reductions in the housing market. Regional Science and Urban Economi | 10.2139/ssrn.1589295 |
| 25 | VERIFIED | de Wit, E. R., Englund, P., & Francke, M. K. (2013). Price and transaction volume in the Dutch housing market. Regional Science and Urban Economics, 4 | 10.2139/ssrn.1589296 |
| 26 | VERIFIED(재확인) | Díaz, A., & Jerez, B. (2013). House prices, sales, and time on the market: A search-theoretic framework. International Economic Review, 54(3), 837-872 | 10.1111/iere.12019 |
| 27 | VERIFIED | Carrillo, P. E. (2013). To sell or not to sell: Measuring the heat of the housing market. Real Estate Economics, 41(2), 310-346. | 10.1111/reec.12003 |
| 28 | VERIFIED | Benefield, J. D., Cain, C. L., & Johnson, K. H. (2014). A review of literature utilizing simultaneous modeling techniques for property price and time | 10.1080/10835547.2014.12090387 |
| 29 | VERIFIED(재확인) | Head, A., Lloyd-Ellis, H., & Sun, H. (2014). Search, liquidity, and the dynamics of house prices and construction. American Economic Review, 104(4), 1 | 10.1257/aer.104.4.1172 |
| 30 | VERIFIED | Ngai, L. R., & Tenreyro, S. (2014). Hot and cold seasons in the housing market. American Economic Review, 104(12), 3991-4026. | 10.1257/aer.104.12.3991 |
| 31 | VERIFIED | Benefield, J. D., & Hardin, W. G. (2015). Does time-on-market measurement matter? Journal of Real Estate Finance and Economics, 50(1), 52-73. | 10.1007/s11146-013-9450-z |
| 32 | VERIFIED | Carrillo, P. E., de Wit, E. R., & Larson, W. (2015). Can tightness in the housing market help predict subsequent home price appreciation? Evidence fro | 10.1111/1540-6229.12082 |
| 33 | [미검증] Handbook 장. Elsevier DOI 수동 확인 | Han, L., & Strange, W. C. (2015). The microstructure of housing markets: Search, bargaining, and brokerage. Handbook of Regional and Urban Economics, | 10.1007/978-3-7908-2864-1 |
| 34 | VERIFIED | Albrecht, J., Gautier, P. A., & Vroman, S. (2016). Directed search in the housing market. Review of Economic Dynamics, 19, 218-231. | 10.2139/ssrn.1535269 |
| 35 | VERIFIED | Anenberg, E. (2016). Information frictions and housing market dynamics. International Economic Review, 57(4), 1449-1479. | 10.2139/ssrn.2192644 |
| 36 | VERIFIED | Han, L., & Strange, W. C. (2016). What is the role of the asking price for a house? Journal of Urban Economics, 93, 115-130. | 10.1016/j.jue.2016.03.008 |
| 37 | VERIFIED | Hedlund, A. (2016). Illiquidity and its discontents: Trading delays and foreclosures in the housing market. Journal of Monetary Economics, 83, 1-13. | 10.2139/ssrn.1932908 |
| 38 | VERIFIED | Anenberg, E., & Laufer, S. (2017). A more timely house price index. Review of Economics and Statistics, 99(4), 722-734. | 10.2139/ssrn.2402394 |
| 39 | VERIFIED | Guren, A. M. (2018). House price momentum and strategic complementarity. Journal of Political Economy, 126(3), 1172-1218. | 10.1086/697207 |
| 40 | VERIFIED | Anundsen, A. K., & Røed Larsen, E. (2018). Testing for micro-efficiency in the housing market. International Economic Review, 59(4), 2133-2162. | 10.1111/iere.12332 |
| 41 | VERIFIED | Gabrovski, M., & Ortego-Marti, V. (2019). The cyclical behavior of the Beveridge curve in the housing market. Journal of Economic Theory, 181, 361-381 | 10.1016/j.jet.2019.03.003 |
| 42 | VERIFIED | Hayunga, D. K., & Pace, R. K. (2019). The impact of TOM on prices in the US housing market. Journal of Real Estate Finance and Economics, 58(3), 335-3 | 10.1007/s11146-018-9657-0 |
| 43 | VERIFIED | Piazzesi, M., Schneider, M., & Stroebel, J. (2020). Segmented housing search. American Economic Review, 110(3), 720-759. | 10.3386/w20823 |
| 44 | VERIFIED(재확인) | Garriga, C., & Hedlund, A. (2020). Mortgage debt, consumption, and illiquid housing markets in the Great Recession. American Economic Review, 110(6), | 10.1257/aer.20170772 |
| 45 | VERIFIED | van Dijk, D. W., Geltner, D. M., & van de Minne, A. M. (2022). The dynamics of liquidity in commercial property markets: Revisiting supply and demand | 10.1007/s11146-020-09782-5 |
| 46 | VERIFIED | Anenberg, E., & Ringo, D. (2024). Volatility in home sales and prices: Supply or demand? Journal of Urban Economics, 139, 103610. | 10.1016/j.jue.2023.103610 |

> #5 Genesove & Mayer(1997)와 #19 Hendel et al.(2009) 등 일부는 NBER 워킹페이퍼 DOI로 매칭됐다. 게재본 DOI는 추출 시 교체한다.
> Berkovec & Goodman(1996)은 연구계획서 참고문헌의 제목이 Crossref 등록 제목("Turnover as a Measure of Demand for Existing Homes", Real Estate Economics 24(4), doi:10.1111/1540-6229.00698)과 다르다. 수정 필요.

## B. 2026-10-06 스코핑 스캔에서 확인된 최근·관련 문헌 (Crossref 직접 조회, 모두 VERIFIED)

| 연도 | 저자 | 제목 | 학술지 | DOI | 왜 중요한가 |
|---|---|---|---|---|---|
| 2002 | Knight, J. R. | Listing price, time on market, and ultimate selling price: Causes and effects of listing price changes | Real Estate Economics | 10.1111/1540-6229.00038 | B층 호가 변경 고전 |
| 2006 | Anglin, P. M. | Value and liquidity under changing market conditions | Journal of Housing Economics | 10.1016/j.jhe.2006.10.003 | 국면 의존성 |
| 2010 | Sirmans, MacDonald & Macpherson | A meta-analysis of selling price and time-on-the-market | Journal of Housing Research | 10.1080/10835547.2010.12092027 | **기존 리뷰(메타분석)** — 차별점 근거 |
| 2012 | Miller & Sklarz | Integrating real estate market conditions into home price forecasting systems | Journal of Housing Research | 10.1080/10835547.2012.12092059 | 계획서의 "3분기 선행" 출처. 쪽수·지표 정의 확인 필요 |
| 2013 | An, Cheng & Lin | How do market conditions impact price-TOM relationship? Evidence from REO sales | Journal of Housing Economics | 10.1016/j.jhe.2013.07.003 | 국면별 이질성 |
| 2013 | Beracha & Wintoki | Forecasting residential real estate price changes from online search activity | Journal of Real Estate Research | 10.1080/10835547.2013.12091364 | D층 검색량 지표 |
| 2014 | Filippova & Rehm | Market conditions, marketing time, and house prices | Journal of Housing Research | 10.1080/10835547.2013.12092086 | 국면 조건 |
| 2017 | van Dijk & Francke | Internet search behavior, liquidity and prices in the housing market | Real Estate Economics | 10.1111/1540-6229.12187 | D층·선행성 |
| 2019 | Liu & van der Vlist | Listing strategies and housing busts: Cutting loss or cutting list price? | Journal of Housing Economics | 10.1016/j.jhe.2018.09.006 | B층 침체기 호가 전략 |
| 2019 | Chernobai & Hossain | Liquidity imbalance in the residential real estate market | Journal of Housing Research | 10.1080/10527001.2020.1776513 | C층 |
| 2020 | Famiglietti, Garriga & Hedlund | The geography of housing market liquidity during the Great Recession | Federal Reserve Bank of St. Louis Review | 10.20955/r.102.51-77 | C층 지역 이질성 |
| 2020 | Suzuki & Asami | Shrinking housing market, long-term vacancy, and withdrawal from housing market | Asia-Pacific Journal of Regional Science | 10.1007/s41685-020-00159-3 | 철회(withdrawal) 지표, 일본(비MLS) |
| 2021 | Irwin & Livy | Price and liquidity dynamics for single and multi-family homes during housing market shocks | J. Real Estate Finance & Economics | 10.1007/s11146-021-09846-0 | 충격기 유형별 이질성 |
| 2022 | Ben-Shahar & Golan | Price dispersion and time-on-market in the housing market | Journal of Housing Economics | 10.1016/j.jhe.2022.101875 | B층 가격분산 지표 |
| 2022 | Gárate Alvarez & Pennington-Cross | Short-term property rental platforms and the housing market: House prices and liquidity | Journal of Housing Research | 10.1080/10527001.2022.2033389 | STR–유동성 (연구실 축 2와 연결) |
| 2024 | van Dijk, D. W. | Local constant-quality housing market liquidity indices | Regional Science and Urban Economics | 10.1016/j.regsciurbeco.2024.103997 | C층 핵심. 계획서 인용 |
| 2024 | Suzuki, Arai & Yamato | Capturing low demand through long time-on-market: Functional obsolescence and owner resignation among old rental housing | Housing, Theory and Society | 10.1080/14036096.2024.2374764 | 일본 임대, 비MLS |
| 2025 | Hayunga & Swymer | Relisting, agent switching, and sale outcomes in the housing market | Journal of Housing Economics | 10.1016/j.jhe.2025.102086 | **재등록 처리** — RQ3 직결 |
| 2025 | Lin, Seiler & Siebert | Selling price, time on the market, and contractual contingencies | Journal of Housing Economics | 10.1016/j.jhe.2025.102062 | A·B층 최신 |
| 2025 | Pilat & Leishman | Strategic underpricing and time-on-market: Evidence from South Australia's housing market | Int. J. Housing Markets and Analysis | 10.1108/ijhma-05-2025-0126 | B층, 호주 |
| 2026 | von Wehrt & Falkenbach | Liquidity in housing markets: The effect of news sentiment on time on market | Journal of European Real Estate Research | 10.1108/jerer-12-2025-0098 | D층 뉴스 심리 |
| 2026 | Liu, Shakib, Miller & Habib | Understanding housing market dynamics through a joint model of time-on-market duration and listing outcome | Journal of Urban Planning and Development | 10.1061/jupddm.upeng-5857 | 경쟁위험(매각 vs 철회) 결합모형 |
| 2026 | Kang & Lee | Frozen markets, falling prices: Illiquidity and bounded price discovery in U.S. neighborhood housing markets | J. Real Estate Finance & Economics | 10.1007/s11146-026-10080-9 | **거래절벽·가격발견 마비** — 계획서 §1 논리와 직결 |

## C. 국내 문헌 (Crossref에 로마자 서지로 등록된 것만. 저자 한글 표기는 원문 확인 필요)

| 연도 | 저자(로마자) | 제목(영문 등록) | 학술지 | DOI |
|---|---|---|---|---|
| 2016 | Lee, Young-Hoon; Kim, Jae-Jun | Influence of liquidity on the housing market before and after macroeconomic fluctuations | 한국산학기술학회논문지 17(5) | 10.5762/kais.2016.17.5.116 |
| 2018 | Lee, Youngsoo; Lee, Jongpil | Causality and predictability of price-volume in housing market: Evidence from Seoul and Busan | SH 도시연구와 인사이트 8(3) | 10.26700/shuri.2018.12.8.3.51 |
| 2019 | Ko, Jinsoo; Choi, Seong-Ho; Noh, Seungchul | Factors affecting the days on market of residential real estate in Seoul | 주택연구 27(1) | 10.24957/hsr.2019.27.1.05 |
| 2019 | Yang, Jae-Yeong; Ko, JinSoo | The effect of apartment housing characteristics on the days on market (DOM) | 도시정책연구 10(3) | 10.21447/jup.2019.10.3.101 |
| 2026 | Oh, Yun Kyung | A study on the typology of the Busan housing market considering price differentiation and transaction liquidity | 부동산학보 44(3) | 10.37407/kres.2026.44.3.315 |

국문 본검색은 KCI OpenAPI 키 발급 후 `protocol/02_search_strings.md` §6의 동의어로 수행한다. 위 5편은 그 검색의 **회수율 점검용**이다.

## D. 회색문헌·워킹페이퍼 (실존 확인 방법 다름)

| 항목 | 상태 |
|---|---|
| 권건우(2025). 부동산 거래활동지표 기반 시장 분석과 활용 방안. 국토연구원 | 계획서 인용. 국토연구원 발간물 DB에서 확인 필요 |
| 문윤상(2024). 주택 양도소득세의 경제적 효과. KDI FOCUS | 계획서 인용. KDI 확인 필요 |
| Anenberg & Ringo(2014). The lock-in effect of rising mortgage rates. FEDS Notes | 계획서 인용. Fed 사이트 확인 필요 |
| Zhang, A. L. Liquidity in residential real estate markets (working paper) | 웹 검색에서 확인(저자 홈페이지 PDF). 게재 여부 확인 필요 |
| LH 토지주택연구원. 매물 소진기간 집계 (2022 보도: 상반기 17.9주) | 경향신문 2022-10-25 보도. **원보고서 확인 필요** |
