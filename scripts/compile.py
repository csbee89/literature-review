import csv,re,html,json
rows=list(csv.DictReader(open("screened.csv",encoding="utf-8")))
res={r["rid"]:r for r in csv.DictReader(open("resolved.csv",encoding="utf-8"))}
# V/M -> final mapping (rid: (decision, tier, note))
VM={
"R794":("I","C","expectation volatility liquidity AppliedEcon2015"),"R795":("I","B","listing price strategy negotiation experiment JEP2016"),"R806":("I","B","dynamic static asking prices Sydney EconRecord2016"),
"R807":("I","A","intermediation characteristics time to sale KR 2017"),"R808":("I","B/C","price concessions high-low priced Taiwan QFE2017"),"R812":("I","C","illiquidity residential AppliedEcon2016"),
"R837":("I","A","TOM credit conditions Italy BER2021"),"R775":("I","A","showing appointment technology JREPE2012"),"R459":("I","A","pricing TOM UK city JRER2009"),"R472":("I","T","search bargaining brokers model REE1992"),
"R070":("I","T","price dispersion stickiness competitive search EconTheory2025"),"R122":("I","A/D","VR property sales platform ISR2025"),"R175":("I","B","ambiguous low asking price signals buyer behavior"),"R183":("I","B","ambiguous price signals negotiation advantage"),
"R252":("I","T","search-matching model appraisal JERER2015"),"R312":("I","T","reservation price divergence liquidity JMSE2018"),"R361":("I","T","volatility liquidity model JRER2018"),"R631":("I","A/D","observational learning home viewings ManSci2026"),
"R157":("I?","C","hurricanes short-run housing markets (full text to confirm indicator)"),"R180":("I?","A","urban disruptions SF market dynamics (full text)"),"R184":("I?","C","tariffs housing outcomes (full text)"),"R185":("I?","A/C","economic shocks Shelby County (full text)"),
"R197":("I?","B/C","reference price policy resale Shenzhen (full text)"),"R221":("I?","C","COVID lockdown Hangzhou (full text)"),"R279":("I?","C","second home trading patterns (full text)"),"R323":("I?","A","AI listing language outcomes JPIF2026 (full text)"),
"R401":("I?","A","distressed sales efficiency Lagos low-tier (full text)"),"R556":("I?","A","ethnicity buyers sellers agents (full text)"),"R565":("I?","A","Surfside collapse market dynamics (full text)"),"R566":("I?","A","online agencies impact (full text)"),
"R567":("I?","A/B","MLS data sharing suspension (full text)"),"R690":("I?","A","agent bankruptcy performance (full text)"),"R729":("I?","A","cladding crisis reaction (full text)"),
"R041":("E4","","Brookings-Wharton volume"),"R063":("E3","","forced-sale auction low-tier"),"R089":("E3","","judicial auction"),"R113":("E2","",""),"R149":("E2","",""),"R178":("E3","","new-build unsold inventory"),"R181":("E2","",""),"R193":("E3","","presale primary market"),"R257":("E2","",""),"R539":("E2","",""),"R574":("E2","",""),
"R603":("DUP","","Anenberg Laufer REStat2017 via anchor"),"R604":("E4","","FEDS WP"),"R606":("E4","","SSRN"),"R610":("E4","","SSRN"),"R611":("DUP","","Andersen AER2022 via add"),"R615":("DUP","","Buchak JPE2026 via add"),"R616":("E4","",""),"R617":("E4","",""),"R619":("E4","",""),"R621":("E1","","eBay"),"R623":("E4","",""),"R624":("E4","",""),"R625":("DUP","","Lin2025"),"R628":("DUP","","REE2025 R571"),"R630":("E4","",""),"R633":("E4","",""),
"R737":("E4","","no journal version found"),"R739":("DUP","","Pryce Gibb REE2006 via add"),"R740":("E4","",""),"R744":("E4","",""),"R745":("DUP","","R661"),"R746":("DUP","","R354"),"R747":("E4","",""),"R748":("E4","",""),"R749":("DUP","","Albrecht RED2016 via add"),"R752":("DUP","","R717"),"R753":("E4","",""),"R755":("DUP","","Carrillo IER2012 via add"),"R760":("DUP","","R718"),"R762":("E4","",""),"R764":("DUP","","Property Management 2006 via add"),"R765":("E4","",""),"R766":("DUP","","Hedlund JME2016 via add"),"R767":("E4","",""),"R770":("E4","",""),"R771":("DUP","","R527 E2"),"R772":("DUP","","R528"),"R773":("E1","",""),"R774":("DUP","","IJHMA2010 via add"),"R776":("E4","",""),"R777":("E4","",""),"R778":("E4","",""),"R779":("E4","",""),"R784":("E4","",""),"R785":("DUP","","R543"),"R787":("DUP","","Haurin JHE2013"),"R788":("DUP","","R361"),"R789":("E4","",""),"R791":("E4","",""),"R793":("DUP","","R334"),"R798":("E4","",""),"R799":("E4","",""),"R804":("E4","",""),"R810":("E4","",""),"R811":("E4","",""),"R813":("E4","",""),"R814":("E4","",""),"R815":("DUP","","R226 rental E3"),"R816":("DUP","","Kang Gardner JRER1989 via add"),"R817":("E4","",""),"R818":("E4","",""),"R823":("E4","",""),"R830":("E4","",""),"R831":("E4","","Zhang WP"),"R832":("DUP","","Gargano JF2023 via add"),"R835":("E4","",""),"R838":("E4","",""),
"R291":("DUP","","R? BenShahar JHE2022 journal record"),"R293":("DUP","","Hayunga JHE2025"),"R419":("DUP","","Glower REE1998"),"R647":("I","A","Genesove Mayer AER1997"),"R126":("I","A","Anenberg IER2016"),
}
DOIFIX={"R647":"10.1257/aer.87.3.255","R126":"10.1111/iere.12210","R011":"","R234":"","R346":"10.1080/10835547.2010.12091669","R794":"10.1080/00036846.2015.1023943","R795":"10.1016/j.joep.2015.11.001","R806":"10.1111/1475-4932.12242","R807":"10.22423/kreus.2017.10.1.189","R808":"10.3934/qfe.2017.1.94","R812":"10.1080/00036846.2016.1189506","R837":"10.1111/boer.12284","R775":"10.1080/10835547.2012.12091701","R459":"10.1080/10835547.2009.12091239","R472":"10.1111/1540-6229.00595","R070":"10.1007/s00199-025-01659-z","R122":"10.1287/isre.2021.9138","R175":"10.1108/ijhma-10-2025-0231","R183":"10.1108/ijhma-01-2026-0009","R252":"10.1108/jerer-09-2014-0035","R312":"10.3724/sp.j.1383.303008","R361":"10.1080/10835547.2018.12091511","R631":"10.1287/mnsc.2023.00917","R157":"10.1108/ijhma-02-2022-0024","R180":"10.1108/ijhma-04-2026-0122","R184":"10.1108/ijhma-01-2026-0014","R185":"10.1108/ijhma-04-2026-0100","R197":"10.3846/ijspm.2026.25135","R221":"10.1016/j.asieco.2022.101544","R279":"10.1007/s10901-023-10047-9","R323":"10.1108/jpif-01-2026-0008","R401":"10.4314/lje.v7i1.3","R556":"10.1111/1540-6229.12410","R565":"10.1111/1540-6229.70025","R566":"10.1111/1540-6229.70023","R567":"10.1111/1540-6229.12524","R690":"10.1007/s11146-024-09984-1","R729":"10.1177/00420980221110785"}
# tier from note for I rows
def tier_of(note):
    m=re.match(r"\s*([ABCDT](/[ABCDT])?)\b",note or "")
    if m: return m.group(1)
    if re.search(r"theory",note or "",re.I): return "T"
    return "?"
