#!/usr/bin/env python3
"""주차별 배정표 생성. 사용: python3 scripts/assign.py --option 1|3 --start 2026-10-12 --out students/assignments_optionN.csv
옵션1: core+theory 전수 완전추출(석박사 주2, 학부 주1) + peripheral 경량추출(전원 주1).
옵션3: core를 '지표 자체가 연구대상인 논문'으로 재정의(측정·시장지표·호가전략·탐색지표·이론·한국). 나머지 A층 결정요인 연구는 경량추출."""
import csv,argparse,re,datetime
ap=argparse.ArgumentParser(); ap.add_argument("--option",type=int,default=3); ap.add_argument("--start",default="2026-10-12"); ap.add_argument("--out",required=True); ap.add_argument("--inc",default="review/included_studies.csv"); ap.add_argument("--grad",type=int,default=2,help="석·박사 1인 주당 완전추출 편수(기본 2)")
a=ap.parse_args()
rows=list(csv.DictReader(open(a.inc,encoding="utf-8")))
measure=re.compile(r"measur|index|indices|censored|hazard|probability of (a )?sale|quick sale|relist|withdraw|distribution|competing|endogeneity|nonlinearity|simultaneous|spatiotemporal solution|inverted U|puzzle|seller motivation|seller heterogeneity|hot (and|or) cold|tightness|KR|Korea|Busan|Seoul|time to close|methodolog|estimating time|parametric|generalized geometric|joint model|optimal (TOM|time)|TOM indicators|duration of marketing|search benefit|price-TOM relation|market conditions, marketing time|credit conditions|thin market|TOM distribution|illiquidity|liquidity (and|&) (price|information)|residential liquidity|home liquidity|liquidity imbalance",re.I)
def is_core3(r):
    t=r["tier"]; txt=r["note"]+" "+r["title"]
    if r["layer"]=="theory": return True
    if r["layer"]=="peripheral": return False
    if "C" in t or "D" in t: return True
    if "B" in t: return not re.search(r"peripheral",r["note"])
    return bool(measure.search(txt))
for r in rows:
    r["workload"]="full" if (r["layer"]!="peripheral" if a.option==1 else is_core3(r)) else "light"
full=[r for r in rows if r["workload"]=="full"]; light=[r for r in rows if r["workload"]=="light"]
# priority: anchors/resolver first, then earlier-known classics by citation proxy (year asc for classics), then rest by year desc
prev=set()
try:
    for x in csv.DictReader(open("students/assignments.csv",encoding="utf-8")): prev.add(x["doi"].lower())
except FileNotFoundError: pass
def prio(r):
    return (0 if r["doi"].lower() in prev else 1, 0 if r["provenance"] in ("anchor","resolver") else 1, str(r["year"]))
full.sort(key=prio); light.sort(key=lambda r:str(r["year"]))
# W1~W4 고정 배정(앵커 32편, 2026-10-07 배정표 승계): (person, title regex)
FIXED=[("박사",r"To Sell or Not to Sell: Measuring the Heat"),("석사①",r"Local Constant-Quality Housing Market Liquidity"),("석사②",r"Equity and Time to Sale"),("학부①",r"Duration of Marketing Time of Residential"),("학부②",r"Measuring Residential Real Estate Liquidity"),("학부③",r"Listing Price, Time on Market, and Ultimate"),("학부④",r"Days on market and home sales"),("이원석",r"Spatiotemporal Solution"),
("박사",r"Search, Liquidity, and the Dynamics of House Prices"),("석사①",r"Can Tightness in the Housing Market"),("석사②",r"Asymmetric information and list-price reductions"),("학부①",r"Selling Time and Selling Price: The Influence of Seller Motivation"),("학부②",r"Trade-off Between the Selling Price"),("학부③",r"How do market conditions impact price-TOM"),("학부④",r"Relisting, Agent Switching"),
("박사",r"House Prices, Sales and Time on the Market: A Search"),("석사①",r"The Impact of TOM on Prices in the US"),("석사②",r"Search and matching in the housing market"),("학부①",r"Search and Liquidity in Single-Family"),("학부②",r"Listing strategies and housing busts"),("학부③",r"Selling price, time on the market, and contractual"),("학부④",r"Integrating Real Estate Market Conditions"),("이원석",r"Internet Search Behavior, Liquidity and Prices"),
("박사",r"Hot and Cold Seasons in the Housing Market"),("석사①",r"A More Timely House Price Index"),("석사②",r"On the Relationship Between Property Price, Time-on-Market, and Photo"),("학부①",r"The Probability of Sale for Residential Real Estate"),("학부②",r"Market Conditions, Marketing Time, and House Prices"),("학부③",r"Liquidity Imbalance in the Residential"),("학부④",r"Forecasting Residential Real Estate Price Changes from Online Search"),("이원석",r"House hunting high and low")]
import re as _re
pre_assigned=[]
for person,rx in FIXED:
    hit=False
    for i,r in enumerate(full):
        if _re.search(rx,r["title"],_re.I):
            pre_assigned.append((person,full.pop(i))); hit=True; break
    if not hit:  # 앵커가 경량 층에 있으면 완전추출로 끌어올린다
        for i,r in enumerate(light):
            if _re.search(rx,r["title"],_re.I):
                r["workload"]="full"; pre_assigned.append((person,light.pop(i))); hit=True; break
    if not hit: print("WARN fixed anchor not found:",rx)

