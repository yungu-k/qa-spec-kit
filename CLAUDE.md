---
status: active
owner: QA
updated: 2026-10-30
---

# [Index] QA Automation Project — Domain Entry Point

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-04-14 | QA Engineer | 진입점 문서 분리 — 본문 도메인별 md 분산. CLAUDE.md 인덱스 역할만, Claude Code 자동 로드 컨텍스트 경량화 |
| 1.1 | 2026-08-24 | QA Engineer | 도메인 3종 신설 등재 — `VERIFICATION_GUIDE.md`(검증 방법론) · `REPORT_STYLE_POLICY.md`(내용/스타일 분리, 2026-08-21 확정) · `SESSION_ROLES.md`(5개 세션 역할). §5 에 push 범위·커밋 메시지·한글 파일 치환 규칙 추가 |
| 1.2 | 2026-10-30 | QA Engineer | TC 설계 키트 2판 등재 — `TC_QUICKSTART.md`(TC 문체 정본) · `tools/tc_lint.py`(금지 패턴·꼴 검사) · `.claude/skills/tc-design/`(입력→초안→반증 라운드→lint 스킬) |
| 1.3 | 2026-10-30 | QA Engineer | TC 설계 키트 2판 보강(깨끗한 환경 시험 반영) — 실행 화면 관찰(캡처) 입력 단계, 반증 두 갈래(소스 대조 + 수행: 모호 0·불가 0), `tc_lint` S10~S13(확정 표 `[확인 필요]`·눈대중 낱말·행 참조·조건부 규칙 세 경우) |
| 1.4 | 2026-10-30 | QA Engineer | TC 키트 2회차 시험 반영 — Pre 는 Expected 가 기대는 상태를 전부(개수+속성), Expected 는 나머지 항목을 닫는다, 수행 반증 Pre 반례 검사 필수·엄격 기준, 불가 vs 도구 한계 분리, `tc_lint` W4(경고) |
| 1.5 | 2026-10-30 | QA Engineer | TC 키트 3회차 시험 반영 — Pre 상태에 모드(편집 중·열린 창)·주소 모양 포함, 같은 화면 행끼리 Pre 조건 맞대기, Pre 반례에 모드·주소·기획과 다르게 남는 상태 |
| 1.6 | 2026-10-30 | QA Engineer | TC 키트 4회차 시험 반영 — 실패할 수 있는 줄만 판정(헛판정 금지), 수행 반증 2-3 헛판정 찾기 |
| 1.7 | 2026-10-30 | QA Engineer | 실무 TC 비교 반영 — §1.2 덮개 점검 다섯 꼴, 반증 라운드 상한 6·미해결 모호 표기, 현장 질문은 「수행 전 확인」 칸(AUDITOR_BRIEF 2-4) |

---

## 1. Purpose

본 파일 Claude Code 프로젝트 진입 시 자동 로드 **인덱스(Index)** 문서. 각 도메인 상세 규격 별도 md 파일 관리.

> **사용 원칙:** 작업 도메인 식별 후, 아래 표 해당 md 파일 참조하여 작업 진행. 상세 규격 본 파일 중복 작성 금지.

---

## 2. Domain Map

| 도메인 | 규격 파일 | 적용 시점 |
| :--- | :--- | :--- |
| **TC 설계 — 시작 한 장 (문체 정본)** | [`TC_QUICKSTART.md`](./TC_QUICKSTART.md) · [`tools/tc_lint.py`](./tools/tc_lint.py) · [`.claude/skills/tc-design/`](./.claude/skills/tc-design/SKILL.md) | 기획 문서 + 코드로 TC 를 **새로 쓸 때**. 칸 규칙·반증 라운드·금지 패턴 검사 |
| **TC 설계 + Bug Report** | [`TC_DESIGN_GUIDE.md`](./TC_DESIGN_GUIDE.md) | Figma → TC 설계, 시트 서식, Jira 버그 등록 시 |
| **QA 리포팅 (Result + Status + PDF 템플릿)** | [`QA_REPORT.md`](./QA_REPORT.md) | QA 종료 보고(Sign-off), 진행 중 현황 보고, Sign-off·Hotfix·UAT PDF 리포트 산출(§11.4 템플릿) 시 |
| **검증 방법론 (검사가 실제로 보고 있나)** | [`VERIFICATION_GUIDE.md`](./VERIFICATION_GUIDE.md) | 테스트·감사·자동화 검사를 **새로 쓸 때**, 남의 검증 결과를 **재확인할 때**, 무변경 리팩터를 증명할 때 |
| **리포트 스타일 규약 (내용/스타일 분리)** | [`REPORT_STYLE_POLICY.md`](./REPORT_STYLE_POLICY.md) · [`assets/report.css`](./assets/report.css) | 리포트·문서를 **발행**하기 직전. 스타일을 직접 짜고 싶어질 때 |
| **AI 팀원 세션 역할** | [`SESSION_ROLES.md`](./SESSION_ROLES.md) | 세션이 여럿일 때 — 누가 결정하나, 누구에게 넘기나 |
| **QA 엔지니어 팀원 (Advisory + 유닛/diff 테스트)** | [`QA_ENGINEER_CONTEXT.md`](./QA_ENGINEER_CONTEXT.md) (헌법) · [`state/qa-engineer-focus.md`](./state/qa-engineer-focus.md) (가변 상태) · [`.claude/qa-engineer-README.md`](./.claude/qa-engineer-README.md) (사용법) | "뭘 테스트해야 해?" 조언, 코드베이스 유닛 테스트, diff 영향도 테스트 시. subagent `qa-engineer` |

