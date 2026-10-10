import csv,json,urllib.request,urllib.parse,time,re,html,difflib,sys
def nt(t): t=html.unescape(t or "").lower(); t=re.sub(r"[^a-z0-9 ]"," ",t); return re.sub(r"\s+"," ",t).strip()
rows=list(csv.DictReader(open("screened.csv",encoding="utf-8")))
todo=[r for r in rows if r["decision"] in ("V","M") or (r["decision"]=="I" and (not r["doi"] or re.search(r"ssrn|10\.3386|arxiv",r["doi"])))]
print("to resolve:",len(todo),file=sys.stderr)
out=[]
for r in todo:
    q=re.sub(r"\(Supplementary material\)|\*$","",r["title"])
    url="https://api.crossref.org/works?"+urllib.parse.urlencode({"query.title":q,"filter":"type:journal-article","rows":4,"select":"DOI,title,container-title,issued,author","mailto":"csbee89@gmail.com"})
    best=None
    try:
        items=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"slr-resolve (mailto:csbee89@gmail.com)"}),timeout=60))["message"]["items"]
        for it in items:
            t=(it.get("title") or [""])[0]; s=difflib.SequenceMatcher(None,nt(q),nt(t)).ratio()
            fa=(it.get("author") or [{}])[0].get("family","")
            if best is None or s>best["score"]:
                best=dict(score=round(s,3),doi=it["DOI"].lower(),jtitle=t,venue=(it.get("container-title") or [""])[0],year=((it.get("issued") or {}).get("date-parts") or [[None]])[0][0],first_author=fa)
    except Exception as e: print("ERR",r["rid"],e,file=sys.stderr)
    r2=dict(rid=r["rid"],decision=r["decision"],note=r["note"],title=r["title"],year=r["year"],venue=r["venue"],doi=r["doi"],authors=r["authors"])
    r2.update({("cr_"+k):v for k,v in (best or {}).items()})
    out.append(r2); time.sleep(1.0)
with open("resolved.csv","w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(f"{r['rid']}|{r['decision']}|{str(r.get('cr_score',''))}|{r['title'][:60]}|=>|{str(r.get('cr_jtitle',''))[:55]}|{str(r.get('cr_venue',''))[:35]}|{r.get('cr_year','')}|{r.get('cr_doi','')}")
