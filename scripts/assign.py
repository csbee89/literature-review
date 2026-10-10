#!/usr/bin/env python3
"""주차별 배정표 생성(v3, 2026-10-10). 사용: python3 scripts/assign.py [--grad 2] [--start 2026-10-19] --out students/assignments.csv
종합 대상(scope=synthesis)만 배정한다. 전부 완전추출. 석·박사 1인 주 --grad 편, 학부 1편. 순서: 측정·정의(C1) 고전 → 연도순."""
import csv,argparse,re,datetime
ap=argparse.ArgumentParser(); ap.add_argument("--option",type=int,default=3); ap.add_argument("--start",default="2026-10-19"); ap.add_argument("--out",required=True); ap.add_argument("--inc",default="review/included_studies.csv"); ap.add_argument("--grad",type=int,default=2,help="석·박사 1인 주당 완전추출 편수(기본 2)")
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
rows=[r for r in rows if r.get("scope")=="synthesis"]
for r in rows: r["workload"]="full"
full=rows; light=[]
# priority: anchors/resolver first, then earlier-known classics by citation proxy (year asc for classics), then rest by year desc
prev=set()
try:
    for x in csv.DictReader(open("students/assignments.csv",encoding="utf-8")): prev.add(x["doi"].lower())
except FileNotFoundError: pass
def prio(r):
    return (0 if r["criterion"].startswith("C1") else 1, str(r["year"]))
full.sort(key=prio); light.sort(key=lambda r:str(r["year"]))
pre_assigned=[]
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
print(f"synthesis={len(out)} | weeks={full_weeks} | end {start+datetime.timedelta(weeks=full_weeks-1,days=4)}")
