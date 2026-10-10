import json,urllib.request,urllib.parse,time,sys,os
KEY=os.environ["OA_KEY"]
CTX='(housing OR house OR houses OR home OR homes OR residential OR dwelling OR apartment OR condominium OR "real estate" OR MLS OR "multiple listing")'
BLOCKS={
"B1":[f'("time on the market" OR "time on market" OR "days on market" OR "marketing time" OR "marketing duration" OR "selling time" OR "time to sale" OR "listing duration" OR "probability of sale" OR relisting OR "withdrawn listings" OR "listing withdrawal") AND {CTX}'],
"B2":[f'("list price" OR "listing price" OR "asking price" OR "price cut" OR "price cuts" OR "price reduction" OR "price revision" OR "sale-to-list" OR "list-to-sale" OR overpricing OR "degree of overpricing" OR "price dispersion" OR "reservation price") AND {CTX} AND (liquidity OR "time on the market" OR "time on market" OR "days on market" OR "selling time" OR "probability of sale" OR "marketing time" OR "time to sale" OR seller OR sellers)'],
"B3":[f'("housing market liquidity" OR "housing liquidity" OR "real estate liquidity" OR "property market liquidity" OR "liquidity index" OR "liquidity indices" OR "market tightness" OR "hot market" OR "cold market" OR "hot and cold" OR "months of inventory" OR "months supply" OR "absorption rate" OR "inventory age" OR "sales-to-listings" OR "housing turnover" OR "transaction volume" OR "sales volume" OR "trading volume") AND {CTX} NOT (stock OR stocks OR bond OR bonds OR REIT OR REITs OR interbank OR "funding liquidity" OR monetary OR cryptocurrency)'],
}
log=open("raw/oa_log.txt","a"); 
for blk,qs in BLOCKS.items():
    rows=[]
    for q in qs:
        cursor="*"; n=0; total=None
        while True:
            params={"filter":f"title_and_abstract.search:{q},type:article,from_publication_date:1986-01-01","per-page":200,"cursor":cursor,"select":"id,doi,title,publication_year,primary_location,authorships,cited_by_count,abstract_inverted_index,language","api_key":KEY}
            url="https://api.openalex.org/works?"+urllib.parse.urlencode(params)
            for a in range(5):
                try: d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"slr (mailto:csbee89@gmail.com)"}),timeout=120)); break
                except Exception as e: print("retry",a,blk,e,file=sys.stderr); time.sleep(5*(a+1))
            else: d={"results":[]}
            total=total or (d.get("meta") or {}).get("count")
            res=d.get("results",[])
            for w in res:
                inv=w.get("abstract_inverted_index") or {}
                words={}
                for tok,pos in inv.items():
                    for p in pos: words[p]=tok
                w["abstract"]=" ".join(words[k] for k in sorted(words)) if words else ""
                w.pop("abstract_inverted_index",None)
            rows.extend(res); n+=len(res); cursor=(d.get("meta") or {}).get("next_cursor")
            if not cursor or not res: break
            time.sleep(0.3)
        msg=f"{time.strftime('%Y-%m-%d')} | OpenAlex title_and_abstract.search | {blk} | total={total} fetched={n} | {q}"; print(msg); log.write(msg+"\n")
    json.dump(rows,open(f"raw/oa_{blk}.json","w"),ensure_ascii=False)
