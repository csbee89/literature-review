# 작업 상태 요약 (다른 Claude 세션·학생이 처음 열 때 읽는 파일)

**프로젝트**: 주택시장 유동성 지표 체계적 문헌고찰 → Journal of Housing Economics (JCR Q1 Economics) 투고.
**연구책임자** 최승비(가천대) · **수합·운영** 이원석(학부 3) · 연구실 8명(박사1 석사2 학부5).

## 지금 어디까지 왔나 (2026-10-10)
1. 프로토콜 v0.5(`protocol/01_protocol.md`): 범위 '좁게' — 동료심사 학술지만, 영어·한국어, 주거용 매매시장만.
2. **검색·선별 완료**: 5경로 52,006건 식별 → 37,104건 중복 제거 → 규칙 선별 → 1,400건 판독(844 + OpenAlex 556) → **438편 포함** (`review/included_studies.csv`, 수치 `review/prisma_flow.md`).
3. 포함 438편 = core 297 / peripheral 104 / theory 37. `I?` 47편은 전문 확인 후 확정. 한국 관련 47편.
4. **운영안 확정: 옵션3** — 완전추출 297편(주 11편: 석박사 2·학부 1) + 경량추출 141편(전원 주 1편). 27주, 2026-10-12 시작 → 2027-04-16 종료. 석박사를 주 3편으로 올리면 22주(2027-03-12).
5. 배정표: `students/assignments.csv`(W1~W4: 완전 44 + 경량 32), 전체 `students/assignments_option3.csv`(채택), 비교용 `_option1.csv`.

## 연구책임자가 위임해 Claude가 내린 결정 (2026-10-10, 바꾸려면 §13 변경 이력에 기록)
- 운영안 옵션3, 연도 하한 없음(1986~), 주 11편.
- 저널 색인 기준 추가하지 않음. 저품질 추정 7편은 `low-tier` 표시 → 민감도 분석.
- AI 보조 선별의 인간 재판독: 무작위 10%(140건) + `I?` 47건 + 1차 E2·E3 142건 → 이원석·석사① 독립 판정, κ 보고.
- OpenAlex 보완 검색 완료(키는 환경변수 `OA_KEY`로만, 저장소에 쓰지 않음).

## 교수만 할 수 있는 일(남은 것)
- [ ] 배정표 사람 칸에 실명 기입(박사/석사①/석사②/학부①~④)
- [ ] Scopus·WoS 기관 접속 확인 → 원석 보완 검색 / KCI OpenAPI 키 발급
- [ ] 10/12(월) 첫 회의

## 파일 지도
- `protocol/` 프로토콜·검색식·코드북·저널 비교·JHE 제약표
- `review/` 포함 목록(438), 판독 로그(844), OpenAlex 판독(556, `screening_openalex.csv`, 사유 `oa/`), 전체 레코드(35,397), PRISMA 수치, 선별 규칙, 선행 리뷰
- `scripts/` 검색(s2/cr/hand/snowball/oa_search) → 병합(merge2) → 규칙선별(stageB) → 게재본 확인(resolve) → 편집(compile) → 배정(assign `--option 3 [--grad 3]`)
- `students/` 운영 계획(v5), 배정표, 주간 보고 양식, AI 사용 기록
- `examples/` 정리 수준 기준 예시(Famiglietti 2020)
- `templates/` 추출 CSV, 1쪽 양식, 선별·검색 로그(OpenAlex 3행 포함)

## 규칙
원문에 없는 것은 쓰지 않는다(`NR`). 인용은 DOI로 실존 확인. 지표마다 1행. AI 사용은 `students/ai_use_log.md`에 기록(JHE 선언 요건). API 키·비밀은 커밋하지 않는다.
