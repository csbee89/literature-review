#!/usr/bin/env python3
"""주차별 배정표 생성 (v6, 2026-10-13 — 깊이 차등 + 주차별 몫 수).
사용: python3 scripts/assign.py [--start 2026-10-19] [--pilot p023] [--ramp 1x5,2] --out students/assignments.csv
     (--ramp 1x5,3 이면 W6부터 1인 3몫)

규칙
- 종합 대상(scope=synthesis)만. 한 사람의 한 주 몫 수는 --ramp: 기본 '1x5,2' = W1~W5는 1몫, W6부터 2몫.
- W01 = 파일럿: 8명 전원이 같은 논문(--pilot)을 정리 → 원석이 8개를 비교해 양식 해석 차이를 잡는다.
- W02~ = 한국 논문 먼저(언어 부담 없음, KCI·RISS 무료 원문, RQ5 핵심) → 그다음 영문을 단계 순 S3→S2→S5→S4→S1.
  같은 단계 안에서는 F1 정의·구축 → F2 측정 쟁점 → F3 선행성, 그 안에서 연도순.
- 어려운 논문(경제학 상위 학술지·구조모형)은 그 주의 석·박사에게 먼저 배정.
- 짝(checker)은 4주마다 바뀐다.
- --done 의 논문(p115 = 정리 예시)은 배정하지 않는다.
- 추출 깊이(synthesis_set.csv의 depth): full = 1쪽 양식(2시간), short = 짧은 양식(30분).
  몫(slot) 하나 = full 1편 또는 short 4편(단계 순서대로 4편씩 꽉 채움, 한국·영문은 따로)."""
import csv,argparse,re,datetime
ap=argparse.ArgumentParser()
ap.add_argument("--start",default="2026-10-19"); ap.add_argument("--pilot",default="p023")
ap.add_argument("--done",default="p115",help="이미 정리된 논문(예시 등), 쉼표 구분 — 배정에서 뺀다")
ap.add_argument("--inc",default="review/synthesis_set.csv"); ap.add_argument("--out",required=True)
ap.add_argument("--ramp",default="1x5,2",help="주차별 1인 몫 수. 예: 1x5,2 = 처음 5주 1몫, 이후 2몫")
a=ap.parse_args()
rows=list(csv.DictReader(open(a.inc,encoding="utf-8")))
def is_kr(r): return bool(re.search(r"KR|Korea",r["note"]+r["venue"]) or re.search(r"[가-힣]",r["venue"]+r["title"]))
HARD=re.compile(r"American Economic Review|Journal of Political Economy|Review of Economic Studies|Quarterly Journal|Econometrica|Journal of Finance|Review of Financial|International Economic Review|RAND Journal|Review of Economics and Statistics|Journal of Urban Economics|Journal of Monetary|Economic Theory",re.I)
def hard(r): return bool(HARD.search(r["venue"]))
STAGE_ORDER={"S3":0,"S2":1,"S5":2,"S4":3,"S1":4}
pilot=[r for r in rows if r["pid"]==a.pilot][0]
DONE=set(x for x in a.done.split(",") if x)
rest=[r for r in rows if r["pid"]!=a.pilot and r["pid"] not in DONE]
def slots(group,order_key):
    """단계 순서대로 full은 1편씩, short는 4편씩 꽉 채워 묶는다(단계 경계를 넘을 수 있음)."""
    res=[]; buf=[]
    for r in sorted(group,key=order_key):
        if r.get("depth")=="short":
            buf.append(r)
            if len(buf)==4: res.append(buf); buf=[]
        else: res.append([r])
    if buf: res.append(buf)
    return res
okey=lambda r:(STAGE_ORDER[r["stage"][:2]],r.get("depth","full")=="short",r["function"][:2],r["year"])
queue=slots([r for r in rest if is_kr(r)],okey)+slots([r for r in rest if not is_kr(r)],okey)
people=["박사","석사①","석사②","학부①","학부②","학부③","학부④","이원석"]
GRAD={"박사","석사①","석사②"}
rot=[["석사①","박사","학부①","석사②","학부③","학부②","이원석","학부④"],   # 각 사람의 짝 (4주마다 순환)
     ["학부①","학부②","박사","학부③","석사①","이원석","석사②","학부④"],
     ["석사②","학부③","박사","학부④","이원석","석사①","학부①","학부②"]]
def checker(i,wk):
    pairs=rot[((wk-1)//4)%len(rot)]
    c=pairs[i]
    return c if c!=people[i] else people[(i+1)%8]
start=datetime.date.fromisoformat(a.start); out=[]
def rec(wk,person,r,i,kind,slot=""):
    d0=start+datetime.timedelta(weeks=wk-1)
    return dict(week=f"W{wk:02d}",assign_date=d0.isoformat(),due_date=(d0+datetime.timedelta(days=4)).isoformat(),person=person,kind=kind,
        slot=slot,depth=r.get("depth","full") if kind!="pilot" else "full",pid=r["pid"],stage=r["stage"][:2],function=r["function"][:2],regime=r["regime"],korean="Y" if is_kr(r) else "",
        year=r["year"],title=r["title"],venue=r["venue"],doi=r["doi"],tier=r["tier"],status=r["status"],checker=checker(i,wk) if kind!="pilot" else "전원 비교(원석)")
for i,p in enumerate(people): out.append(rec(1,p,pilot,i,"pilot"))
ramp=[]
for part in a.ramp.split(","):
    k,_,n=part.partition("x"); ramp.append((int(k),int(n) if n else None))
def per_person(wk):
    w=wk
    for k,n in ramp:
        if n is None or w<=n: return k
        w-=n
    return ramp[-1][0]
wk=2
order=[p for p in people if p in GRAD]+[p for p in people if p not in GRAD]
while queue:
    k=per_person(wk)
    batch=queue[:8*k]; queue=queue[8*k:]
    batch=[sl for sl in batch if any(hard(r) for r in sl)]+[sl for sl in batch if not any(hard(r) for r in sl)]
    for j,sl in enumerate(batch):
        p=order[j%8]; sid=f"W{wk:02d}-{people.index(p)+1}-{j//8+1}"
        for r in sl: out.append(rec(wk,p,r,people.index(p),r.get("depth","full"),sid))
    wk+=1
out.sort(key=lambda x:(x["week"],people.index(x["person"])))
w=csv.DictWriter(open(a.out,"w",encoding="utf-8",newline=""),fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
last=max(x["due_date"] for x in out)
kw=sorted({x["week"] for x in out if x["korean"]=="Y" and x["kind"]!="pilot"})
print(f"pilot={a.pilot} | ramp={a.ramp} | weeks={wk-1} | papers={len({x['pid'] for x in out})} | korean weeks {kw[0]}-{kw[-1]} | end {last}")
