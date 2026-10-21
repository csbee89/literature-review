#!/usr/bin/env python3
"""주차별 배정표 생성 (v8, 2026-10-21 — 청년 주거경로 리뷰와 같은 방식).
사용: python3 scripts/assign.py [--meet 2026-10-28] [--w1 2026-10-19] [--ramp 1x5,2] [--defer-missing] --out students/assignments.csv
     (--ramp 1x5,3 이면 W6부터 1인 3편)

규칙
- 종합 대상(scope=synthesis)만. 정리 단위는 논문 1편(워드 1쪽 + 구글시트 행). 긴·짧은 구분 없음.
- 한 사람의 한 주 편수는 --ramp: 기본 '1x5,2' = W1~W5는 1편, W6부터 2편.
  W1~W5는 같은 8명이 청년 주거경로 리뷰(10/21~11/24, 주 1편)를 함께 하는 기간이다.
- 매주 수요일 모임. 모임에서 다음 논문 배정, 모임 전날(화) 18:00 마감(청년 리뷰와 같은 요일).
  W1만 모임 전에 미리 배포(--w1, 기본 10/19 월) → 첫 모임 10/28(수).
- --defer-missing: 원문이 아직 없거나 게재본이 아닌 논문(pdf_status != '받음')은 순서에서 빼서
  맨 마지막 주에 따로 모은다(원문 확보 후 배포, 끝내 못 구하면 그 주만 비운다). v8, 연구책임자 지시 10/21.
- 파일럿 없음. 정리 예시(--examples, 기본 p115·p033)는 배정하지 않는다.
- 한국 논문 먼저(언어 부담 없음, RQ5 핵심) → 영문을 단계 순 S3→S2→S5→S4→S1.
  같은 단계 안에서는 F1 → F2 → F3, 그 안에서 연도순.
- 어려운 논문(경제학 상위 학술지·구조모형)은 그 주의 석·박사에게 먼저.
- 짝 점검 없음. 학생 정리 = 독립 2차 추출. Claude가 원문으로 1차 추출을 따로 해 두고,
  매주 둘을 맞춘 대조표를 만들며, 다른 곳은 연구책임자가 판정한다(프로토콜 §8, 코드북 §H)."""
import csv, argparse, re, datetime

ap = argparse.ArgumentParser()
ap.add_argument("--meet", default="2026-10-28", help="첫 모임(수요일). W01 마감은 그 전날 18:00")
ap.add_argument("--w1", default="2026-10-19", help="W01 배포일(첫 모임 전)")
ap.add_argument("--examples", default="p115,p033", help="정리 예시로 쓰는 논문 — 배정에서 뺀다")
ap.add_argument("--inc", default="review/synthesis_set.csv")
ap.add_argument("--pdf", default="papers/pdf_status.csv")
ap.add_argument("--out", required=True)
ap.add_argument("--defer-missing", action="store_true", help="원문 없는 논문을 마지막 주로")
ap.add_argument("--ramp", default="1x5,2", help="1인 주당 편수. 1x5,2 = 처음 5주 1편, 이후 2편")
a = ap.parse_args()

rows = list(csv.DictReader(open(a.inc, encoding="utf-8")))
pdf = {r["pid"]: r["pdf_status"] for r in csv.DictReader(open(a.pdf, encoding="utf-8-sig"))}


def is_kr(r):
    return bool(re.search(r"KR|Korea", r["note"] + r["venue"]) or re.search(r"[가-힣]", r["venue"] + r["title"]))


HARD = re.compile(r"American Economic Review|Journal of Political Economy|Review of Economic Studies|Quarterly Journal|"
                  r"Econometrica|Journal of Finance|Review of Financial|International Economic Review|RAND Journal|"
                  r"Review of Economics and Statistics|Journal of Urban Economics|Journal of Monetary|Economic Theory", re.I)
STAGE_ORDER = {"S3": 0, "S2": 1, "S5": 2, "S4": 3, "S1": 4}
EX = set(x for x in a.examples.split(",") if x)
rest = [r for r in rows if r["pid"] not in EX]
okey = lambda r: (STAGE_ORDER[r["stage"][:2]], r["function"][:2], r["year"])
queue = sorted([r for r in rest if is_kr(r)], key=okey) + sorted([r for r in rest if not is_kr(r)], key=okey)
held = [r for r in queue if a.defer_missing and pdf.get(r["pid"]) != "받음"]
queue = [r for r in queue if r not in held]

# 직급: 전우성(박사) · 손수연·최찬미(석사) · 이원석·이다윤(학부 3) · 오건·이지은·홍다연(학부 2)
people = ["전우성", "손수연", "최찬미", "이원석", "이다윤", "오건", "이지은", "홍다연"]
GRAD = {"전우성", "손수연", "최찬미"}
ramp = []
for part in a.ramp.split(","):
    k, _, n = part.partition("x")
    ramp.append((int(k), int(n) if n else None))


def per_person(wk):
    w = wk
    for k, n in ramp:
        if n is None or w <= n:
            return k
        w -= n
    return ramp[-1][0]


meet0 = datetime.date.fromisoformat(a.meet)
w1 = datetime.date.fromisoformat(a.w1)
out = []
wk = 1
order = [p for p in people if p in GRAD] + [p for p in people if p not in GRAD]
while queue or held:
    k = per_person(wk)
    if queue:
        batch, queue = queue[:8 * k], queue[8 * k:]
    else:  # 원문 대기 논문만 모은 마지막 주
        batch, held = held, []
    batch = [r for r in batch if HARD.search(r["venue"])] + [r for r in batch if not HARD.search(r["venue"])]
    meet = meet0 + datetime.timedelta(weeks=wk - 1)
    d0 = w1 if wk == 1 else meet - datetime.timedelta(days=7)
    for j, r in enumerate(batch):
        out.append(dict(week=f"W{wk:02d}", assign_date=d0.isoformat(), due_date=(meet - datetime.timedelta(days=1)).isoformat(),
                        meeting=meet.isoformat(),
                        person=order[j % 8], pid=r["pid"], stage=r["stage"][:2], function=r["function"][:2], regime=r["regime"],
                        korean="Y" if is_kr(r) else "", year=r["year"], title=r["title"], venue=r["venue"], doi=r["doi"],
                        tier=r["tier"], status=r["status"], pdf_status=pdf.get(r["pid"], "")))
    wk += 1
out.sort(key=lambda x: (x["week"], people.index(x["person"]), x["pid"]))
w = csv.DictWriter(open(a.out, "w", encoding="utf-8", newline=""), fieldnames=list(out[0].keys()))
w.writeheader()
w.writerows(out)
kw = sorted({x["week"] for x in out if x["korean"] == "Y"})
print(f"ramp={a.ramp} | weeks={wk - 1} | papers={len(out)} | korean {kw[0]}-{kw[-1]} | last due {max(x['due_date'] for x in out)}")
