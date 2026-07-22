# qa-spec-kit

AI Agent(Claude Code)와 함께 일하는 QA 팀의 **규격 문서 모음**입니다. 프롬프트가 아니라 규격 문서가 자동화 품질을 결정한다는 원칙으로, 실무에서 1년간 실수 → 교정 → 문서화를 거치며 다듬어진 실물입니다.

> 배경 이야기: [AI-Driven QA 블로그](https://ai-driven-qa.vercel.app) — 특히 [따라하기 가이드](https://ai-driven-qa.vercel.app/posts/getting-started-qa-automation-with-ai/)와 [AI QA 엔지니어 팀원 만들기](https://ai-driven-qa.vercel.app/posts/ai-qa-engineer-teammate/).

## 구성

| 파일 | 내용 |
| --- | --- |
| `CLAUDE.md` | 도메인 인덱스 — Claude Code가 매 세션 자동 로드하는 진입점 |
| `TC_DESIGN_GUIDE.md` | TC 설계 + Bug Report 규격 — 필수 컬럼, 서식 체크리스트 9단계, diff 기반 영향도 TC, 테스터 언어 원칙 |
| `QA_REPORT.md` | QA Result(Sign-off)·QA Status 리포트 규격 |
| `HOTFIX_REPORT_TEMPLATE.md` | Hotfix 검증 PDF 리포트 템플릿 (headless 브라우저 인쇄) |
| `QA_ENGINEER_CONTEXT.md` | AI QA 엔지니어 팀원의 '헌법' — 역할 경계, 실수에서 옮겨온 규칙들 |
| `.claude/agents/` `.claude/skills/` `.claude/commands/` | subagent 페르소나 + 스킬 3종(커버리지 조언/유닛 테스트/diff 영향도) + 슬래시 커맨드 |

## 사용법

Claude Code로 이 폴더를 열면 `CLAUDE.md`가 자동 로드됩니다. 팀에 맞게 고칠 것:

1. 예시 자리표시자 교체 — `CustomerA`(고객사), `KioskA`/`KioskB`/`Platform`(제품), `PROJ-`(티켓 프리픽스), `your-team.atlassian.net`
2. `TC_DESIGN_GUIDE.md`의 컬럼·라벨 규칙을 팀 시트 구조에 맞게 조정
3. AI가 실수하면 그 자리에서 규칙 한 줄을 추가 — 이 문서들이 자란 방식 그대로

## 원칙

- **규칙은 코드가 아니라 문서에 먼저** — 사람도 읽고, AI도 참조한다
- **실패는 규칙으로 옮긴다** — 이 문서의 규칙 대부분은 실제 사고의 흔적이다
- **산출물의 언어는 독자를 따른다** — 테스터용은 쉬운 말, CI용은 코드 말

## License

MIT
