---
status: active
owner: QA
updated: 2026-08-24
---

# [Index] QA Automation Project — Domain Entry Point

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-04-14 | QA Engineer | 진입점 문서 분리 — 본문 도메인별 md 분산. CLAUDE.md 인덱스 역할만, Claude Code 자동 로드 컨텍스트 경량화 |
| 1.1 | 2026-08-24 | QA Engineer | 도메인 3종 신설 등재 — `VERIFICATION_GUIDE.md`(검증 방법론) · `REPORT_STYLE_POLICY.md`(내용/스타일 분리, 2026-08-21 확정) · `SESSION_ROLES.md`(5개 세션 역할). §5 에 push 범위·커밋 메시지·한글 파일 치환 규칙 추가 |

---

## 1. Purpose

본 파일 Claude Code 프로젝트 진입 시 자동 로드 **인덱스(Index)** 문서. 각 도메인 상세 규격 별도 md 파일 관리.

> **사용 원칙:** 작업 도메인 식별 후, 아래 표 해당 md 파일 참조하여 작업 진행. 상세 규격 본 파일 중복 작성 금지.

---

## 2. Domain Map

| 도메인 | 규격 파일 | 적용 시점 |
| :--- | :--- | :--- |
| **TC 설계 + Bug Report** | [`TC_DESIGN_GUIDE.md`](./TC_DESIGN_GUIDE.md) | Figma → TC 설계, Jira 버그 등록 시 |
| **QA 리포팅 (Result + Status)** | [`QA_REPORT.md`](./QA_REPORT.md) | QA 종료 보고(Sign-off), 진행 중 현황 보고 시 |
| **Hotfix 검증 리포트** | [`HOTFIX_REPORT_TEMPLATE.md`](./HOTFIX_REPORT_TEMPLATE.md) | Hotfix 검증 후 PDF 리포트 산출 시 |
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
├── TC_DESIGN_GUIDE.md                 # TC 설계 + Bug Report 규격
├── QA_REPORT.md                       # QA Result + QA Status 리포팅 규격
├── HOTFIX_REPORT_TEMPLATE.md          # Hotfix 검증 PDF 리포트 템플릿
├── VERIFICATION_GUIDE.md              # 검증 방법론 — 검사가 실제로 보고 있는가
├── REPORT_STYLE_POLICY.md             # 리포트 내용/스타일 분리 규약
├── SESSION_ROLES.md                   # AI 팀원 5개 세션 역할·경계·라우팅
├── QA_ENGINEER_CONTEXT.md             # QA 엔지니어 팀원 헌법 (subagent 지식베이스=위 규격 재사용)
├── assets/
│   └── report.css                     # 리포트 공용 스타일 (A4 인쇄 전용) — 스타일의 유일한 원본
├── state/
│   └── qa-engineer-focus.md           # 가변 상태 템플릿 (헌법과 유효기간이 다름)
└── .claude/
    ├── agents/
    │   └── qa-engineer.md             # QA 엔지니어 페르소나(subagent)
    ├── skills/                        # advise-test-coverage · write-unit-tests · diff-driven-test (각 SKILL+TEMPLATE+EXAMPLE)
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