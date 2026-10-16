# 작업 상태 요약 (다른 Claude 세션·학생이 처음 열 때 읽는 파일)

**프로젝트**: 주택시장 유동성 지표 체계적 문헌고찰 → Journal of Housing Economics (JCR Q1 Economics) 투고.
**연구책임자** 최승비(가천대) · **수합·운영** 이원석(학부 3) · 연구실 8명: 전우성(박사), 손수연·최찬미(석사), 이원석·이다윤(학부 3), 오건·이지은·홍다연(학부 2).

## 지금 어디까지 왔나 (2026-10-13, 프로토콜 v0.7.3)
1. 범위 '좁게': 동료심사 학술지만, 영어·한국어, 주거용 매매시장만. **핵심 조건(§4.4)**: 유동성 지표가 연구의 *대상*(C1 측정·정의·지수 / C2 선행성·정보내용)이어야 한다. 지표를 결과변수로만 쓴 연구는 증거지도, 이론은 배경.
2. 검색·선별: 5경로 52,006건 → 37,104건 중복 제거 → 1,400건 판독 → 제목·초록 통과 438편 → **§4.4 적용: 종합 148편** / 배경 37 / 증거지도 253 (`review/included_studies.csv`의 `scope` 열, 수치 `review/prisma_flow.md` §3b).
3. 종합 148편 = A 37 · B 27 · C 68 · D 16, 한국 관련 28. **연구책임자 승인 완료(2026-10-11, O/X 페이지 전부 O)**. 목록 `review/synthesis_set.md`·`.csv`.
3b. **분류 틀 확정(§3.1)**: 주축 = 거래 사슬 단계 S1 수요·관심 25 / S2 공급·호가 16 / S3 매칭 39 / S4 체결 52 / S5 집계 상태 16; 부축 = 기능 F1 정의·구축 39 / F2 측정 쟁점 26 / F3 선행성·관계 83; 교차 = 제도환경 MLS 53 / 비MLS 87 / 경매 4 / 복수 4. 대안 비교 `review/framework_alternatives.md`. 초기 코드는 `synthesis_set.csv`, 학생이 추출 시 확인.
4. **운영(v11, 연구책임자 결정 10/13): 청년 주거경로 리뷰와 같은 방식.** 모든 논문 같은 양식 = 워드 1쪽(`handover/word/논문정리_양식_v1.docx`: 서지·1.분류·2.요약·3.저자 한계·4.막힌 것) + 구글시트 지표마다 1행(`handover/유동성리뷰_추출시트_양식.xlsx`, `scripts/build_sheet_template.py`). 예시 `handover/word/예시_p115_마승렬2021.docx`·`예시_p033_Liu2024.docx`(Claude 작성, 배정 제외, `scripts/make_word.js`). 파일럿·긴/짧은 구분·짝 점검 폐지(프로토콜 v0.7.3 §8.1): **독립 이중 추출** = Claude 1차(원문 PDF) + 학생 2차, Claude가 매주 대조표, 불일치는 연구책임자 판정(코드북 §H). 원석은 Claude 1차를 보지 않는다. **10/19(월) W1 배포 → 10/28(수) 첫 모임, 이후 매주 수요일 모임**(모임에서 배정, 전날 화 18:00 마감; 배정표 `meeting` 열). W1~W5 1인 1편(청년 리뷰 10/21~11/24와 겹침), W6부터 2편 → 146편 12주(마지막 마감 2027-01-12). `scripts/assign.py` v7 `--meet 2026-10-28 --w1 2026-10-19 --ramp 1x5,2`(3편이면 `1x5,3`, 12/29). 순서: 한국 관련 27편(W1~W4) → 영문 S3→S2→S5→S4→S1. 배정표 `students/assignments.csv`, 사람별 `students/schedule_by_person.md`, 운영 `students/assignment_brief.md`, 학생 안내 `students/how_to_summarize.md`. 담당자 엑셀 `handover/유동성리뷰_담당자파일.xlsx`(`scripts/build_handover_xlsx.py` 후 recalc). 원문 `papers/` 35편 + `papers/pdf_status.csv`. **원석 역할: 없는 원문 받아 수요일 배포, 화요일 제출·빈칸·쪽수 확인, 엑셀 입력, 본인 논문.**

