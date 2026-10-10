# 주택시장 유동성 지표 체계적 문헌고찰 (Systematic Review of Housing Market Liquidity Indicators)

2026 신진연구(유형A) 「AI 기반 주택시장 유동성 조기경보 시스템 개발」 1차년도 — 문헌고찰 작업 저장소.
연구책임자 최승비(가천대 도시계획전공). 참여 학생연구원 공동 작업.

**현재 상태(2026-10-10)**: 검색·선별 완료(OpenAlex 보완 포함), **438편 포함**. 운영안은 옵션3으로 확정(`CLAUDE.md`). 포함 목록 `review/included_studies.csv`.

## 작업 순서 (이 순서대로)

1. `protocol/01_protocol.md` (타겟 저널 판단은 `protocol/04_target_journal_q1.md`) — 리뷰 질문·범위·적격기준·선별·추출·종합·일정·역할. **검색 시작 전에 확정하고 OSF에 등록.**
2. `protocol/02_search_strings.md` — DB별 검색식. 실행마다 `templates/search_log.csv`에 기록.
3. `seed/seed_list.md` — 앵커 문헌 60여 편(실존 검증 완료). 검색식 회수율 점검과 스노볼링 출발점.
4. `templates/screening_log.csv` + `templates/exclusion_codes.md` — 2인 독립 선별 기록. `scripts/slr_tools.py kappa`로 일치도.
5. `templates/one_pager_template.md` → `templates/extraction_form.csv` — 문헌 1쪽 정리는 이 양식만. 코딩 규칙은 `protocol/03_codebook.md`.
6. 종합: 증거지도, 측정 쟁점 매트릭스, 선행성 표 (프로토콜 §10).

## 폴더

| 폴더 | 내용 |
|---|---|
| `protocol/` | 프로토콜, 검색식, 코드북, 타겟 저널 비교(04), **JHE 제약표(05)** |
| `manuscript/` | 리뷰 원고 뼈대 (JHE 제약 헤더 포함). 집필 순서: 3장 → 4장 → 1장 → 2장 → 5장 → 초록 → Highlights |
| `examples/` | **정리 수준의 기준 예시**(Famiglietti et al. 2020 전문 PDF + 1쪽 정리) |
| `templates/` | 검색 로그, 선별 로그, 제외 코드, 추출 양식, 학생용 1쪽 양식 |
| `seed/` | 앵커 문헌 목록, 검증 리포트, JHE 게재 인용 후보 15편 |
| `review/` | **포함 438편, 판독 로그(844+556), PRISMA 수치, 선별 규칙, 선행 리뷰** |
| `scans/` | 2026-10-06 Crossref 스코핑 스캔 3축(약 600편) + `journals/` 후보 저널 8종 게재 지형 |
| `students/` | **운영 계획(assignment_brief v3)**, 주차별 배정표(assignments.csv), 주간 보고 양식, AI 사용 기록, 정리 예시 피드백, 아이디어 로그 |
| `reports/` | 주간 보고 (`W01_이름.md`) |
| `extraction/` · `analysis/` | 문헌 1쪽 정리 / 데이터 분석 과제 (섞지 않는다) |
| `scripts/` | `slr_tools.py` — dedupe / kappa / openalex 검색 로그 |

## 도구

- 서지 관리: **Zotero 그룹 라이브러리**(필수). DOI로 가져오기. PDF 첨부.
- 선별: Rayyan(무료) 또는 ASReview(오픈소스). 결정은 `screening_log.csv`로도 내보내 저장.
- 인용 검증: sb-paper 스킬 `scripts/verify_citations.py` (Crossref/OpenAlex; 국문은 KCI OpenAPI 키 필요).

## 규칙 세 줄

1. 원문에 없는 것은 쓰지 않는다. 비면 `NR`, 못 확인하면 `[확인 필요]`, 인용 미검증은 `[미검증]`.
2. 지표 정의는 원문을 그대로 인용하고 쪽수를 적는다.
3. 분석 단위는 논문이 아니라 **지표**다. 지표마다 한 행.
