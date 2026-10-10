import json,urllib.request,urllib.parse,time,sys
J={"Real Estate Economics":"1080-8620","AREUEA Journal":"0270-0484","J Real Estate Finance & Economics":"0895-5638","Journal of Housing Economics":"1051-1377","Journal of Urban Economics":"0094-1190","Regional Science and Urban Economics":"0166-0462","Journal of Housing Research":"1052-7001","Journal of Real Estate Research":"0896-5803","Housing Studies":"0267-3037","Int J Housing Markets and Analysis":"1753-8270","Journal of Property Research":"0959-9916","Journal of Real Estate Literature":"0927-7544","Housing Policy Debate":"1051-1482","Journal of Housing and the Built Environment":"1566-4910","Urban Studies":"0042-0980","Journal of European Real Estate Research":"1753-9269","International Real Estate Review":"1029-6131","Real Estate Management and Valuation":"2300-5289"}
log=open("raw/hand_log.txt","a"); out=[]
for name,issn in J.items():
    cursor="*"; n=0
    while True:
        url="https://api.crossref.org/journals/%s/works?"%issn+urllib.parse.urlencode({"filter":"from-pub-date:1986-01-01,type:journal-article","rows":1000,"cursor":cursor,"select":"DOI,title,author,issued,container-title,is-referenced-by-count,abstract","mailto":"csbee89@gmail.com"})
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"slr-handsearch (mailto:csbee89@gmail.com)"}),timeout=120))["message"]
        except Exception as e: print("ERR",name,e,file=sys.stderr); time.sleep(5); break
        items=d.get("items",[]); 
        for it in items: it["_journal"]=name
        out.extend(items); n+=len(items); cursor=d.get("next-cursor")
        if len(items)<1000: break
        time.sleep(1.0)
    msg=f"{time.strftime('%Y-%m-%d')} | Crossref journal hand-search | {name} ({issn}) | fetched={n}"; print(msg); log.write(msg+"\n"); time.sleep(0.8)
json.dump(out,open("raw/hand_journals.json","w"),ensure_ascii=False); print("total",len(out))