peri=re.compile(r"flood|school|crime|EPC|energy|HOA|historic|film|subdivision|names|lockbox|estate sales|water quality|VR|virtual|technology|agent|broker|gender|ethnic|bonus|commission|limited service|relocation|cash discount|contingenc|concession|hurricane|COVID|lockdown|tariff|shock|disruption|cladding|Surfside|police|nursing|rental externality|stamp duty|tax|MRT|noise|design features|sustainab|green|solar|AI listing|photo|appointment|amenity|uniqueness|quality TOM|HOA|marketability|sex offender|crisis|TRA97|salesperson|intermediation|collaboration|bankruptcy|visits|viewings|disaster|MLS data|online agencies|second home|high-rise|film|Save Our|Megan|EIFS|off-dollar|range pricing|estate|foreclos|vacant|bank|REO|distressed|forced",re.I)
inc=[]
for r in rows:
    d,n=r["decision"],r["note"]
    if r["rid"] in VM: d,t,n2=VM[r["rid"]]; n=n2 or n
    else: t=tier_of(n)
    if d not in ("I","I?"): continue
    doi=DOIFIX.get(r["rid"],r["doi"] or "")
    if not doi and r["rid"] in res and res[r["rid"]].get("cr_score") and float(res[r["rid"]]["cr_score"])>=0.95: doi=res[r["rid"]]["cr_doi"]
    TFIX={"R200":"Housing price, trading volume and time on market [title garbled in source; verify in IRER 2011]"}
    inc.append(dict(rid=r["rid"],doi=doi,title=TFIX.get(r["rid"],html.unescape(r["title"])),year=r["year"],venue=r["venue"],authors=r["authors"],tier=t,status=d,note=n,provenance=r["sources"]+"|"+r["blocks"]))
