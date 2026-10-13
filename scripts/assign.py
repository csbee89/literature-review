#!/usr/bin/env python3
"""주차별 배정표 생성 (v4, 2026-10-13).
사용: python3 scripts/assign.py [--start 2026-10-19] [--pilot p023] --out students/assignments.csv

규칙
- 전원 매주 1편(8명 → 주 8편). 종합 대상(scope=synthesis)만.
- W01 = 파일럿: 8명 전원이 같은 논문(--pilot)을 정리 → 원석이 8개를 비교해 양식 해석 차이를 잡는다.
- W02~ = 한국 논문 먼저(언어 부담 없음, KCI·RISS 무료 원문, RQ5 핵심) → 그다음 영문을 단계 순 S3→S2→S5→S4→S1.
  같은 단계 안에서는 F1 정의·구축 → F2 측정 쟁점 → F3 선행성, 그 안에서 연도순.
- 어려운 논문(경제학 상위 학술지·구조모형)은 그 주의 석·박사에게 먼저 배정.
- 짝(checker)은 4주마다 바뀐다.
- --done 의 논문(p115 = 정리 예시)은 배정하지 않는다."""
import csv,argparse,re,datetime
ap=argparse.ArgumentParser()
ap.add_argument("--start",default="2026-10-19"); ap.add_argument("--pilot",default="p023")
ap.add_argument("--done",default="p115",help="이미 정리된 논문(예시 등), 쉼표 구분 — 배정에서 뺀다")
ap.add_argument("--inc",default="review/synthesis_set.csv"); ap.add_argument("--out",required=True)
a=ap.parse_args()
rows=list(csv.DictReader(open(a.inc,encoding="utf-8")))
def is_kr(r): return bool(re.search(r"KR|Korea",r["note"]+r["venue"]) or re.search(r"[가-힣]",r["venue"]+r["title"]))
HARD=re.compile(r"American Economic Review|Journal of Political Economy|Review of Economic Studies|Quarterly Journal|Econometrica|Journal of Finance|Review of Financial|International Economic Review|RAND Journal|Review of Economics and Statistics|Journal of Urban Economics|Journal of Monetary|Economic Theory",re.I)
def hard(r): return bool(HARD.search(r["venue"]))
STAGE_ORDER={"S3":0,"S2":1,"S5":2,"S4":3,"S1":4}
pilot=[r for r in rows if r["pid"]==a.pilot][0]
DONE=set(x for x in a.done.split(",") if x)
rest=[r for r in rows if r["pid"]!=a.pilot and r["pid"] not in DONE]
kr=sorted([r for r in rest if is_kr(r)],key=lambda r:(r["stage"][:2],r["function"][:2],r["year"]))
en=sorted([r for r in rest if not is_kr(r)],key=lambda r:(STAGE_ORDER[r["stage"][:2]],r["function"][:2],r["year"]))
queue=kr+en
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
def rec(wk,person,r,i,kind):
    d0=start+datetime.timedelta(weeks=wk-1)
    return dict(week=f"W{wk:02d}",assign_date=d0.isoformat(),due_date=(d0+datetime.timedelta(days=4)).isoformat(),person=person,kind=kind,
        pid=r["pid"],stage=r["stage"][:2],function=r["function"][:2],regime=r["regime"],korean="Y" if is_kr(r) else "",
        year=r["year"],title=r["title"],venue=r["venue"],doi=r["doi"],tier=r["tier"],status=r["status"],checker=checker(i,wk) if kind!="pilot" else "전원 비교(원석)")
for i,p in enumerate(people): out.append(rec(1,p,pilot,i,"pilot"))
wk=2
while queue:
    batch=queue[:8]; queue=queue[8:]
    hardp=[r for r in batch if hard(r)]; easy=[r for r in batch if not hard(r)]
    order=[p for p in people if p in GRAD]+[p for p in people if p not in GRAD]
    picks=hardp+easy
    for p,r in zip(order,picks): out.append(rec(wk,p,r,people.index(p),"full"))
    wk+=1
out.sort(key=lambda x:(x["week"],people.index(x["person"])))
w=csv.DictWriter(open(a.out,"w",encoding="utf-8",newline=""),fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
last=max(x["due_date"] for x in out)
print(f"pilot={a.pilot} | weeks={wk-1} | papers={len({x['pid'] for x in out})} | korean weeks W02-W{1+ (len(kr)+7)//8:02d} | end {last}")
