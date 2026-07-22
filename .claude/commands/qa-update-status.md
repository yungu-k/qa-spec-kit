# QA Status 업데이트

Jira 데이터 + TC 시트 기반으로 QA Status 시트 Section 2~5 최신화.

## 입력
- `$ARGUMENTS`: Google Sheets URL 또는 Spreadsheet ID (필수)
  - 미입력 시 사용자에 URL 요청.

## 업데이트 대상

| Section | 데이터 소스 | 업데이트 내용 |
|---|---|---|
| **2. Defect Status** | Jira (Epic 하위 Bug) | Total/Open/Fixed/Reject/Closed 건수, Resolution Rate, Priority 분포 |
| **3. Open & Reopened Defects** | Jira | Open 상태(NEW, 진행 중, QA 배포됨, 다시 열림) 버그 목록 |
| **4. Fixed — QA 검증 대기** | Jira | FIXED 상태 버그 목록 |
| **5. Remaining Work** | Jira + TC 시트 | FIXED N건, N/T+Retest N건, Open N건 기반 잔여 작업 |

## 처리 절차

1. **Epic Key 확인:** 대상 스프레드시트 TC 시트 D2 셀에서 Epic Key 파싱.
2. **Jira 전체 Bug 조회:** `parent = {Epic Key} AND issuetype = Bug` JQL 조회. **페이지네이션 필수** — next_page_token 있으면 모든 페이지 순회.
3. **상태별 분류:**
   - **Open:** `NEW`, `진행 중`, `QA 배포됨`, `다시 열림`
   - **Fixed:** `FIXED`
   - **Reject:** `REJECT`
   - **Closed:** `완료`
4. **Priority 매핑:** Highest=P0, High=P1, Medium=P2, Low/Lowest=P3
5. **TC 시트 집계:** 각 Full Test Case 시트 I열에서 N/T, Retest 건수 집계.
6. **시트 재생성:** QA Status 시트 삭제 후 새로 생성. (가변 행 처리 위해 재생성 방식)
   - Section 1: TC 시트 수식 참조 (자동 계산)
   - Section 2: Jira 집계 값 입력
   - Section 3: Open 버그 목록 (Priority 순 P0→P3)
   - Section 4: Fixed 버그 목록 (Priority 순)
   - Section 5: Remaining Work 기본 항목 생성
7. **서식 적용:** QA_REPORT.md Section 10 규격 따라 머지, 스타일, 조건부 서식, 테두리 적용
8. **결과 리포트:** 업데이트 내용 요약 출력.

## Remaining Work 기본 항목

1. FIXED N건 리그레션 테스트
2. N/T N건 + Retest N건 테스트 수행
3. Bug fix + 리그레션 테스트 준비
4. Open Defect N건 수정 후 재검증
5. 전체 리그레션 테스트

- **N건:** 실제 집계값 반영. 항목 1(FIXED), 2(N/T+Retest), 4(Open Defect) 건수는 매 실행 시 Jira/TC 시트에서 최신 값으로 현행화.
- **Owner / ETA:** 빈값 생성 (엔지니어 수동 입력)

## 주의사항
- Google Sheets API 접근에 `google-credentials.json` 서비스 계정 파일 사용.
- 시트 재생성 시 QA_REPORT.md Section 10 디자인 시스템(색상, 폰트, 머지 구조, 열 너비, 조건부 서식) 정확히 따른다.
- 가변 행 계산 규칙(Section 10.2) 준수: 빈 행(구분선)과 Section Header 혼동 금지.
- 테스트 버전은 TC 시트 D4에서 실시간 읽음.

## 수식 행 참조 규칙 (필수 — 전체 Section 공통)

수식은 **Google Sheets 행 번호(1-indexed)** 기준 참조. Python data 리스트 인덱스(0-indexed)나 `len(data)` 시점 값 사용 시 헤더/데이터 행 뒤바뀌는 버그 발생.

- **일반 규칙:** Row N 수식은 자기 행 번호 N 참조.
- **data 리스트 기반 계산 금지:** `len(data) + 1` 같은 동적 계산 대신, data에 행 모두 추가 후 확정된 행 번호 사용.
- **검증:** 수식 생성 후, 참조 대상이 헤더 행 아닌 데이터 행인지 반드시 확인.
- **적용 대상:** Section 1 (Progress/SR), Section 2 (Resolution Rate), 기타 모든 수식 셀

## 서식 적용 필수 규칙 (깨짐 방지)

시트 재생성 시 아래 규칙 반드시 준수. 과거 발생한 서식 깨짐 사례 기반 작성.

### 1. Category 데이터 행 서식 범위
- Category 데이터 행(Row 7~) 서식 루프는 **TC 시트 개수만큼** 정확히 반복.
- 0-indexed 기준 `range(6, 6+len(tc_sheets))` — **6부터 시작, 6+N 미만** 설정.
- 마지막 Category 행 누락 시 머지(A:B, C:D), 배경색, 정렬, % 포맷 모두 빠짐.

### 2. Category header(Row 6) 서식 덮어쓰기 방지
- Category data 서식 루프가 Row 6(0-indexed 5)부터 시작 시 header `bold=True`가 data `bold=False`로 덮어쓰기됨.
- data 서식 범위는 반드시 **Row 7(0-indexed 6)부터** 시작.
- header 서식은 data 서식 **이후에** 적용 또는, data 범위와 겹치지 않도록 한다.

### 3. Priority Distribution 머지 순서
- C:D, E:F, G:H, I:J 머지 **먼저** 적용 후, A:B 세로 머지(2행) 마지막 적용.
- A:B 머지 먼저 시 이후 B:C 머지에서 B열 겹쳐 에러 발생.
- 머지 컬럼: C:D(P0), E:F(P1), G:H(P2), I:J(P3), K단독(Comment)
- A8:B9 세로 머지 = Priority Distribution 라벨

### 4. 머지 셀 값 입력 규칙
- 머지 영역에 값 입력 시 반드시 **머지 좌상단 셀**에 입력.
- 예: C:D 머지 → C열에 값 입력 (D열 입력 시 무시)
- 예: A:B 세로 머지(Row 8-9) → A8에 값 입력

### 5. Fixed 0건 처리
- Fixed 상태 버그 0건일 때 Section 4는 header 1행 + "해당 없음" 1행 구성.
- 빈 데이터 영역에 머지 적용 시 에러 발생 가능.

### 6. Progress/SR 서식
- Category 데이터 행 J열(Progress)과 K열(Success Rate)에는 반드시 `bold=True` + `numberFormat PERCENT 0.0%` 적용.
- 서식 범위가 I열까지만 적용 시 J-K의 % 포맷과 Bold 누락.