ADD=[ # (title,year,venue,doi,tier,note,provenance)
("Reference Dependence in the Housing Market",2022,"American Economic Review","10.1257/aer.20191766","B","listing decisions reference points (journal version of SSRN R611)","resolver"),
("Selling Price and Marketing Time in the Residential Real Estate Market",1989,"Journal of Real Estate Research","10.1080/10835547.1989.12090570","A","Kang Gardner 1989","resolver"),
("Submarket Dynamics of Time to Sale",2006,"Real Estate Economics","10.1111/j.1540-6229.2006.00171.x","A","Pryce Gibb 2006","resolver"),
("Offer price, transaction price and time-on-market",2006,"Property Management","10.1108/02637470610671631","A/B","","resolver"),
("List price and sale price variation across the housing market cycle",2010,"International Journal of Housing Markets and Analysis","10.1108/17538271011049731","B","","resolver"),
("Market Distortions When Agents Are Better Informed: The Value of Information in Real Estate Transactions",2008,"Review of Economics and Statistics","10.1162/rest.90.4.599","A","agent-owned TOM price","anchor"),
("The Relative Performance of Real Estate Marketing Platforms: MLS versus FSBOMadison.com",2009,"American Economic Review","10.1257/aer.99.5.1878","A","FSBO vs MLS TOM","anchor"),
("Conflicts between principals and agents: evidence from residential brokerage",2005,"Journal of Financial Economics","10.1016/j.jfineco.2004.06.006","A","agent-owned TOM","anchor"),
("Bargaining over residential real estate: evidence from England",2004,"Journal of Urban Economics","10.1016/j.jue.2004.05.004","B","list price changes bargaining","anchor"),
("Time-on-the-Market as a Sign of Quality",1999,"Review of Economic Studies","10.1111/1467-937x.00098","T","TOM signal theory","anchor"),
("Illiquidity and its discontents: Trading delays and foreclosures in the housing market",2016,"Journal of Monetary Economics","10.1016/j.jmoneco.2016.08.005","T","","anchor"),
("The cyclical dynamics of illiquid housing, debt, and foreclosures",2016,"Quantitative Economics","10.3982/qe483","T","Hedlund","resolver"),
("Volatility in Home Sales and Prices: Supply or Demand?",2024,"Journal of Urban Economics","10.1016/j.jue.2023.103610","C","Anenberg Ringo","anchor"),
("Directed search in the housing market",2016,"Review of Economic Dynamics","10.1016/j.red.2015.05.002","T","","anchor"),
("The cyclical behavior of the Beveridge Curve in the housing market",2019,"Journal of Economic Theory","10.1016/j.jet.2019.03.003","T","","anchor"),
("Search and credit frictions in the housing market",2021,"European Economic Review","10.1016/j.euroecorev.2021.103699","T","Gabrovski Ortego-Marti","resolver"),
("Segmented Housing Search",2020,"American Economic Review","10.1257/aer.20141772","D/A","Piazzesi Schneider Stroebel","anchor"),
("Local Experiences, Search, and Spillovers in the Housing Market",2023,"The Journal of Finance","10.1111/jofi.13208","D","Gargano Giacoletti Jarnecic (journal version of SSRN R832)","resolver"),
("Why Is Intermediating Houses So Difficult? Evidence from iBuyers",2026,"Journal of Political Economy","10.1086/742710","C","Buchak et al. (journal version of SSRN R615)","resolver"),
("Evidence of Buyer Bargaining Power in the Stockholm Residential Real Estate Market",2008,"Journal of Real Estate Research","10.1080/10835547.2008.12091227","B","","resolver"),
("Effects of Real Estate Brokers' Marketing Strategies: Public Open Houses and MLS Virtual Tours",2015,"Journal of Real Estate Research","10.1080/10835547.2015.12091422","A","peripheral broker marketing TOM","resolver"),
("Search, Liquidity, and the Dynamics of House Prices and Construction",2014,"American Economic Review","10.1257/aer.104.4.1172","T","Head Lloyd-Ellis Sun","anchor"),
("Hot and Cold Seasons in the Housing Market",2014,"American Economic Review","10.1257/aer.104.12.3991","C","Ngai Tenreyro","anchor"),
("House Price Momentum and Strategic Complementarity",2018,"Journal of Political Economy","10.1086/697207","B","Guren list price momentum","anchor"),
("An Empirical Stationary Equilibrium Search Model of the Housing Market",2012,"International Economic Review","10.1111/j.1468-2354.2011.00677.x","T","Carrillo 2012","anchor"),
("Mortgage Debt, Consumption, and Illiquid Housing Markets in the Great Recession",2020,"American Economic Review","10.1257/aer.20170772","T","Garriga Hedlund","anchor"),
("A More Timely House Price Index",2017,"Review of Economics and Statistics","10.1162/rest_a_00634","B/D","Anenberg Laufer list-price index","anchor"),
("Does Time-on-Market Measurement Matter?",2015,"The Journal of Real Estate Finance and Economics","10.1007/s11146-013-9450-z","A","Benefield Hardin measurement","anchor"),
("Integrating Real Estate Market Conditions into Home Price Forecasting Systems",2012,"Journal of Housing Research","10.1080/10835547.2012.12092059","C","Miller Sklarz lead indicators","anchor"),
("Forecasting Residential Real Estate Price Changes from Online Search Activity",2013,"Journal of Real Estate Research","10.1080/10835547.2013.12091364","D","Beracha Wintoki","anchor"),
("Estimating House Price Indexes in the Presence of Seller Reservation Prices",2006,"Review of Economics and Statistics","10.1162/003465306775565783","B/C","Goetzmann Peng selection","anchor"),
("Search and matching in the housing market",2012,"Journal of Urban Economics","10.1016/j.jue.2012.01.002","A/T","Genesove Han","anchor"),
("Intercity Information Diffusion and Price Discovery in Housing Markets: Evidence from Google Searches",2015,"The Journal of Real Estate Finance and Economics","10.1007/s11146-014-9493-9","D","","recovery"),
("Online Information Search, Market Fundamentals and Apartment Real Estate",2015,"The Journal of Real Estate Finance and Economics","10.1007/s11146-015-9496-1","D","","recovery"),
("Google Search Queries, Foreclosures, and House Prices",2020,"The Journal of Real Estate Finance and Economics","10.1007/s11146-020-09789-y","D","","recovery"),
("House price index based on online listing information: The case of China",2020,"Journal of Housing Economics","10.1016/j.jhe.2020.101715","B/D","","recovery"),
("Web-scraping housing prices in real-time: The Covid-19 crisis in the UK",2023,"Journal of Housing Economics","10.1016/j.jhe.2022.101906","B/D","","recovery"),
("Further Assessment of the Efficiency Effects of Internet Use in Home Search",2012,"Journal of Real Estate Research","10.1080/10835547.2012.12091344","A/D","search duration internet","recovery"),
("Improving search efficiency in housing markets using online listings",2024,"Real Estate Economics","10.1111/1540-6229.12482","A/D","","recovery"),
("Bidding Wars for Houses",2013,"Real Estate Economics","10.1111/reec.12015","B/C","above-list sales as heat","recovery"),
("Listing Agent Signals: Does a Picture Paint a Thousand Words?",2018,"The Journal of Real Estate Finance and Economics","10.1007/s11146-018-9674-z","A","peripheral photos TOM","recovery"),
("From digital search to deed: forecasting UK housing purchases in Spain using Google Trends across the Brexit divide",2026,"Journal of European Real Estate Research","10.1108/jerer-07-2025-0060","D","","recovery"),
("Analysis of the Relationship Between COVID-19 Infections and Web-Based Housing Searches",2022,"Real Estate Management and Valuation","10.2478/remav-2022-0031","D","","recovery"),
("Predicting Housing Price Trends in Poland: Online Social Engagement - Google Trends",2023,"Real Estate Management and Valuation","10.2478/remav-2023-0032","D","","recovery"),
("Is the behavior of sellers with expected gains and losses relevant to cycles in house prices?",2021,"Journal of Housing Economics","10.1016/j.jhe.2021.101750","B","seller list price behavior (full text)","recovery"),
("Capitalizing consumer school ratings into residential listing prices: evidence from Greater Houston",2026,"International Journal of Housing Markets and Analysis","10.1108/ijhma-07-2026-0273","B","peripheral listing prices (full text)","recovery"),
("Buyer Search Intensity and the Role of the Residential Real Estate Broker",1999,"The Journal of Real Estate Finance and Economics","10.1023/a:1007737102125","A/D","buyer search intensity (full text)","recovery"),
]

