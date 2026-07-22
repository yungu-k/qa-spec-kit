# Regression Test Case 추출

Full Test Case 시트서 우선순위 높은 TC 추출하여 Regression Test Case 시트 생성.

## 입력
- `$ARGUMENTS`: Google Sheets URL 또는 Spreadsheet ID (필수)
  - 미입력시 사용자에게 URL 요청.

## 추출 기준

1. **P0 전체 추출:** 모든 Full Test Case 시트서 Priority P0인 TC 전체 추출.
2. **N/A 제외:** 원본 TC Test Result(I열) N/A 항목 제외. (환경 미비, 추후 제거 대상 등 검증 불가 TC)
3. **User Flow 보완:** P0만으로 User Flow 단절되는 영역 있으면 해당 영역 P1 TC 선별 추가.
   - 판단 기준: 대분류 > 중분류 단위로 P0 0건인 영역 중, 사용자 플로우상 필수 경로 영역
   - 예: 다국어 선택(대표 1건), 회원 정보 수정(전체) 등

## 시트 구성

- **시트명:** `Regression Test Case`
- **포맷:** TC_DESIGN_GUIDE.md Section 6.2 Full TC 규격 준수
- **Source 구분:** 대분류(B열)에 `[User]`, `[Admin]`, `[Platform]` 접두사 붙여 원본 시트 구분.
  - 예: `[User] 멤버십 가입`, `[Admin] Quick Commands`, `[Platform] Dashboard`
- **정렬:** 원본 시트 순서(User → Admin → Platform) 유지, 각 시트 내서는 원래 TC 순서 유지.

## 시트 레이아웃

| 영역 | 내용 |
|---|---|
| Row 1 (A1:B1 머지) | Summary |
| Row 2-6 | TOTAL / PASS / FAIL / N/A / N/T 자동 집계 |
| Row 7 | 빈 행 |
| Row 8 | Header (TC_No. / 대분류 / 중분류 / 소분류 / 우선 순위 / Pre-Condition / Test Step / Expected Result / Test Result / Comment & Jira link / Ref. TC) |
| Row 9+ | 데이터 |

## 서식

- Summary, Header, Priority 조건부 서식, Test Result 드롭다운, Freeze Pane(A9) 등 Full TC 규격 적용
- 컬럼 너비: A:97 / B:97 / C:167 / D:258 / E:69 / F:265 / G:363 / H:419 / I:87 / J:231 / K:139

## 처리 절차

1. **대상 시트 식별:** 스프레드시트 내 "Full Test Case" 시트 모두 식별, 시트명서 Source 접두사 결정.
2. **P0 분석:** 대분류 > 중분류 단위로 P0 TC 유무 분석.
3. **Flow 보완 판단:** P0 0건 영역 중 User Flow 필수 경로 식별하여 P1 TC 선별.
4. **시트 생성:** 기존 Regression Test Case 시트 있으면 삭제 후 새로 생성.
5. **서식 적용:** Full TC 규격(Summary, Header, Priority 서식, 드롭다운, Freeze Pane, Border) 적용.
6. **결과 리포트:** Source별 건수, Flow 보완 TC 목록 출력.

## 주의사항
- Google Sheets API 접근에 `google-credentials.json` 서비스 계정 파일 사용.
- 원본 TC Test Result, Comment 가져오지 않음. (Regression 별도 수행)
- 대상 시트명 프로젝트마다 다를 수 있음 (예: Full Test Case_User, Full Test Case_Admin 등). "Full Test Case" 포함 시트 자동 탐지.