---

## 3. Slash Commands (재사용 워크플로우)

`.claude/commands/` 폴더 등록 슬래시 커맨드 목록.

| 커맨드 | 용도 | 참조 규격 |
| :--- | :--- | :--- |
| `/qa-update-result` | QA Result 리포트 자동 생성/업데이트 | `QA_REPORT.md` |
| `/qa-update-status` | QA Status 리포트 자동 생성/업데이트 | `QA_REPORT.md` |
| `/qa-sync-jira-result` | Jira 티켓 상태 → TC 시트 결과 자동 동기화 | `TC_DESIGN_GUIDE.md` |
| `/qa-create-regression` | P0 기반 Regression TC 자동 추출 | `TC_DESIGN_GUIDE.md` |
| `/qa-figma-coverage` | Figma 변경 감지 + TC 커버리지 갭 분석 | `TC_DESIGN_GUIDE.md` |

---

## 4. Project Structure

```
qa-spec-kit/
├── CLAUDE.md                          # 본 파일 (Index, 자동 로드)
├── TC_QUICKSTART.md                   # TC 설계 키트 2판 — 한 장 시작 (TC 문체 정본)
├── TC_DESIGN_GUIDE.md                 # TC 설계 + Bug Report 규격 (분류·서식·근거)
├── QA_REPORT.md                       # QA Result + QA Status 리포팅 규격 + PDF 리포트 HTML 템플릿(§11.4)
├── VERIFICATION_GUIDE.md              # 검증 방법론 — 검사가 실제로 보고 있는가
├── REPORT_STYLE_POLICY.md             # 리포트 내용/스타일 분리 규약
├── SESSION_ROLES.md                   # AI 팀원 5개 세션 역할·경계·라우팅
├── QA_ENGINEER_CONTEXT.md             # QA 엔지니어 팀원 헌법 (subagent 지식베이스=위 규격 재사용)
├── assets/
│   └── report.css                     # 리포트 공용 스타일 (A4 인쇄 전용) — 스타일의 유일한 원본
├── state/
│   └── qa-engineer-focus.md           # 가변 상태 템플릿 (헌법과 유효기간이 다름)
├── tools/
│   ├── tc_lint.py                     # TC 표 금지 패턴·꼴 검사 (--self-test 먼저)
│   └── hooks/pre-commit               # 공개 저장소 반출 검사 훅
└── .claude/
    ├── agents/
    │   └── qa-engineer.md             # QA 엔지니어 페르소나(subagent)
    ├── skills/                        # advise-test-coverage · write-unit-tests · diff-driven-test (각 SKILL+TEMPLATE+EXAMPLE)
    │   └── tc-design/                 # 기획+코드 → TC (SKILL + TEMPLATE·AUDITOR_BRIEF·EXAMPLE)
    ├── qa-engineer-README.md          # QA 엔지니어 사용법
    └── commands/                      # 재사용 슬래시 커맨드
```

---

## 5. Persona & Working Principles (공통)

본 프로젝트 모든 도메인 공통 적용 작업 원칙.

* **Senior QA Persona:** 9년 차 시니어 QA 엔지니어 관점 산출물 생성. 단순 기능 확인 넘어 **엣지 케이스, 예외 처리, UX, 성능 임계치** 고려.
* **Holistic View:** 기획서 미명시 **암묵적 요구사항(Implicit Requirements)** 도출.
* **Precision:** 각 도메인 규격 엄격 준수, 일관 산출물 생성.
* **Knowledge Engineering:** 분류/서식/네이밍 규칙 항상 해당 도메인 md 명시, 코드는 구현물. 규격 변경 시 md와 코드 함께 갱신.
* **검증 규율:** 새 검사는 **일부러 한 번 실패시켜 본다.** 남의 결과·명세는 **재구현하지 말고 원본을 돌려서** 확인한다. 상세 [`VERIFICATION_GUIDE.md`](./VERIFICATION_GUIDE.md).
* **버전 관리:** 본 폴더 = git repo (**규격 저장소이므로** main 직push OK). **규격 md 를 변경한 세션은 마무리 시점에 commit + push** — 미루면 방치됨 (2026-05~07 두 달 방치 사고). 크리덴셜은 .gitignore 확인 후.
  - ⚠️ **이 예외는 이 저장소에만 적용된다.** **제품·개발 저장소의 보호 브랜치(main/release/develop) push 는 금지** — `QA_ENGINEER_CONTEXT.md` §4. 두 규칙은 대상이 다르다.
  - **커밋 메시지에 이슈 트래커 티켓 키를 넣지 않는다.** 저장소–트래커 연동이 자동 mention 코멘트를 달아 무관한 사람에게 알림이 간다. TC 번호나 "티켓 NNNN" 표기로 우회.
* **한글 파일 일괄 치환은 편집 도구로만.** 셸 도구(PowerShell·sed)로 읽어 되쓰면 Windows 기본 인코딩 추정이 UTF-8 을 CP949 로 읽어 **mojibake** 를 만든다(실사고: 5개 파일 손상 → `git checkout` 복구). 파일마다 Edit. 새 파일을 UTF-8 로 생성하는 것은 재인코딩이 없어 해당 없음.

---

## 6. Adding a New Domain

새 도메인 추가 시:
1. 도메인 전용 md 파일 적절 위치 생성 (자체 완결 도메인이면 별도 폴더 권장)
2. 본 파일 Section 2 Domain Map 등재
3. 관련 슬래시 커맨드 있으면 Section 3 등재
4. 폴더 구조 변화 있으면 Section 4 반영