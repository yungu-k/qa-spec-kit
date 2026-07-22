# QA 엔지니어 팀원 — 사용법

QA 팀의 **동료 QA 엔지니어**(Claude subagent). 사람 QA(공윤구)의 짝.
기획자([[planner]])와 대칭: 기획자="무엇을 만들까", QA="무엇이 깨질까·무엇을 검증할까".

## 부르는 법
- 이 디렉토리(`Desktop\QA\AI`)에서 Claude Code 실행 → `qa-engineer` subagent 자동 인식.
- 또는 Agent 도구로 `subagent_type: "qa-engineer"` 지정.

## 무엇을 시키나 (3대 역할)
| 하고 싶은 것 | 한마디 | 쓰는 skill |
| :-- | :-- | :-- |
| 뭘 테스트해야 할지·예외 케이스 조언 | "이거 뭘 테스트해야 해?" | `advise-test-coverage` |
| 코드베이스 유닛 테스트 작성 | "이 함수 유닛 테스트 짜줘" | `write-unit-tests` |
| 릴리스 diff 영향도·회귀 테스트 | "이번 diff 뭐가 영향받아?" | `diff-driven-test` |

## 4층 구조
| 층 | 파일 |
| :-- | :-- |
| 페르소나 | `.claude/agents/qa-engineer.md` |
| 헌법(불변) | `QA_ENGINEER_CONTEXT.md` |
| 방법론(3-파일 skill) | `.claude/skills/{advise-test-coverage,write-unit-tests,diff-driven-test}/` |
| 상태(가변) | `state/qa-engineer-focus.md` |
| 지식베이스(재사용) | `TC_DESIGN_GUIDE.md` · `QA_REPORT.md` |

## 핵심 원칙 (헌법 요약)
- **경계에 가치.** 정상 경로는 기본, 예외·엣지·경계·상태전이를 먼저 판다.
- **fail ≠ dev 버그.** 스펙·mock 정합 먼저. Jira 는 사람 confirm 후.
- **언어가 산출물마다 갈림.** 테스터용=메뉴·화면·조작·결과, CI용=코드 용어.
- **사실대로 보고.** 초록불만 보고 넘기지 않음(유닛 테스트는 일부러 깨서 역검증).
- **스펙 결정·배포·머지는 사람이.** QA 는 검증·근거·초안까지.
- **보호 브랜치 push 금지.** qa 브랜치 + `qa/` 접두사만.
