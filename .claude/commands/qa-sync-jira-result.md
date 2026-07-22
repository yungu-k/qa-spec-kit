# Jira ↔ Test Result 동기화

Jira 티켓 상태 기반 Google Sheets TC 시트 Test Result 업데이트.

## 입력
- `$ARGUMENTS`: Google Sheets URL 또는 Spreadsheet ID (필수)
  - 미입력 시 사용자에게 URL 요청.

## 동기화 규칙

| Jira 상태 | TC Result 액션 | 사유 |
|---|---|---|
| **완료** | Fail → **Pass** | 수정 완료 및 검증 완료 |
| **FIXED** | 유지 (Fail) | 수정됐으나 QA 재검증 필요 |
| **REJECT** | Fail → **N/A** | 반려 — 기능 미구현/스펙 제외 |
| **PENDING** (상태명에 `pending` 포함, 대소문자 무관) | Fail → **N/A** | 이번 QA 범위 제외 — 차기 이관 |
| **다시 열림** | 유지 (Fail) | 재오픈 이슈 |
| 기타 | 유지 (Fail) | 미해결 |

## 처리 절차

1. **대상 시트 식별:** 스프레드시트 내 모든 **"Full Test Case" 시트 + "Regression Test Case" 시트** 대상. (Smoke Test, QA Plan, QA Result, QA Status 등 제외)

2. **Fail TC 수집:** 각 TC 시트에서 Test Result(I열)="Fail" + Comment(J열)에 Jira 이슈 키(CAS-XXXX) 있는 행 수집.

3. **Jira 상태 조회:** 수집된 Jira 이슈 키 현재 상태를 MCP `jira_get_issue` 또는 `jira_search`로 일괄 조회. **페이지네이션 필수:** next_page_token 있으면 전체 페이지 순회.

4. **동기화 판정:**
   - TC 연결된 **모든** Jira 티켓이 "완료"일 때만 Pass로 변경.
   - TC 연결된 **모든** Jira 티켓이 "REJECT" 또는 **PENDING**(상태명에 `pending` 포함)일 때 N/A로 변경.
   - 하나라도 위 조건 미충족 티켓 있으면 Fail 유지.

5. **시트 업데이트:** 판정 결과 따라 I열(Test Result)을 "Pass" 또는 "N/A"로 업데이트.

6. **결과 리포트:** 아래 형식으로 출력:
   - 변경된 TC 목록 (시트명, TC No, Jira 키, 이전 상태 → 이후 상태)
   - 미변경 TC 목록 및 사유 (FIXED, REJECT, 다시 열림 등)
   - 전체 요약 (변경 N건 / 유지 N건)

## 주의사항
- Google Sheets API 접근은 `google-credentials.json` 서비스 계정 파일 사용.
- Jira 상태명 프로젝트별 상이 가능 — status.name 정확히 비교.
- 실행 전 변경 대상 목록을 사용자에게 보여주고 확인 받은 후 업데이트 진행.