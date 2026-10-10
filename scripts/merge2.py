import json,re,csv,glob,html,os
def nt(t):
    t=re.sub(r"<[^>]+>","",t or ""); t=html.unescape(t).lower(); t=t.replace("‐","-").replace("–","-")
    t=re.sub(r"[^a-z0-9가-힣 ]"," ",t); return re.sub(r"\s+"," ",t).strip()
def is_preprint(doi,venue):
    return bool(re.search(r"ssrn|nber|10\.3386|arxiv|repec|mpra|wp\.|working",(doi or "")+" "+(venue or ""),re.I))
recs={}   # key: normalized title -> record (journal version preferred)
ident=0
def add(r):
    global ident; ident+=1
    k=nt(r["title"])
    if not k: return
    if k in recs:
        o=recs[k]
        # prefer journal (non-preprint) DOI/venue/year
        if is_preprint(o["doi"],o["venue"]) and not is_preprint(r["doi"],r["venue"]) and r["doi"]:
            o["doi"],o["venue"],o["year"]=r["doi"],r["venue"],r["year"]
        if not o["doi"] and r["doi"]: o["doi"]=r["doi"]; o["venue"]=o["venue"] or r["venue"]; o["year"]=o["year"] or r["year"]
        if not o["venue"] and r["venue"]: o["venue"]=r["venue"]
        if (not o["abstract"]) and r["abstract"]: o["abstract"]=r["abstract"]
        if not o["authors"] and r["authors"]: o["authors"]=r["authors"]
        o["cites"]=max(o["cites"] or 0,r["cites"] or 0); o["sources"]|=r["sources"]; o["blocks"]|=r["blocks"]
    else: recs[k]=r
def s2rec(w,src,blk):
    doi=((w.get("externalIds") or {}).get("DOI") or "").lower()
    venue=w.get("venue") or ((w.get("journal") or {}).get("name") if isinstance(w.get("journal"),dict) else "") or ""
    return dict(doi=doi,title=w.get("title") or "",year=w.get("year"),venue=venue,abstract=w.get("abstract") or "",cites=w.get("citationCount"),ptypes=";".join(w.get("publicationTypes") or []),sources={src},blocks={blk},authors="; ".join(a.get("name","") for a in (w.get("authors") or [])[:6]))
def crrec(w,src,blk):
    return dict(doi=(w.get("DOI") or "").lower(),title=(w.get("title") or [""])[0],year=((w.get("issued") or {}).get("date-parts") or [[None]])[0][0],venue=(w.get("container-title") or [""])[0] or w.get("_journal",""),abstract=re.sub(r"<[^>]+>","",w.get("abstract") or ""),cites=w.get("is-referenced-by-count"),ptypes="journal-article",sources={src},blocks={blk},authors="; ".join((a.get("family","")+" "+a.get("given","")[:1]) for a in (w.get("author") or [])[:6]))
for f in glob.glob("raw/s2_B*.json"):
    for w in json.load(open(f)): add(s2rec(w,"S2",f.split("s2_")[1][:2]))
for f in glob.glob("raw/cr_B*.json"):
    for w in json.load(open(f)): add(crrec(w,"CR",f.split("cr_")[1][:2]))
for w in json.load(open("raw/hand_journals.json")): add(crrec(w,"HAND","HS"))
if os.path.exists("raw/snowball.json"):
    for w in json.load(open("raw/snowball.json")): add(s2rec(w,"SNOW","SB"))
