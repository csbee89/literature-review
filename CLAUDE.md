# 작업 상태 요약 (다른 Claude 세션·학생이 처음 열 때 읽는 파일)

**프로젝트**: 주택시장 유동성 지표 체계적 문헌고찰 → Journal of Housing Economics (JCR Q1 Economics) 투고.
**연구책임자** 최승비(가천대) · **수합·운영** 이원석(학부 3) · 연구실 8명(박사1 석사2 학부5).

## 지금 어디까지 왔나 (2026-10-10)
1. 프로토콜 v0.3 확정(`protocol/01_protocol.md`): 범위 '좁게' — 동료심사 학술지만, 영어·한국어, 주거용 매매시장만.
2. **검색·선별 완료**: 48,608건 식별 → 35,397건 중복 제거 → 규칙 선별 → 844건 판독 → **340편 포함** (`review/included_studies.csv`, 흐름도 수치 `review/prisma_flow.md`).
3. 포함 340편 = core 216 / peripheral 96 / theory 28. 전수 완전추출은 8명 체제로 19~23주. **연구책임자 결정 대기**(아래).
4. 배정표: `students/assignments.csv`(W1~W4 공통 44편), `students/assignments_option1.csv`, `students/assignments_option3.csv`.

## 연구책임자 결정 대기
- [ ] 코퍼스 운영안 선택: 옵션1(core+theory 244편 완전추출, 23주) / 옵션3(지표 중심 208편 완전추출 + 132편 경량추출, 19주) / 연도 하한(2000~ 또는 2005~) 추가 / 주당 편수 상향
- [ ] 저널 색인 기준 추가 여부(Scopus·WoS·KCI 색인 학술지만) — 저품질 추정 6편 처리
- [ ] AI 보조 선별의 인간 재판독 범위 승인(기본안: 무작위 10% + I? 15편 + E2·E3 142편)
- [ ] OpenAlex API 키(무료) 발급, KCI OpenAPI 키 발급, Scopus·WoS 접속 확인 → 보완 검색

## 파일 지도
- `protocol/` 프로토콜·검색식·코드북·저널 비교·JHE 제약표
- `review/` 포함 목록, 판독 로그(844), 전체 레코드(35,397), PRISMA 수치, 선별 규칙, 선행 리뷰
- `scripts/` 검색(s2/cr/hand/snowball) → 병합(merge2) → 규칙선별(stageB) → 게재본 확인(resolve) → 편집(compile) → 배정(assign)
- `students/` 운영 계획, 배정표, 주간 보고 양식, AI 사용 기록
- `examples/` 정리 수준 기준 예시(Famiglietti 2020)
- `templates/` 추출 CSV, 1쪽 양식, 선별·검색 로그

## 규칙
원문에 없는 것은 쓰지 않는다(`NR`). 인용은 DOI로 실존 확인. 지표마다 1행. AI 사용은 `students/ai_use_log.md`에 기록(JHE 선언 요건).
