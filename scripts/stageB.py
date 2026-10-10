import csv,re,html
def norm(s): return html.unescape(s or "").replace("‐","-").replace("‑","-").replace("–","-").replace("—","-").replace("’","'")
rows=list(csv.DictReader(open("merged_all.csv",encoding="utf-8")))
H=r"(hous\w*|home\w*|residential|dwelling\w*|apartment\w*|condo\w*|real estate|realt\w*|propert\w*|mls|listing\w*|seller\w*)"
strong=re.compile(r"time[- ]on[- ](the[- ])?market|\btom\b|days[- ]on[- ](the[- ])?market|\bdom\b|marketing (time|duration|period|span)|selling (time|duration|period)|time[- ]to[- ](sale|sell)|listing duration|duration of (the )?(listing|marketing|sale)|probability of (a )?(sale|selling)|likelihood of (a )?sale|withdraw\w* (from|of|listing)|listing\w* withdraw\w*|relist\w*|re-list\w*|list(ing)? price (change|reduction|cut|revision|adjustment|strateg|setting|premium)\w*|(change|reduction|cut|revision)s? (in|of|to) (the )?(list|listing|asking) price|asking price|sale[s]?[- ]to[- ]list|list[- ]to[- ]sale|over[- ]?pric\w*|under[- ]?pric\w*|price dispersion|("+H+r"\W+(\w+\W+){0,4})?liquidity|liquidity(\W+\w+){0,4}\W+"+H+r"|illiquid\w*|market tightness|tightness of (the )?"+H+r"|hot (and|or) cold|\b(hot|cold) (housing |real estate |property )?market|months.? (of )?(supply|inventory)|absorption rate|(for-sale|unsold|housing|home) inventor\w*|inventory of (unsold|homes|houses)|sales?[- ]to[- ](listing|inventory)s?|(housing|home|house) (sales )?turnover|turnover (rate|of (housing|homes|houses))|(transaction|sales|trading) volume|housing search (index|activity|duration|behavio)|search (index|volume|activity|behavio)\w*(\W+\w+){0,6}\W+(hous|home|real estate)|vacancy duration|time to (let|rent)",re.I)
rental=re.compile(r"\brent(al|ers|ed)?\b|tenant|landlord|lease|leasing",re.I)
out=[]
for r in rows:
    if not r["stageA"].startswith("candidate"): continue
    text=norm(r["title"])+" || "+norm(r["abstract"])
    m=strong.search(text)
    r["stageB"]="read" if m else "exclude"
    r["codeB"]="" if m else "E2-weak-only"
    r["hit"]=m.group(0)[:40] if m else ""
    out.append(r)
with open("stageB.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
read=[r for r in out if r["stageB"]=="read"]
from collections import Counter
print("stage-B read set:",len(read)," excluded weak-only:",len(out)-len(read))
print("by source:",Counter(r["sources"] for r in read).most_common(8))
print("with abstract:",sum(1 for r in read if r["abstract"]))
print("venues top:",Counter(r["venue"] for r in read).most_common(25))
