# 생성형 AI 사용 기록 (JHE 투고 시 선언문 작성 근거)

| 일자 | 사용자 | 도구 | 용도 | 산출물에 반영된 범위 | 원문 확인 여부 |
|---|---|---|---|---|---|
| 2026-10-06 | 최승비 | Claude Code | 프로토콜·검색식·코드북·양식 초안, Crossref 스캔·서지 실존 검증 스크립트 실행, 후보 저널 비교 | `protocol/`, `templates/`, `seed/`, `scans/` 초안 전체 | 서지는 Crossref 자동 검증 + `[미검증]` 표기 유지 |
| 2026-10-10 | 최승비(지시) / Claude(실행) | Claude Code | 체계적 검색 실행(Semantic Scholar·Crossref API, 핵심저널 hand-search, 인용추적), 중복 제거, 규칙 선별(정규식), 844건 제목·초록 판독 및 코드 부여, 게재본 확인, 포함 목록·배정표 생성 | `review/`, `scripts/`, `students/assignments*.csv` | 판독 판정은 인간 2인 재판독(10%+I?+E2/E3)으로 검증 예정. 논문 3장에 자동화 도구 사용 명시 |
