# OSF Preregistration — Housing market liquidity indicators: a systematic review

> 아래 절 제목은 OSF Preregistration 양식의 칸 제목과 같다. 그대로 복사해 붙인다. 작성 2026-10-11.

## Title
Measuring housing market liquidity: a systematic review of indicator definitions, measurement choices and leading properties across MLS and non-MLS markets

## Authors
Seungbee Choi (Gachon University, PI); research team, Department of Urban Planning, Gachon University. Generative AI (Claude) was used for search execution, rule-based screening, first-pass title/abstract judgement and document drafting; all judgements are verified by two human readers and the PI (see Other).

## Description
Housing market liquidity is measured with many indicators (time on market, list-price adjustments, transaction volume, inventory, tightness, search-based indices) whose definitions vary across data environments. This review (i) catalogues indicator definitions, (ii) documents measurement choices (censoring, withdrawal, relisting, aggregation), (iii) synthesises evidence on their leading properties relative to prices and volumes, and (iv) compares indicator availability across MLS, non-MLS portal/brokerage and auction markets, with Korea as the principal non-MLS case. Target journal: Journal of Housing Economics.

## Hypotheses
H1 (ordering). Indicators that measure upstream stages of the transaction chain (demand/search signals S1, supply/listing S2) are reported to lead prices by longer horizons than indicators of downstream stages (matching S3, closing S4). H2 (measurement). Reported time-on-market–price elasticities differ systematically with censoring treatment (excluded vs survival/competing risk) and relisting treatment (reset vs cumulative). H3 (regime). In non-MLS markets, volume-, listing-count- and search-based indicators substitute for listing-level time measures; direct TOM evidence is sparse. These are descriptive hypotheses tested by structured synthesis (vote counting and tabulation), not by meta-analytic pooling.

## Design Plan
Study type: systematic review following PRISMA 2020. Blinding: not applicable. Existing data: literature search executed 2026-10-10 before this registration; title/abstract screening and the eligibility clarification (protocol v0.6, §4.4) are complete and documented with dates in the protocol change log (§13). Full-text eligibility assessment and data extraction have NOT started at registration.

## Sampling Plan
Information sources: Semantic Scholar bulk search, Crossref (28 phrase queries), Crossref ISSN hand-search of 16 core journals (1986–), Semantic Scholar forward citations of 5 seed papers, OpenAlex title/abstract Boolean search (blocks 1–3). Scopus, Web of Science, EconLit and KCI were not available at search time and will be run as supplementary searches; additions will be reported as a separate PRISMA row. Records: 52,006 identified; 37,104 after deduplication; 1,400 read at title/abstract; 438 passed; 148 meet the object-of-study criterion (§4.4) and form the synthesis set (attached CSV); 37 theory papers are background; 253 studies using an indicator only as an outcome of another factor form the evidence map (counts only). Eligibility: peer-reviewed journal articles, English or Korean, residential sales markets, 1986 onward; the liquidity indicator must be the object of study (C1 definition/measurement/index construction or C2 leading property/information content). Full-text exclusions will be coded E1 scope, E2 publication type, E3 indicator not object, E4 other.

## Variables
Study-level: bibliographic fields; country; spatial scale; period; market phase; institutional regime (MLS / non-MLS / auction); stage code S1–S5; function code F1–F3. Indicator-level (one row per indicator): verbatim definition with page; unit; start/end events; censoring; relisting and duplicate handling; aggregation; quality adjustment; data source; method family; endogeneity treatment; outcome variable; direction; verbatim effect size with page; lead–lag horizon and test; phase dependence. Quality appraisal: six items scored 0/1/2 (definition clarity, data transparency, censoring handling, endogeneity, robustness, reproducibility). Codebook: protocol/03_codebook.md.

## Analysis Plan
Tabulation and narrative synthesis organised by stage (S1→S5) and function (F1–F3), with institutional regime as a cross-cutting dimension. Table 1 corpus description (stage × regime × decade, 401 studies); Table 2 indicator definitions by stage; Table 3 measurement-issue matrix; Table 4 stage-ordered leading-property evidence (horizon, method, market); Table 5 substitute indicators in non-MLS markets (Korea). Evidence map heat map (stage × regime). Vote counting as auxiliary only; no effect-size pooling because definitions are heterogeneous. Sensitivity: results with and without 7 studies from journals whose indexing could not be confirmed. Inter-rater reliability: two human readers independently re-screen a random 10% of read records (140), all 47 uncertain records and all 142 first-round E2/E3 exclusions; Cohen's kappa reported; disagreements resolved by the PI. Students confirm or revise the stage/function/regime codes during extraction; the proportion changed and kappa are reported.

## Other
Protocol v0.7 (attached) and change log §13 record every criterion change with date and reason, including the 2026-10-10 clarification of the core eligibility condition from "indicator is a dependent, explanatory or constructed variable" to "indicator is the object of study", which reduced the title/abstract-passed set from 438 to a synthesis set of 148. Repository: github.com/csbee89/literature-review (private until submission; data and code to be deposited with the paper). Generative AI use is logged in students/ai_use_log.md and will be declared per the journal's policy.