people=[("박사",a.grad,"T,C"),("석사①",a.grad,"C,B,D"),("석사②",a.grad,"B,D,C"),("학부①",1,"A"),("학부②",1,"A"),("학부③",1,"A"),("학부④",1,"A"),("이원석",1,"A,KR")]
pairs={"박사":"석사①","석사①":"박사","석사②":"학부①","학부①":"석사②","학부②":"학부③","학부③":"학부②","학부④":"이원석","이원석":"학부④"}
# distribute full by tier preference
def pick(pool,pref):
    for p in pref.split(","):
        for i,r in enumerate(pool):
            if p=="KR" and re.search(r"KR|Korea",r["note"]+r["venue"]): return pool.pop(i)
            if p!="KR" and p in r["tier"]: return pool.pop(i)
    return pool.pop(0) if pool else None
out=[]; start=datetime.date.fromisoformat(a.start); wk=1
pool=list(full)
pending={p:[r for q,r in pre_assigned if q==p] for p,_,_ in people}
while pool or any(pending.values()):
    d0=start+datetime.timedelta(weeks=wk-1); d1=d0+datetime.timedelta(days=4)
    for name,n,pref in people:
        for k in range(n):
            r=pending[name].pop(0) if pending[name] else pick(pool,pref)
            if not r: break
            out.append(dict(week=f"W{wk:02d}",assign_date=d0.isoformat(),due_date=d1.isoformat(),person=name,workload="full",layer=r["layer"],tier=r["tier"],first_author=(r["authors"].split(";")[0].split(",")[0] if r["authors"] else ""),year=r["year"],title=r["title"],venue=r["venue"],doi=r["doi"],status=r["status"],note=r["note"],checker=pairs[name]))
    wk+=1
full_weeks=wk-1
lp=list(light); wk=1
while lp:
    d0=start+datetime.timedelta(weeks=wk-1); d1=d0+datetime.timedelta(days=4)
    for name,n,pref in people:
        if not lp: break
        r=lp.pop(0)
        out.append(dict(week=f"W{wk:02d}",assign_date=d0.isoformat(),due_date=d1.isoformat(),person=name,workload="light",layer=r["layer"],tier=r["tier"],first_author=(r["authors"].split(";")[0].split(",")[0] if r["authors"] else ""),year=r["year"],title=r["title"],venue=r["venue"],doi=r["doi"],status=r["status"],note=r["note"],checker=pairs[name]))
    wk+=1
out.sort(key=lambda x:(x["week"],x["workload"]!="full",x["person"]))
with open(a.out,"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print(f"option {a.option}: full={len(full)} light={len(light)} | full weeks={full_weeks} (11/wk) | light weeks={wk-1} (8/wk) | end {start+datetime.timedelta(weeks=max(full_weeks,wk-1)-1,days=4)}")
