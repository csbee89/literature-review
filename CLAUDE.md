# 작업 상태 요약 (다른 Claude 세션·학생이 처음 열 때 읽는 파일)

**프로젝트**: 주택시장 유동성 지표 체계적 문헌고찰 → Journal of Housing Economics (JCR Q1 Economics) 투고.
**연구책임자** 최승비(가천대) · **수합·운영** 이원석(학부 3) · 연구실 8명(박사1 석사2 학부5).

## 지금 어디까지 왔나 (2026-10-13, 프로토콜 v0.7.1)
1. 범위 '좁게': 동료심사 학술지만, 영어·한국어, 주거용 매매시장만. **핵심 조건(§4.4)**: 유동성 지표가 연구의 *대상*(C1 측정·정의·지수 / C2 선행성·정보내용)이어야 한다. 지표를 결과변수로만 쓴 연구는 증거지도, 이론은 배경.
2. 검색·선별: 5경로 52,006건 → 37,104건 중복 제거 → 1,400건 판독 → 제목·초록 통과 438편 → **§4.4 적용: 종합 148편** / 배경 37 / 증거지도 253 (`review/included_studies.csv`의 `scope` 열, 수치 `review/prisma_flow.md` §3b).
3. 종합 148편 = A 37 · B 27 · C 68 · D 16, 한국 관련 28. **연구책임자 승인 완료(2026-10-11, O/X 페이지 전부 O)**. 목록 `review/synthesis_set.md`·`.csv`.
3b. **분류 틀 확정(§3.1)**: 주축 = 거래 사슬 단계 S1 수요·관심 25 / S2 공급·호가 16 / S3 매칭 39 / S4 체결 52 / S5 집계 상태 16; 부축 = 기능 F1 정의·구축 39 / F2 측정 쟁점 26 / F3 선행성·관계 83; 교차 = 제도환경 MLS 53 / 비MLS 87 / 경매 4 / 복수 4. 대안 비교 `review/framework_alternatives.md`. 초기 코드는 `synthesis_set.csv`, 학생이 추출 시 확인.
4. **운영(v8, 연구책임자 지시 10/13): 8명 전원 매주 1편.** W1 파일럿(8명이 같은 논문 p023) → W2~W5 한국 논문 26편 → W5~W20 영문, 단계 순 S3→S2→S5→S4→S1. 2026-10-19 시작, 2027-03-05 종료(20주). p115는 Claude가 정리 예시로 완료(`examples/example_Ma2021_p115.md`, 원석 검증). 배정표 `students/assignments.csv`(`scripts/assign.py` v4). 담당자 엑셀 `handover/유동성리뷰_담당자파일.xlsx`(`scripts/build_handover_xlsx.py`로 재생성 후 recalc). 원문 `papers/`(OA 15편) + 상태표 `papers/pdf_status.csv`.

## 리뷰 시작 전 반드시 끝낼 것 (순서대로)
1. [x] 연구책임자: 148편 승인(2026-10-11, 전부 O).
2. [x] 분류 틀 확정, 코드북 §G, 배정표에 단계·기능·환경 코드 반영.
3. [x] 프로토콜 동결(2026-10-13, `protocol/FREEZE.md`). OSF 등록은 **선택**(연구책임자 판단 보류): 하지 않으면 PRISMA 항목 24에 미등록 + 저장소 동결 일자로 기재, 프로토콜은 부록 S1로 제출. 하려면 `osf/README.md`.
4. [ ] 연구책임자: 배정표 실명. **첫 회의 10/19(월)부터 리뷰 시작.**
4a. [ ] **원석: Scopus·WoS 보완 검색** — Claude는 기관 인증이 없어 직접 못 함(API 401 확인, 2026-10-13). 원석이 학교 계정으로 `search/scopus_wos_guide.md`의 식 6개를 붙여 넣고 내보내 `search/supp/`에 올리면 Claude가 `scripts/import_scopus_wos.py`로 중복 제거·규칙 선별·판독.
4b. [ ] 원석(10/13~16): 파일럿 p023 원문 KCI에서 받아 배포(안 되면 `--pilot p025`), W2·W3 한국 16편 원문, 예시 p115 원문 대조 검증, Zotero 148편.
5. [ ] 원석·석사①: 인간 재판독(무작위 140 + I? 47 + 1차 E2·E3 142) — 리뷰 시작과 병행 가능.

## 연구책임자가 위임해 Claude가 내린 결정
- 저널 색인 기준 추가하지 않음. 저품질 추정 저널 논문은 `low-tier` 표시 → 민감도 분석.
- OpenAlex 보완 검색 완료(키는 환경변수 `OA_KEY`로만, 저장소에 쓰지 않음).
- v0.5의 옵션1/3·경량추출 체계는 폐기(기준 불일치의 산물).

## 파일 지도
- `protocol/` 프로토콜(v0.7, 동결 기록 FREEZE.md)·검색식·코드북·저널 비교·JHE 제약표
- `search/scopus_wos_guide.md` Scopus·WoS 실행 안내(붙여 넣을 식, 내보내기 방법), `scripts/import_scopus_wos.py` 가져오기·중복 제거
- `osf/` OSF 사전등록 묶음(README 7단계, preregistration.md, 148편 CSV)
- `review/` 포함 목록(438, scope·stage·function·regime 열), 종합 목록 `synthesis_set.md/.csv`(승인 완료), 분류 틀 대안 비교 `framework_alternatives.md`, 판독 로그(844 + OpenAlex 556), 전체 레코드, PRISMA 수치, 선별 규칙, 선행 리뷰
- `scripts/` 검색(s2/cr/hand/snowball/oa_search) → 병합 → 규칙선별 → 게재본 확인 → 편집(compile) → 배정(assign `[--grad N]`)
- `handover/` 담당자 엑셀(7개 시트: 안내·종합148·주차별배정·진행현황·분류틀·선별과정·전체438)
- `papers/` 오픈액세스 원문 15편 + `pdf_status.csv`(148편 원문 받는 법)
- `students/` 운영 계획(v8), 배정표, 주간 보고 양식, AI 사용 기록
- `examples/` 정리 예시: 한국 논문 p115(마승렬 2021), 영문 Famiglietti 2020 · `templates/` 추출 CSV, 1쪽 양식, 선별·검색 로그

## 규칙
원문에 없는 것은 쓰지 않는다(`NR`). 인용은 DOI로 실존 확인. 지표마다 1행. AI 사용은 `students/ai_use_log.md`에 기록(JHE 선언 요건). API 키·비밀은 커밋하지 않는다.
