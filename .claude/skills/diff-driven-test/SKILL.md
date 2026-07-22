---
name: diff-driven-test
description: >
  릴리스 diff(마지막 QA 검증 ref ↔ 최신)로 영향 범위를 산정하고 신규/변경/회귀
  테스트를 뽑는다. baseline 정확도가 전부(PROD live 아니라 마지막 검증 ref).
  "이 diff 뭐가 영향받아?", "이번 릴리스 뭘 테스트해야 해?", "회귀 포인트 짚어줘" 때 사용.
  규격 원본은 TC_DESIGN_GUIDE.md §6.5, repo/baseline 매핑은 project_diff_driven_tc 메모.
---

# diff-driven-test — Diff 기반 영향도 테스트

릴리스 변경점을 git diff 로 산정해 **무엇이 바뀌었고 무엇이 회귀 위험인지**를 뽑는 방법. Jira 산문보다 정확(시그니처 변경·회귀 포인트까지). 규격 원본 = `TC_DESIGN_GUIDE.md §6.5`.

## 좋은 산출물이란 (품질 기준)

- **baseline 이 정확하다** = 마지막 **QA 검증완료** ref ↔ 최신. PROD live 로 잡으면 이미 검증된 걸 신규로 오검출(전례: KioskA 7건 작성 후 삭제).
- 변경이 **신규/변경/회귀**로 분류돼 있다. 회귀(간접 영향)를 특히 짚는다.
- 각 변경에 **테스터 언어 TC**(메뉴·화면·조작·결과)가 붙는다 — 코드 용어 금지([[feedback_tc_tester_language]]).
- 검증 불가(HW 의존 등)는 `N/T` 로 정직하게 표시.
- DB 스키마 변경 등 **git 밖 변경**을 놓치지 않는다(별도 확인).

## 절차

1. **헌법·상태·메모 로드**: `QA_ENGINEER_CONTEXT.md` + `state/qa-engineer-focus.md` + [[project_diff_driven_tc]](repo URL·baseline 매핑).
2. **baseline 확정** (最중요): 대상 repo 의 **마지막 QA 검증완료 ref** 를 찾는다. 검증완료 차수 시트 먼저 대조(가이드 §6.5.2). PROD 브랜치 ≠ 자동으로 baseline.
3. **diff 실행**: `git diff <baseline>..<latest>`(remote ref 직접 가능, 크리덴셜 캐시됨). 파일 수 과다면 baseline 재의심.
4. **변경 추출**: hunk 별로 동작 변경 판별 — 라우팅/분기/상수/시그니처/문구. 다국어 문구만이면 로직 무변화(TC skip 가능).
5. **분류**:
   - **신규**: 없던 기능/화면.
   - **변경**: 기존 동작 수정 → 기대결과 갱신.
   - **회귀**: 직접 안 바뀌었지만 **공유 코드/상태 통해 영향** 받는 것. ← 여기가 diff 방식의 핵심 가치.
6. **git 밖 변경 확인**: DB 스키마·설정·마이그레이션(신규 테이블 등)은 diff 에 안 잡힘 → 별도 확인(§6.5.0).
7. **TC 작성** (`TC_DESIGN_GUIDE.md §6.4` Release TC): mock 우선, 의존성 Pre-Condition, 검증불가 `N/T`. 문구는 테스터 언어(코드 근거로 확정하되 사용자 문구로 번역).
8. **bundled commit 주의**: 한 커밋에 검증됨+미검증 번들이면 수동 판별(RFID 검증분 vs 비RFID 미검증 전례).

## 언제 쓰지 말 것 (경계)

- 코드 레벨 회귀 방어(함수 단위) → `write-unit-tests` skill.
- 화면 커버리지 조언(diff 아닌 신규 기획) → `advise-test-coverage` skill.
- baseline 이 불명확 → 먼저 사람 QA·버전 시트로 확정(추측 diff 금지).

## 출력 계약

`references/TEMPLATE.md` 구조:
1. **baseline/latest ref** — 무엇을 무엇과 비교했나 + 근거(검증완료 차수).
2. **변경 요약** — 파일/hunk 수, 로직 변경 vs 문구만.
3. **영향도 표** — 변경점 / 분류(신규·변경·회귀) / 테스터 TC / N/T 여부.
4. **git 밖 변경** — DB/설정 확인 결과.
5. **미완/대기** — dev 미푸시분 등(전례: Platform RFID 부분 커버).

품질 앵커: `references/EXAMPLE.md`. baseline 원칙: **마지막 검증 ref**, PROD 아님.