ADD2=[
("Asymmetric information, signaling, and round listing prices: evidence from China's housing market",2023,"Applied Economics","10.1080/00036846.2023.2244252","B","round listing prices","recovery2"),
("Explaining the Pace of Foreclosed Home Sales during the US Foreclosure Crisis: Evidence from Atlanta",2012,"Housing Studies","10.1080/02673037.2012.728576","A","pace of foreclosed sales","recovery2"),
("Optimal Real Estate Pricing and Offer Acceptance Strategy",2023,"IEEE Access","10.1109/access.2023.3284549","B/T","optimal pricing offer acceptance (full text)","recovery2"),
("Listing behaviour in the Italian real estate market",2015,"International Journal of Housing Markets and Analysis","10.1108/ijhma-01-2014-0003","B","","recovery2"),
("Do hurricanes matter?",2017,"International Journal of Housing Markets and Analysis","10.1108/ijhma-06-2016-0045","A","peripheral hurricanes TOM (full text)","recovery2"),
("Real estate list price anchoring and cognitive ability",2019,"International Journal of Housing Markets and Analysis","10.1108/ijhma-08-2018-0060","B","","recovery2"),
("TOM: Why isn't Price Enough?",2003,"International Real Estate Review","10.2139/ssrn.406101","A","IRER 2003; DOI is SSRN mirror, replace with IRER record","recovery2"),
("The impact of house characteristics on the bargaining outcome",2013,"Journal of European Real Estate Research","10.1108/jerer-12-2012-0030","B","","recovery2"),
("Incorporating the Number of Existing Home Sales into a Structural Model of the Market for Owner-Occupied Housing",1995,"Journal of Housing Economics","10.1006/jhec.1995.1005","C","","recovery2"),
("List price and sales prices of residential properties during booms and busts",2013,"Journal of Housing Economics","10.1016/j.jhe.2013.01.003","B","Haurin McGreal Adair","recovery2"),
("Listing strategies and housing busts: Cutting loss or cutting list price?",2019,"Journal of Housing Economics","10.1016/j.jhe.2018.09.006","B","Liu van der Vlist","recovery2"),
("Selling price, time on the market, and contractual contingencies",2025,"Journal of Housing Economics","10.1016/j.jhe.2025.102062","A","Lin Seiler Siebert","recovery2"),
("The Influence of Contingent Closing Costs on Sale Price, Time on Market, and Probability of Sale",2009,"Journal of Housing Research","10.1080/10835547.2009.12092008","A","","recovery2"),
("Charm Pricing as a Signal of Listing Price Precision",2004,"Journal of Housing Research","10.1080/10835547.2004.12091967","B","","recovery2"),
("Could We Have Predicted the Recent Downturn in Home Sales in the Four U.S. Census Regions?",2010,"Journal of Housing Research","10.1080/10835547.2010.12092026","C","home sales forecasting","recovery2"),
("Marketing Time and Pricing Strategies",2012,"Journal of Real Estate Research","10.1080/10835547.2012.12091342","A/B","","recovery2"),
("Bigger is not Better: Brokerage and Time on the Market",1995,"Journal of Real Estate Research","10.1080/10835547.1995.12090770","A","peripheral brokerage TOM","recovery2"),
("Does Neighborhood Condition Create a Discount Effect on House List Prices? Evidence from Physical Disorder",2018,"Journal of Real Estate Research","10.1080/10835547.2018.12091492","B","peripheral list price discount","recovery2"),
("Mispricing and Optimal Time on the Market",1993,"Journal of Real Estate Research","10.1080/10835547.1993.12090697","A/B","","recovery2"),
("The Repeat Time-On-The-Market Index",2019,"Journal of Urban Economics","10.1016/j.jue.2019.04.005","C","Carrillo Williams repeat-TOM index — measurement core","recovery2"),
("List Prices in the US Housing Market",2016,"The Journal of Real Estate Finance and Economics","10.1007/s11146-016-9555-2","B","","recovery2"),
("Properties that Sell at or above Listing Price: Strategic Pricing, Better Broker or Just Dumb Luck?",2020,"The Journal of Real Estate Finance and Economics","10.1007/s11146-019-09714-y","B","","recovery2"),
("Cross sectional Analysis of time on Market indicators for an Australian City",2012,"Pacific Rim Property Research Journal","10.1080/14445921.2012.11104370","A/C","TOM indicators Adelaide","recovery2"),
("Estimating Bargaining Effects in Hedonic Models: Evidence from the Housing Market",2003,"Real Estate Economics","10.1046/j.1080-8620.2003.00078.x","B","bargaining list-sale (full text)","recovery2"),
("The Impacts of Contract Type on Broker Performance",2001,"Real Estate Economics","10.1111/1080-8620.00016","A","peripheral broker contract TOM","recovery2"),
("The Effects of Charm Listing Prices on House Transaction Prices",2004,"Real Estate Economics","10.1111/j.1080-8620.2004.00108.x","B","","recovery2"),
("The Economic Impact of Anticipated House Price Changes—Evidence from Home Sales",2011,"Real Estate Economics","10.1111/j.1540-6229.2010.00292.x","C","home sales volume","recovery2"),
("School quality as a catalyst for bidding wars and new housing development",2023,"Real Estate Economics","10.1111/1540-6229.12426","B/C","peripheral bidding wars (full text)","recovery2"),
("Asymmetric information and list-price reductions in the housing market",2013,"Regional Science and Urban Economics","10.1016/j.regsciurbeco.2013.03.001","B","de Wit van der Klaauw","recovery2"),
("Selling price, financing premiums, and days on the market",1989,"The Journal of Real Estate Finance and Economics","10.1007/bf00152349","A","","recovery2"),
("List price signaling and buyer behavior in the housing market",1994,"The Journal of Real Estate Finance and Economics","10.1007/bf01099271","B","","recovery2"),
("Using Leading Indicators to Forecast U.S. Home Sales in a Bayesian Vector Autoregressive Framework",1999,"The Journal of Real Estate Finance and Economics","10.1023/a:1007718725609","C","home sales forecasting","recovery2"),
("Forecasting Connecticut home sales in a BVAR framework using coincident and leading indexes",1996,"The Journal of Real Estate Finance and Economics","10.1007/bf00217392","C","home sales forecasting","recovery2"),
("Neighborhood Institutions and Residential Home Sales: Evaluating the Impact of Property Tax Exemptions",2021,"The Journal of Real Estate Finance and Economics","10.1007/s11146-020-09808-y","C","peripheral home sales (full text)","recovery2"),
("Qualitative Response Estimations of the Selling Behaviour in the Swedish Market for Owner-Occupied Houses",1988,"Urban Studies","10.1080/00420988820080071","A/B","","recovery2"),
("Optimal List Price and Duration of Vacancy in the Housing Market in Tokyo",2016,"Review of Urban & Regional Development Studies","10.1111/rurd.12053","B/A","","recovery2"),
]
ADD=ADD+ADD2