print("identified:",ident,"unique titles:",len(recs))
ctx=re.compile(r"\b(hous\w*|home\w*|residential|dwelling\w*|apartment\w*|condo\w*|real estate|realt\w*|propert\w*|mls|multiple listing|listing\w*|seller\w*|homeowner\w*|mortgage|land market)\b",re.I)
core=re.compile(r"time[- ]on[- ](the[- ])?market|\btom\b|days[- ]on[- ](the[- ])?market|\bdom\b|marketing (time|duration|period)|selling (time|duration|period)|time[- ]to[- ](sale|sell)|listing duration|duration of (listing|marketing)|probability of (a )?sale|withdraw\w*|relist\w*|re-list\w*|list(ing)? price|asking price|price (cut|reduction|revision|dispersion|discount)\w*|sale[s]?[- ]to[- ]list|list[- ]to[- ]sale|over[- ]?pric\w*|under[- ]?pric\w*|reservation price|liquidity|illiquid\w*|tightness|market heat|\bhot\b|\bcold\b|months.? (of )?(supply|inventory)|absorption rate|inventory|sales?[- ]to[- ]listings?|turnover|transaction volume|trading volume|sales volume|vacan\w*|search\w*|matching|bargaining|broker\w*|agent\w*|auction|foreclos\w*|seller motivation|anchoring|loss aversion",re.I)
noise=re.compile(r"\b(stock market|stock price|stocks?\b|equit(y|ies) market|bond\w*|REIT\w*|interbank|bank(ing)? liquidity|funding liquidity|liquidity (risk|creation|provision|premium)|monetary|central bank|crypto\w*|bitcoin|ETF|futures|options? market|derivative\w*|order book|bid-ask|labor market|labour market|unemploy\w*|hotel|tourism|hospital|patient|medical|clinical|cancer|drug|pharma\w*|electric\w*|energy market|oil|battery|wireless|sensor|neural|protein|soil|crop|wheat|cattle|livestock|fish\w*|forest\w*|carbon|emission|vehicle|automobile|airline|freight|supply chain|warehouse|manufactur\w*|semiconductor|smartphone|e-commerce|software)\b",re.I)
rows=[]
for k,r in recs.items():
    text=(r["title"] or "")+" || "+(r["abstract"] or ""); t=r["title"] or ""
    try: yr=int(r["year"] or 0)
    except: yr=0
    has_ctx=bool(ctx.search(text)); has_core=bool(core.search(text))
    has_noise=bool(noise.search(t)) and not re.search(r"hous|home|real estate|residential|propert",t,re.I)
    pre=is_preprint(r["doi"],r["venue"])
    if yr and yr<1986: dec,code="exclude","E5-year"
    elif has_noise: dec,code="exclude","E1-noise"
    elif not has_ctx: dec,code="exclude","E3-nocontext"
    elif not has_core: dec,code="exclude","E2-noindicator"
    elif pre and not r["doi"].startswith("10.1111") : dec,code="candidate-preprint","E4-check-journal-version"
    else: dec,code="candidate",""
    rows.append(dict(key=k,doi=r["doi"],title=t,year=yr,venue=r["venue"],authors=r["authors"],cites=r["cites"],ptypes=r["ptypes"],sources="|".join(sorted(r["sources"])),blocks="|".join(sorted(r["blocks"])),abstract=(r["abstract"] or "")[:1500],stageA=dec,codeA=code))
with open("merged_all.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
print(Counter(r["codeA"] or "candidate" for r in rows))
cand=[r for r in rows if r["stageA"].startswith("candidate")]
print("candidates:",len(cand)," with abstract:",sum(1 for r in cand if r["abstract"]), " from hand-search only:",sum(1 for r in cand if r["sources"]=="HAND"))
true_anchors={"10.1111/1540-6229.00463":"Haurin1988","10.1111/1540-6229.00514":"Kluger1990","10.1111/1540-6229.00691":"Forgey1996","10.1111/1540-6229.00038":"Knight2002","10.1023/a:1021526332732":"Anglin2003","10.1111/j.1540-6229.2007.00191.x":"LinVandell2007","10.1080/10835547.2007.12091978":"Johnson2007","10.1080/10835547.2008.12091217":"Clayton2008","10.1080/10835547.2010.12092027":"Sirmans2010","10.1016/j.jhe.2013.07.003":"An2013","10.1111/reec.12003":"Carrillo2013","10.1080/10835547.2014.12090387":"Benefield2014","10.1257/aer.104.4.1172":"Head2014","10.1257/aer.104.12.3991":"Ngai2014","10.1007/s11146-013-9450-z":"BenefieldHardin2015","10.1111/1540-6229.12082":"Carrillo2015","10.1016/j.jue.2016.03.008":"HanStrange2016","10.1111/1540-6229.12187":"vanDijkFrancke2017","10.1086/697207":"Guren2018","10.1016/j.jhe.2018.09.006":"Liu2019","10.1016/j.jhe.2022.101875":"BenShahar2022","10.1016/j.regsciurbeco.2024.103997":"vanDijk2024","10.1016/j.jhe.2025.102086":"Hayunga2025","10.1016/j.jhe.2025.102062":"Lin2025","10.1016/j.jhe.2026.102163":"Godinho2026","10.1080/10835547.2012.12092059":"MillerSklarz2012","10.1080/10835547.2013.12091364":"Beracha2013","10.1111/1756-2171.12022":"Tucker2013","10.1111/1540-6229.12121":"Dube2015","10.1016/j.jue.2012.01.002":"GenesoveHan2012","10.1111/iere.12019":"DiazJerez2013","10.1016/j.jhe.2010.03.002":"Cheng2010","10.1016/j.jhe.2013.01.003":"Haurin2013","10.1016/j.jhe.2014.09.001":"Maury2014","10.1016/j.jhe.2015.04.002":"Bian2015","10.1007/s11146-018-9657-0":"HayungaPace2019","10.1080/10835547.2013.12092086":"Filippova2014","10.1080/10527001.2020.1776513":"Chernobai2019","10.24957/hsr.2019.27.1.05":"Ko2019","10.21447/jup.2019.10.3.101":"Yang2019"}
bydoi={r["doi"]:r for r in rows if r["doi"]}
hit=[(n,bydoi[d]["stageA"]) for d,n in true_anchors.items() if d in bydoi]; miss=[n for d,n in true_anchors.items() if d not in bydoi]
print(f"anchor recall (true anchors): {len(hit)}/{len(true_anchors)}  missed: {miss}")
print("anchors not passing stage A:",[h for h in hit if not h[1].startswith("candidate")])
