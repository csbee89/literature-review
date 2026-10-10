import json,urllib.request,urllib.parse,time,sys
F="title,year,venue,externalIds,abstract,publicationTypes,citationCount,authors"
def get(url):
    for a in range(5):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"slr-snowball (mailto:csbee89@gmail.com)"}),timeout=90))
        except Exception as e: print("retry",a,url[:80],e,file=sys.stderr); time.sleep(6*(a+1))
    return {}
def pull(kind,doi):
    rows=[];off=0
    while True:
        d=get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}/{kind}?"+urllib.parse.urlencode({"fields":F,"limit":1000,"offset":off}))
        data=d.get("data") or []
        if not data and off==0: print("no data for",kind,doi,str(d)[:120],file=sys.stderr)
        
        for x in data:
            p=x.get("citedPaper") if kind=="references" else x.get("citingPaper")
            if p: p["_via"]=f"{kind}:{doi}"; rows.append(p)
        if "next" not in d or not data: break
        off=d["next"]; time.sleep(1.2)
    time.sleep(1.2); return rows
back=["10.1080/10835547.2010.12092027","10.1080/10835547.2014.12090387","10.1016/B978-0-444-59531-7.00013-2","10.1007/s11146-013-9450-z"]  # Sirmans2010, Benefield2014 review, Han&Strange2015, Benefield&Hardin2015
fwd=["10.1111/1540-6229.00514","10.1111/1540-6229.00463","10.1111/reec.12003","10.1016/j.regsciurbeco.2024.103997","10.1111/1540-6229.00038","10.1007/s11146-013-9450-z","10.1080/10835547.2010.12092027"]  # Kluger&Miller, Haurin, Carrillo2013, vanDijk2024, Knight2002, Benefield&Hardin2015, Sirmans2010
out=[]; log=open("raw/snow_log.txt","a")
for d in back:
    r=pull("references",d); out+=r; m=f"{time.strftime('%Y-%m-%d')} | S2 backward | {d} | n={len(r)}"; print(m); log.write(m+"\n")
for d in fwd:
    r=pull("citations",d); out+=r; m=f"{time.strftime('%Y-%m-%d')} | S2 forward | {d} | n={len(r)}"; print(m); log.write(m+"\n")
json.dump(out,open("raw/snowball.json","w"),ensure_ascii=False); print("total",len(out))
