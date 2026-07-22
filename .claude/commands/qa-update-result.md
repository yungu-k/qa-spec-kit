# QA Result 업데이트

Jira 데이터 + TC 시트 기반으로 QA Result (Sign-off) 시트 최신화.

## 입력
- `$ARGUMENTS`: Google Sheets URL 또는 Spreadsheet ID (필수)
  - 미입력시 사용자에게 URL 요청.

## 업데이트 대상

| Section | 데이터 소스 | 업데이트 내용 |
|---|---|---|
| **1. QA Opinion** | TC 시트 + Jira | 전체 요약, Category별 결과, Defect 현황, 종합 의견 |
| **2. Defect Summary** | Jira (Epic 하위 Bug) | Detected Defects, Priority 분포 (P0~P3) |
| **4. Verification Details** | TC 시트 (대분류별 분석) | Test Area별 핵심 검증 항목, Pass/Fail/N/A 건수, Result 판정 |

## 처리 절차

### 1단계: 데이터 수집
1. **Epic Key 확인:** TC 시트 D2 셀 파싱
2. **Jira Bug 전체 조회:** 페이지네이션 필수. 상태별(완료/REJECT/FIXED/Open) + Priority별(P0~P3) 집계
3. **TC 시트 집계:** 각 Full Test Case + Regression Test Case 시트 I열(Test Result)을 대분류(B열) > 중분류(C열) 단위 집계

### 2단계: Defect Summary 업데이트 (Row 7-9)
- C7: Detected Defects (전체 건수)
- C9/E9/G9/I9/K9: P0/P1/P2/P3/Total

### 3단계: QA Opinion 업데이트 (Row 5)
아래 구조로 작성. **모든 수치 실제 집계값 사용, 유추 금지.**

```
[전체 요약]
총 N건의 TC 중 N건 Pass, N건 Fail, N건 N/A, N건 N/T, N건 Retest. 전체 Success Rate N%. 검출 Defect N건.

[Category별 결과]
- {시트명}: N건 중 N건 Pass, SR N%. {Fail이 있으면 어떤 영역에서 Fail인지 대분류>중분류 기준으로 기술}
- ...

[Defect 현황]
총 N건 중 Closed N건, REJECT N건, Open N건. Open 목록(이슈키+요약).

[종합 의견]
Success Rate 기반 품질 평가. Open Defect 영향도 평가. 잔여 작업(Retest/N/T) 언급.
```

### 4단계: Verification Details 업데이트 (Row 24+)
- TC 시트 **대분류(B열)** 기준으로 Test Area 결정
- 해당 대분류 속한 TC의 **중분류(C열), 소분류(D열)** 분석해 Key Verification Items 작성
- 각 항목 끝에 `— N건 중 N건 Pass, N건 Fail, ...` 요약 추가
- **Result:** 영역 TC 중 Fail 1건이라도 있으면 `Fail`, 전체 Pass면 `Pass`, TC 없으면 `N/A`

## 주의사항
- **사실 기반 작성:** 모든 데이터는 TC 시트 + Jira에서 실제 확인된 값만 사용. 유추 금지.
- Google Sheets API 접근에 `google-credentials.json` 서비스 계정 파일 사용.
- Jira 조회시 페이지네이션 필수 (next_page_token 순회)
- 테스트 버전은 TC 시트 D4에서 실시간 읽음.
- Verdict, Date, QA Lead, Remarks (Row 4)는 수동 입력 항목 — 변경 금지.
- etc. 영역 (Row 18-21)은 수동 입력 항목 — 변경 금지.