## 구글 드라이브 (2026-10-16, 연구책임자 가천 계정 sbchoi@gachon.ac.kr)
폴더 「주택시장 유동성 지표 리뷰」 https://drive.google.com/drive/folders/1xFmziqQo3t2tJhA1tvp_HnGt9Jt05X-d — 00_먼저 읽기(원석 운영 안내), 01_학생 안내, 02_논문정리 양식, 03·04_예시(p115·p033), 05_추출시트(공용), 06_주차별 배정(원석 확인 칸), 07_AI 사용 기록, 「원문」 하위 폴더(비어 있음; PDF는 커넥터로 못 올림 → 연구책임자에게 zip 2개 전달). 저장소 파일이 원본, 드라이브는 운영본. 바꾸면 둘 다 고친다.

## 리뷰 시작 전 반드시 끝낼 것 (순서대로)
1. [x] 연구책임자: 148편 승인(2026-10-11, 전부 O).
2. [x] 분류 틀 확정, 코드북 §G, 배정표에 단계·기능·환경 코드 반영.
3. [x] 프로토콜 동결(2026-10-13, `protocol/FREEZE.md`). OSF 등록은 **선택**(연구책임자 판단 보류): 하지 않으면 PRISMA 항목 24에 미등록 + 저장소 동결 일자로 기재, 프로토콜은 부록 S1로 제출. 하려면 `osf/README.md`.
4. [x] 배정표 실명(2026-10-13): 전우성(박사), 손수연·최찬미(석사), 이원석·이다윤(학부 3), 오건·이지은·홍다연(학부 2). 사람별 일정 `students/schedule_by_person.md`. **10/19(월) 첫 배포, 10/28(수) 첫 모임.**
**확정까지는 연구책임자가 직접 한다(2026-10-13 지시).** 원석은 W1부터 주간 운영만.
4a. [ ] **연구책임자: Scopus·WoS 보완 검색** — Claude는 기관 인증이 없어 직접 못 함(API 401 확인, 2026-10-13). 연구책임자가 학교 계정으로 `search/scopus_wos_guide.md`의 식 6개를 붙여 넣고 내보내 `search/supp/`에 올리면 Claude가 `scripts/import_scopus_wos.py`로 중복 제거·규칙 선별·판독.
4b. [ ] 연구책임자: 워드 예시 p115·p033 원문 대조 확인. 원석: 남은 원문 확보·배포(W1은 10/19, 한국 5편 p025·p035·p058·p063·p128 먼저), 구글 드라이브 공용 폴더·시트. Claude: 원문 들어오는 대로 1차 추출(학생과 비공유, `review/claude_first/`). W1 p023·p129·p074 진행.
5. [ ] 연구책임자 + 손수연(석사): 선별 재판독(무작위 140 + I? 47 + 1차 E2·E3 142), κ 보고. 리뷰 시작과 병행 가능.

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
- `papers/` 원문 35편 + `pdf_status.csv`(148편 원문 받는 법)
- `students/` 운영 계획(v11), 학생용 정리 안내 `how_to_summarize.md`, 배정표, 주간 보고 양식, AI 사용 기록
- `handover/word/` 워드 양식·예시(p115 한국, p033 영문) · `handover/유동성리뷰_추출시트_양식.xlsx` 구글시트 양식 · `examples/`·`templates/` 이전 md 양식(v10까지, 참고용), 추출 CSV(코드북 열)

## 규칙
원문에 없는 것은 쓰지 않는다(`NR`). 인용은 DOI로 실존 확인. 지표마다 1행. AI 사용은 `students/ai_use_log.md`에 기록(JHE 선언 요건). API 키·비밀은 커밋하지 않는다.
