---
status: active
owner: QA
updated: 2026-08-24
---

# qa-spec-kit

AI Agent(Claude Code)와 함께 일하는 QA 팀의 **규격 문서 모음**입니다. 프롬프트가 아니라 규격 문서가 자동화 품질을 결정한다는 원칙으로, 실무에서 1년간 실수 → 교정 → 문서화를 거치며 다듬어진 실물입니다.

> 배경 이야기: [AI-Driven QA 블로그](https://ai-driven-qa.vercel.app) — 특히 [따라하기 가이드](https://ai-driven-qa.vercel.app/posts/getting-started-qa-automation-with-ai/)와 [AI QA 엔지니어 팀원 만들기](https://ai-driven-qa.vercel.app/posts/ai-qa-engineer-teammate/).

## 구성

| 파일 | 내용 |
| --- | --- |
| `CLAUDE.md` | 도메인 인덱스 — Claude Code가 매 세션 자동 로드하는 진입점 |
| `TC_DESIGN_GUIDE.md` | TC 설계 + Bug Report 규격 — 필수 컬럼, 서식 체크리스트 9단계, diff 기반 영향도 TC, 테스터 언어 원칙 |
| `VERIFICATION_GUIDE.md` | **검사가 실제로 무언가를 보고 있는가** — 눈 없는 단언 7유형, 원본을 돌리는 검증, 무변경은 해시로 증명, 최종 매체 감사 |
| `QA_REPORT.md` | QA Result(Sign-off)·QA Status 리포트 규격 |
| `HOTFIX_REPORT_TEMPLATE.md` | Hotfix 검증 PDF 리포트 템플릿 (headless 브라우저 인쇄) |
| `REPORT_STYLE_POLICY.md` · `assets/report.css` | 리포트 내용/스타일 분리 규약 + 공용 CSS 1벌 |
| `SESSION_ROLES.md` | AI 팀원 세션(planner/dev/QA/design/tw) 역할·경계·라우팅 |
| `QA_ENGINEER_CONTEXT.md` · `state/` | AI QA 엔지니어 팀원의 '헌법'(불변) + 가변 상태 템플릿 |
| `.claude/agents/` `.claude/skills/` `.claude/commands/` | subagent 페르소나 + 스킬 3종(커버리지 조언/유닛 테스트/diff 영향도) + 슬래시 커맨드 |

## 사용법

Claude Code로 이 폴더를 열면 `CLAUDE.md`가 자동 로드됩니다. 팀에 맞게 고칠 것:

1. 예시 자리표시자 교체 — `CustomerA`(고객사), `KioskA`/`KioskB`/`Platform`(제품), `PROJ-`(티켓 프리픽스), `your-team.atlassian.net`, `{작성자}`
2. `TC_DESIGN_GUIDE.md`의 컬럼·라벨 규칙을 팀 시트 구조에 맞게 조정
3. `assets/report.css`를 팀 디자인 자산으로 교체 — 규약(내용/스타일 분리)만 그대로 쓴다
4. `state/qa-engineer-focus.md`를 팀 실제 상태로 덮어쓰기 (지금은 빈 템플릿)
5. AI가 실수하면 그 자리에서 규칙 한 줄을 추가 — 이 문서들이 자란 방식 그대로

> **`[[wiki-link]]` 표기에 대하여**: 문서 곳곳의 `[[feedback_...]]` `[[project_...]]` 는 이 저장소가
> 아니라 **AI 팀원의 개인 메모리 노트**를 가리킨다. 클론한 쪽에는 그 노트가 없으므로 **링크가 아니라
> "이 규칙이 어떤 사고에서 나왔는지 태그" 정도로 읽으면 된다.** 규칙 본문은 전부 문서 안에 있다.

## 원칙

- **규칙은 코드가 아니라 문서에 먼저** — 사람도 읽고, AI도 참조한다
- **실패는 규칙으로 옮긴다** — 이 문서의 규칙 대부분은 실제 사고의 흔적이다
- **산출물의 언어는 독자를 따른다** — 테스터용은 쉬운 말, CI용은 코드 말
- **초록은 「통과」와 「아무것도 안 봄」을 구분하지 못한다** — 새 검사는 일부러 실패시켜 본다
- **만든 세션이 자기 산출물을 최종 검증하지 않는다** — 역할을 가르는 이유는 분업이 아니라 독립성이다

## License

MIT