for t,y,v,d,tier,n,prov in ADD:
    inc.append(dict(rid="ADD",doi=d.lower(),title=t,year=y,venue=v,authors="",tier=tier,status="I",note=n,provenance=prov))
# dedupe by doi, then title
seen={};final=[]
def nt(t): t=t.lower(); t=re.sub(r"[^a-z0-9 ]"," ",t); return re.sub(r"\s+"," ",t).strip()
for r in inc:
    k=r["doi"] or nt(r["title"])
    if k in seen or nt(r["title"]) in seen: continue
    seen[k]=1; seen[nt(r["title"])]=1; final.append(r)
for r in final:
    r["layer"]="theory" if "T" in r["tier"] else ("peripheral" if peri.search(r["note"]+" "+r["title"]) and not re.search(r"liquidity ind|tightness|hot|price dispersion|list(ing)? price|asking price|relist|withdraw|TOM distribution|measurement|search|volume|turnover|absorption|inventory|forecast|index|KR|probability of sale|censored|TOM and|price-TOM|TOM-price|seller motivation|hazard|duration",r["note"]+" "+r["title"],re.I) else "core")
final.sort(key=lambda r:(r["layer"],str(r["year"])))
with open("included_studies.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(final[0].keys())); w.writeheader(); w.writerows(final)
from collections import Counter
print("included total:",len(final)); print(Counter(r["layer"] for r in final)); print(Counter(r["status"] for r in final)); print("no doi:",[(r["rid"],r["title"][:40]) for r in final if not r["doi"]])
print(Counter(r["tier"] for r in final).most_common())
yrs=Counter((int(r["year"])//10*10) if str(r["year"]).isdigit() else 0 for r in final); print(sorted(yrs.items()))
