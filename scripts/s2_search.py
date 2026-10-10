import json,urllib.request,urllib.parse,time,sys,csv
CTX='(housing | house | houses | home | homes | residential | dwelling | dwellings | apartment | apartments | condominium | "real estate" | property | MLS | "multiple listing")'
BLOCKS={
 "B1_tom": '("time on the market" | "time on market" | "time-on-market" | "time-on-the-market" | "days on market" | "days-on-market" | "marketing time" | "marketing duration" | "marketing period" | "selling time" | "time to sale" | "time-to-sale" | "listing duration" | "probability of sale" | "withdrawn listing" | "withdrawn listings" | relisting | "re-listing" | "listing survival") + '+CTX,
 "B2_list": '("list price" | "listing price" | "asking price" | "price cut" | "price cuts" | "price reduction" | "price reductions" | "price revision" | "price revisions" | "sale-to-list" | "sales-to-list" | "list-to-sale" | overpricing | "degree of overpricing" | underpricing | "price dispersion" | "reservation price") + '+CTX+' + (liquidity | "time on the market" | "time on market" | "days on market" | "selling time" | "probability of sale" | "marketing time" | "time to sale")',
 "B3_liq": '("housing market liquidity" | "housing liquidity" | "real estate liquidity" | "property market liquidity" | "liquidity index" | "liquidity indices" | "liquidity measure" | "liquidity measures" | "market tightness" | "market heat" | "hot market" | "hot markets" | "cold market" | "cold markets" | "hot and cold" | "months of inventory" | "months supply" | "months\' supply" | "absorption rate" | "inventory age" | "sales-to-listings" | "sale-to-inventory" | "turnover rate" | "transaction volume" | "trading volume" | "sales volume" | "liquidity-adjusted" | "constant-liquidity" | "variable liquidity") + '+CTX+' - (stock | stocks | bond | bonds | REIT | REITs | interbank | "funding liquidity" | monetary | "central bank" | crypto | cryptocurrency | "bid-ask" | "order book")',
}
FIELDS="title,year,venue,publicationVenue,externalIds,abstract,publicationTypes,citationCount,authors,journal"
log=open("raw/s2_log.txt","a")
for name,q in BLOCKS.items():
    rows=[];token=None;pages=0
    while True:
        params={"query":q,"fields":FIELDS,"year":"1986-"}
        if token: params["token"]=token
        url="https://api.semanticscholar.org/graph/v1/paper/search/bulk?"+urllib.parse.urlencode(params)
        for attempt in range(6):
            try:
                d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"slr-search (mailto:csbee89@gmail.com)"}),timeout=90)); break
            except Exception as e:
                print(name,"retry",attempt,e,file=sys.stderr); time.sleep(8*(attempt+1))
        else:
            d={"data":[]}
        rows.extend(d.get("data",[])); pages+=1
        total=d.get("total")
        token=d.get("token")
        if not token or pages>=12: break
        time.sleep(1.5)
    json.dump(rows,open(f"raw/s2_{name}.json","w"),ensure_ascii=False)
    msg=f"{time.strftime('%Y-%m-%d')} | SemanticScholar bulk | {name} | total={total} fetched={len(rows)} | {q}"
    print(msg); log.write(msg+"\n"); time.sleep(2)
