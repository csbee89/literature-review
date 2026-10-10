import json,urllib.request,urllib.parse,time,sys
PHRASES={
 "B1":['"time on the market" housing','"time on market" housing','"days on market" housing','"marketing time" housing sale','"selling time" housing','"time to sale" housing','"probability of sale" housing','relisting housing market','"withdrawn" listings housing market'],
 "B2":['"list price" "time on market" housing','"listing price" housing liquidity','"asking price" housing "time on market"','"price cut" housing listing','"price reduction" housing listing market','"sale-to-list" ratio housing','overpricing housing "time on market"','"price dispersion" housing market'],
 "B3":['"housing market liquidity"','"housing liquidity"','"real estate liquidity" residential','"liquidity index" housing market','"market tightness" housing','"hot and cold" housing market','"months of inventory" housing','"months supply" housing market','"absorption rate" housing','"turnover" housing market transactions','"transaction volume" housing market'],
}
log=open("raw/cr_log.txt","a"); 
for blk,ph in PHRASES.items():
    allrows=[]
    for q in ph:
        rows=[];cursor="*"
        for page in range(3):  # up to 3x200 = 600 per phrase, relevance-ranked
            url="https://api.crossref.org/works?"+urllib.parse.urlencode({"query.bibliographic":q,"filter":"from-pub-date:1986-01-01,type:journal-article","rows":200,"cursor":cursor,"select":"DOI,title,author,issued,container-title,ISSN,type,is-referenced-by-count,abstract","mailto":"csbee89@gmail.com"})
            try:
                d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"slr-search (mailto:csbee89@gmail.com)"}),timeout=90))["message"]
            except Exception as e:
                print("ERR",q,e,file=sys.stderr); time.sleep(5); break
            items=d.get("items",[]); rows.extend(items); cursor=d.get("next-cursor")
            if len(items)<200: break
            time.sleep(1.0)
        for r in rows: r["_query"]=q
        allrows.extend(rows)
        msg=f"{time.strftime('%Y-%m-%d')} | Crossref | {blk} | {q} | fetched={len(rows)}"; print(msg); log.write(msg+"\n"); time.sleep(1.0)
    json.dump(allrows,open(f"raw/cr_{blk}.json","w"),ensure_ascii=False)
