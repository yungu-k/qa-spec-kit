---
status: active
owner: QA
updated: 2026-10-16
---

# [Standard] QA Report Design Guide

QA Result (Sign-off) Report 및 QA Status Report Google Sheets 작성 규격 정의.

> **참조:** TC 설계 및 Bug Report 규격 `TC_DESIGN_GUIDE.md` 참조.

---

## 9. QA Result (Sign-off) Report

QA 완료 후 Sign-off 리포트 Google Sheets 작성. 시트명 `QA Result` 또는 프로젝트별 지정.

### 9.1. 디자인 시스템

#### 9.1.1. 색상 / 폰트 / 정렬

| 요소 | 배경색 | 글자색 | 폰트 | 크기 | 굵기 | 정렬(가로/세로) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Title (Row 1) | `#2C3E50` | 흰색 | IBM Plex Sans | 14pt | bold | 왼쪽/중앙 |
| Section Header (Row 3,10,15,29) | `#34495E` | 흰색 | IBM Plex Sans | 11pt | bold | 왼쪽/중앙 |
| Sub-section Label (Row 7,19,24) | `#5D6D7E` | 흰색 | IBM Plex Sans | 10pt | bold | 왼쪽/중앙 |
| Table Header | `#EAECEE` | 기본(검정) | IBM Plex Sans | 10pt | bold | 가운데/중앙 |
| Data Cell | 흰색 | 기본(검정) | IBM Plex Sans | 10pt | normal | 가운데/중앙 |
| Section 4 Test Area (A열) | 교차색상 | 기본 | IBM Plex Sans | 10pt | bold | 가운데/중앙 |
| Section 4 Content (B:J열) | 교차색상 | 기본 | IBM Plex Sans | 10pt | normal | 왼쪽/중앙 |

* **세로 맞춤:** 전체 시트 `MIDDLE` 통일
* **교차 행 색상 (Section 4 데이터):** 홀수 `#F7F8F9` / 짝수 흰색

#### 9.1.2. 테두리

* **대상:** 7개 테이블 영역 (Row 4:5, 7:8, 11:13, 16:17, 20:22, 25:27, 30:39)
* **스타일:** SOLID thin, 색상 `#B3B3B3`
* **적용 순서:** **모든 서식 후 마지막** 실행. (타 서식이 border 덮어씀 → 최종 단계)

### 9.2. 시트 레이아웃

> **공백 행 없음:** Section 구분 = Section Header(`#2C3E50`). 빈 행 삽입 금지.

#### Section 1: QA Opinion (Row 1–5)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 1 | A1:K1 | `#QA Result (Sign-off)` | Title (`#1B2A3D`, 14pt bold, 흰색) |
| 2 | A2:K2 | `1. QA Opinion` | Section Header |
| 3 | A:C, D:F, G:I, J:K | Verdict / Date / QA Lead / Remarks | Table Header |
| 4 | A:C, D:F, G:I, J:K | 데이터 | Data Cell, center, wrap |
| 5 | A5:K5 | QA 의견 본문 (멀티라인) | 높이 240px, wrap, 10pt |

#### Section 2: Defect Summary (Row 6–9)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 6 | A6:K6 | `2. Defect Summary` | Section Header |
| 7 | A:B, C:D, E:F, G:K | Detected Defects(라벨) / 값 / Jira Dashboard(라벨) / 링크 | 라벨=Table Header, 값=Data Cell |
| 8–9 | A8:B9 세로 머지, C:D, E:F, G:H, I:J, K단독 | Priority Distribution(세로 머지) / P0 / P1 / P2 / P3 / Total | Row 8=Table Header, Row 9=Priority 글자색 (P0=Red, P1=Orange, P2=Gold, P3=Green), 12pt bold |

#### Section 3: Test Case Result (Row 10–17+)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 10 | A10:K10 | `3. Test Case Result` | Section Header |
| 11 | A:B, C:D, E:F, G:H, I:J, K단독 | Total / PASS / FAIL / N/A / N/T / Success Rate | Table Header |
| 12 | A:B, C:D, E:F, G:H, I:J, K단독 | 데이터 | Data Cell, center |
| 13 | C:D, E:F, G:H, I:J (A,B,K 단독) | Category / Total / PASS / FAIL / N/A / N/T / Success Rate | Table Header |
| 14–17 | 동일 머지 | TC별 데이터 | Category left/wrap, 수치 center, 교차 행 색상 |
| {etc} | A:K 전체 머지 | `etc.` | Sub-section Label |
| {etc}+1 | B:F, G:J (A,K 단독) | No. / Category / Description / Result | Table Header |
| {etc}+2~ | 동일 머지 | 데이터 | No. center, Category/Desc left, Result center |

#### Section 4: Verification Details

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| {S4} | A:K 전체 머지 | `4. Verification Details (Summary)` | Section Header |
| {S4}+1 | B:J (A,K 단독) | Test Area / Key Verification Items / Result | Table Header |
| {S4}+2~ | B:J (A,K 단독) | 검증 분야별 데이터 | 교차 행 색상, 번호 목록 형식 |

### 9.3. 조건부 서식

| 대상 | 조건 | 배경색 | 글자색 | 굵기 |
| :--- | :--- | :--- | :--- | :--- |
| A4 (Verdict) | `PASS` | `#34A853` | 흰색 | bold |
| | `CONDITIONAL PASS` | `#FFC107` | 흰색 | bold |
| | `FAIL` | `#D11A1A` | 흰색 | bold |
| | `ON HOLD` | `#999999` | 흰색 | bold |
| K12, K14:K17+ (Success Rate) | E열(FAIL)=0 | — | `#1C65C0` | bold |
| | E열(FAIL)>0 | — | `#CD1C1C` | bold |
| K{S4}+2~ (Result) | Pass | — | `#1E8449` | bold |
| | Fail | — | `#CD1C1C` | bold |
| | N/A | — | `#7F8C8D` | bold |

### 9.4. Defect Summary — Priority 매핑 및 컬러

#### 9.4.1. Jira Priority → QA Report 매핑

Jira Bug `priority` 필드 → P0–P3 매핑 후 Defect Summary 집계.

| Jira Priority | QA Report | 의미 |
| :--- | :--- | :--- |
| Highest | **P0** | Blocker — 서비스 불가 치명적 결함 |
| High | **P1** | Critical — 핵심 기능 장애 |
| Medium | **P2** | Major — 주요 기능 이슈 |
| Low | **P3** | Minor — 경미한 UI/UX 이슈 |

* 글자색 4단계: P0=Red(`#FF0000`), P1=Orange(`#FF8C00`), P2=Gold(`#DAA520`), P3=Green(`#4CAF50`).
* Jira `Lowest` → P3 매핑.
* 집계 대상: 대상 Epic 하위 `issuetype = Bug` 전체 (상태 무관)

#### 9.4.2. 자동 집계 절차

1. 전체 버그 조회 JQL — **구조에 따라 선택** (2026-07-21 스프린트 전환 개정):
   - **스프린트/Release Train 구조 (현행)**: 릴리스 결산 = `affectedVersion = "Release {N}" AND issuetype = Bug AND reporter = {QA 계정}` / 진행 중 현황 = `sprint = "{스프린트명}" AND issuetype = Bug AND reporter = {QA 계정}` (affectedVersion = 검출 기준 anchor — QA 입력값. fixVersion 은 dev 소유라 집계 기준으로 쓰지 않음)
   - 舊 에픽 버킷 구조: `parent = {Epic Key} AND issuetype = Bug`
   **페이지네이션 필수:** `next_page_token` 존재 시 모든 페이지 순회. (MCP 도구 기본 limit 50건 → 50건 초과 시 누락 발생)
2. 각 이슈 `priority.name` → 위 매핑표 기준 P0–P3 분류.
3. QA Result 시트 반영:
   - **C11 (Detected Defects 값):** 전체 건수
   - **C13 (P0):** Highest 건수
   - **E13 (P1):** High 건수
   - **G13 (P2):** Medium 건수
   - **I13 (P3):** Low + Lowest 건수
   - **K13 (Total):** 전체 건수
4. **G11 (Jira Dashboard):** 사용자 수동 입력. (API 자동 생성 불가)

### 9.5. Data Validation / 숫자 포맷

| 대상 | 유형 | 값 |
| :--- | :--- | :--- |
| A5 | 드롭다운 | `PASS` / `CONDITIONAL PASS` / `FAIL` / `ON HOLD` |
| D5 | 날짜 포맷 | `yyyy-MM-dd` |
| K17, K21:K22 | 백분율 | `0.0%` (소수점 1자리 반올림) |

### 9.6. 열 너비 / 행 높이

#### 열 너비 (px)

| A | B | C | D | E | F | G | H | I | J | K |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 190 | 140 | 80 | 60 | 80 | 60 | 80 | 60 | 80 | 60 | 90 |

#### 행 높이 (px) — 기본값(21) 이외

| Row | 높이 | 용도 |
| :--- | :--- | :--- |
| 1 | 40 | Title |
| 3 | 30 | Section Header |
| 4 | 32 | Table Header |
| 7 | 28 | Sub-section Label |
| 8 | 240 | QA 의견 본문 (멀티라인) |
| 10 | 30 | Section Header |
| 11 | 36 | Defect 라벨+값 |
| 12 | 28 | Priority Header |
| 15 | 30 | Section Header |
| 16, 19, 20, 24, 25 | 28 | Table Header / Sub-section |
| 29 | 30 | Section Header |
| 30 | 28 | Table Header |
| 31+ | 자동 | Verification (`autoResizeDimensions`) |

* Section 4 데이터 행(Row 31~끝) 높이 = `autoResizeDimensions`로 내용 맞춰 자동 피팅. 시트 생성 후 데이터 입력 시 `startIndex: 30, endIndex: {마지막 데이터 행}` 범위로 1회 실행.

### 9.7. 작성 규칙

* **언어:** 헤더/라벨 = 영문, 내용(QA 의견, 검증 항목) = 한국어
* **검증 항목:** 콤마 나열 금지 → **번호 목록**(1. 2. 3. ...) + 마지막 줄 `— N건 전체 PASS/N/A` 요약
* **Verdict:** 전체 대문자 (`PASS`, `CONDITIONAL PASS`, `FAIL`, `ON HOLD`)
* **표기 통일 (2026-07-03 피드백 반영):**
  - `e-Cash` — 고객사 커뮤니케이션 용어. `E-Cash` 금지.
  - 결과 표기는 문서 전체 `PASS`/`FAIL` 대문자 통일 (요약줄 "— N건 전체 PASS" 포함). `Pass`/`PASS` 혼용 금지.
  - **에러코드**: 검증 항목에 부가 표기 금지 (예: "(0002)", "(CHIP-ACCEPTOR-0003)"). 단, **에러 발생 자체가 검증 대상**인 항목(예: RFID 200018~200021 차단)은 유지.
  - 결함 처리 문구: "추후 수정 진행, 이번 릴리즈와 무관한 이슈" 형태 — "후속 진행" 같은 모호 표현 지양.
  - 운영 리스크는 "고객 공유 필요" 대신 **Known Issue 섹션**으로 프레이밍 (Disposition 명기).

### 9.8. 서식 적용 순서 (체크리스트)

| # | 항목 | 비고 |
| :--- | :--- | :--- |
| 1 | 데이터 입력 | 값, 수식 |
| 2 | 머지 | 전 영역 셀 병합 |
| 3 | 폰트/색상/정렬 | Section별 batch_format_cells |
| 4 | 조건부 서식 | Verdict, Success Rate, Result |
| 5 | Data Validation | 드롭다운, 날짜/백분율 포맷 |
| 6 | 행 높이 / 열 너비 | Python `updateDimensionProperties` |
| 7 | **테두리 (반드시 마지막)** | 7개 테이블 영역, `#B3B3B3` thin |

### 9.9. 자동화 로직 — 데이터 수집 및 생성 규칙

#### 9.9.0. 핵심 원칙

* **사실 기반 작성:** QA Result 모든 데이터 = QA Workspace(Google Sheets TC 시트, Jira) **실존 값** 기반. 유추/허위 금지.
* **수동/자동 구분:** 아래 표 따라 입력 방식 구분.

| 영역 | 입력 방식 | 데이터 소스 |
| :--- | :--- | :--- |
| Verdict (A5) | **수동** — 엔지니어 판단 | — |
| Date (D5) | **수동** — 엔지니어 입력 | — |
| QA Lead (G5) | **수동** — 엔지니어 입력 | — |
| Remarks (J5) | **수동** — 엔지니어 입력 | — |
| QA Opinion (A8) | **자동 생성** | TC Result + Jira Defect 분석 |
| Defect Summary (Row 11–13) | **자동 집계** | Jira Bug (Section 9.4.2) |
| Test Case Result (Row 16–22) | **자동 집계** | TC 시트 데이터 |
| etc. (Row 25–27) | **수동** — 엔지니어 입력 | — |
| Verification Details (Row 30–39) | **자동 생성** | QA Plan + TC 시트 데이터 |

#### 9.9.1. Test Case Result — 데이터 소스 매핑 (Section 3)

TC 시트에서 Test Case Result 데이터 수집 규칙.

* **대상 시트 식별:** 담당자 입력 **Test Case 시트명** 기반, 동일 스프레드시트 내 해당 시트 읽음.
* **Category 표시명:** 담당자 입력 Test Case 시트명 그대로 Category 사용.
* **Success Rate 정의:** `PASS / (PASS + FAIL)` — N/A·N/T 분모 제외. 실행 테스트 품질만 측정, 미수행 범위 = N/A·N/T 컬럼 + QA Opinion에서 별도 확인.
* **집계 절차:**
  1. 각 TC 시트 Test Result(I열) 집계: PASS / FAIL / N/A / N/T 건수.
  2. **Row 17 (전체 합산):** 모든 TC 시트 합계 — Total, PASS, FAIL, N/A, N/T, Success Rate
  3. **Row 21~22+ (Category별):** TC 시트별 Category명(시트명), Total, PASS, FAIL, N/A, N/T, Success Rate
* **행 수 가변:** Category 수 따라 Row 21 이후 행 증가. 이후 Section(etc., Verification Details) 시작 행도 함께 조정.

**Row 21+ (Category별) — TC 시트 참조 수식:**

> `{r}` = Category 행 번호, `{시트명}` = TC 시트명, `{end}` = TC 시트 데이터 마지막 행

| 셀 | 수식 | 설명 |
| :--- | :--- | :--- |
| A{r} | *(시트명)* | Category명 |
| B{r} | `=COUNTA('{시트명}'!I9:I{end})` | Total (결과 입력된 TC 건수) |
| C{r} | `=COUNTIF('{시트명}'!I9:I{end},"Pass")` | PASS 건수 |
| E{r} | `=COUNTIF('{시트명}'!I9:I{end},"Fail")` | FAIL 건수 |
| G{r} | `=COUNTIF('{시트명}'!I9:I{end},"N/A")` | N/A 건수 |
| I{r} | `=COUNTIF('{시트명}'!I9:I{end},"N/T")` | N/T 건수 |
| K{r} | `=IF((C{r}+E{r})=0,"",C{r}/(C{r}+E{r}))` | Success Rate |

**Row 17 (전체 합산) — Category 행 합산 수식:**

> `{last}` = 마지막 Category 행 번호

| 셀 | 수식 | 설명 |
| :--- | :--- | :--- |
| A17 | `=SUM(B21:B{last})` | Total 합산 (A:B 머지 셀) |
| C17 | `=SUM(C21:C{last})` | PASS 합산 |
| E17 | `=SUM(E21:E{last})` | FAIL 합산 |
| G17 | `=SUM(G21:G{last})` | N/A 합산 |
| I17 | `=SUM(I21:I{last})` | N/T 합산 |
| K17 | `=IF((C17+E17)=0,"",C17/(C17+E17))` | Success Rate |

#### 9.9.2. QA Opinion — 자동 생성 (Section 1)

Test Case Result + Jira Defect 분석 → QA Opinion 본문 자동 생성.

* **입력 데이터:**
  - Test Case Result: Category별 PASS/FAIL/N/A/N/T 건수, Success Rate
  - Jira Defect: Epic 하위 Bug 목록, Priority별 건수, 현재 상태(Open/Resolved 등)
* **작성 구조:**
  1. **전체 요약:** 총 TC 건수, 전체 Success Rate, 검출 Defect 건수 → 1–2문장 요약
  2. **Category별 결과:** Category별 PASS/FAIL 현황 + 주요 이슈 요약
  3. **미해결 Defect:** FAIL 또는 Open 상태 Defect 존재 시 Priority별 언급
  4. **종합 의견:** 테스트 결과 기반 품질 상태 평가
* **작성 원칙:**
  - 실제 TC 결과 + Jira 데이터 확인 사실만 기술.
  - 수치(건수, 비율) = 실제 집계값 사용.
  - 추측/가정 금지.

#### 9.9.3. Verification Details — Test Area 매핑 (Section 4)

QA Plan(Section 4) + TC 시트 데이터 기반 Verification Details 자동 생성.

* **Test Area (A열):**
  - QA Plan(Section 4.2) 도출 **검증 분야(대분류)** = 기본 Test Area.
  - TC 시트 대분류(B열) 매핑 → 해당 분야 TC 실존 확인.
* **Key Verification Items (B:J열):**
  - 해당 Test Area(대분류) 소속 TC 분석 → **핵심 검증 항목** 도출.
  - TC 중분류(C열), 소분류(D열) 참조 → 수행 검증 구체 기술.
  - 번호 목록(1. 2. 3. ...) 형식, 마지막 줄 `— N건 전체 Pass/N/A` 요약.
* **Result (K열):**
  - 해당 Test Area 소속 TC Test Result(I열) 참조 판정.
  - 전체 Pass → `Pass`, FAIL 1건이라도 → `Fail`, 해당 TC 없음 → DD`N/A`.
* **행 수:** QA Plan 검증 분야 수 따라 Row 31 이후 행 가변. 행 높이 = Key Verification Items 항목 수 비례(항목 1개당 약 18px).

#### 9.9.4. etc. — 수동 입력 (Section 3 하위)

* etc. 항목(Row 25–27) = 엔지니어 직접 입력.
* 자동 채움/유추 금지.
* 빈 상태로 시트 생성, 필요 시 엔지니어 추가.

---

## 10. QA Status Report

QA 진행 중 실시간 현황 공유 리포트 Google Sheets 작성. 시트명 `QA Status` 지정.

> **QA Result와 차이:** QA Result(Section 9) = QA 완료 후 Sign-off 용도, QA Status = **진행 중** QA 현황 보고 용도. Test Execution Progress(진행률), Open/Fixed Defect 상세 목록, 잔여 작업 등 실시간 추적 항목 포함.

### 10.1. 디자인 시스템

#### 10.1.1. 색상 / 폰트 / 정렬

| 요소 | 배경색 | 글자색 | 폰트 | 크기 | 굵기 | 정렬(가로/세로) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Title (Row 1) | `#1B2A3D` | 흰색 | IBM Plex Sans | 16pt | bold | 왼쪽/중앙 |
| Subtitle (Row 2) | `#34495E` | `#BDC3C7` | IBM Plex Sans | 10pt | normal | 왼쪽/중앙 |
| Section Header | `#2C3E50` | 흰색 | IBM Plex Sans | 11pt | bold | 왼쪽/중앙 |
| Table Header | `#EAECEE` | 기본(검정) | IBM Plex Sans | 10pt | bold | 가운데/중앙 |
| Overall Label (A5) | `#34495E` | 흰색 | IBM Plex Sans | 10pt | bold | 가운데/중앙 |
| Overall Value (Row 6) | 흰색 | 기본 | IBM Plex Sans | 12pt | bold | 가운데/중앙 |
| Data Cell | 흰색 | 기본 | IBM Plex Sans | 10pt | normal | 가운데/중앙 |
| Category Data (A열) | 교차색상 | 기본 | IBM Plex Sans | 10pt | normal | 왼쪽/중앙 |
| Percent Value (Progress/SR) | 교차색상 | 기본 | IBM Plex Sans | 10pt | **bold** | 가운데/중앙 |

* **세로 맞춤:** 전체 시트 `MIDDLE` 통일
* **교차 행 색상:** 홀수 `#F8F9FA` / 짝수 흰색

#### 10.1.2. Defect Status 카드 색상

| 항목 | 배경색 | 글자색 | 용도 |
| :--- | :--- | :--- | :--- |
| Total | 흰색 | 기본 | 전체 건수 |
| Open | `#FDEBD0` | `#C0392B` (Red) | 미해결 건수 |
| Fixed (QA 대기) | `#D5F5E3` | `#2980B9` (Blue) | 수정 완료, QA 검증 대기 |
| Reject | `#EBDEF0` | `#8E44AD` (Purple) | 반려 건수 |
| Closed | `#D5F5E3` | `#27AE60` (Green) | 검증 완료 건수 |
| Resolution Rate | 흰색 | `#2980B9` (Blue) | (Closed+Reject)/Total |

#### 10.1.3. 테두리

* **스타일:** SOLID thin, 색상 `#D5D8DC`
* **적용 대상:** 7개 테이블 영역 (Row 4:5, 6:9, 11:12, 13:14, 16:{Open끝}, {S4 Table}:{S4 Data끝}, {S5 Table}:{S5 Data끝})
* **적용 순서:** **모든 서식 후 마지막** 실행.

### 10.2. 시트 레이아웃

#### Row 1–2: Title & Subtitle

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 1 | A1:K1 | `{프로젝트명} — QA Status` | Title |
| 2 | A:C, D:F, G:K | `Report Date: {날짜}` / `Epic: {에픽키}` / `Version: {버전}` | Subtitle |

> **공백 행 없음:** Section 구분 = Section Header(`#2C3E50`). 빈 행 삽입 금지.

#### Section 1: Test Execution Progress (Row 3–9)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 3 | A3:K3 | `1. Test Execution Progress` | Section Header |
| 4 | A:B, C:D, E단독, F단독, G단독, H단독, I단독, J:K | Overall / Total TC / Pass / Fail / N/A / Not Tested / Retest / Progress | Overall Label(A:B) + Table Header |
| 5 | A:B, C:D, E단독, F단독, G단독, H단독, I단독, J:K | (빈값) / 합산수식 / … / 진행률% | Overall Value (12pt bold) |
| 6 | A:B, C:D, E단독, F단독, G단독, H단독, I단독, J단독, K단독 | Category / Total / Pass / Fail / N/A / Not Tested / Retest / Progress / Success Rate | Table Header |
| 7–9 | 동일 머지 | TC 시트별 데이터 | Data Cell, 교차 행 색상, Progress·SR = bold % |

* **Pass:** Pass 건수
* **Fail:** Fail 건수
* **N/A:** N/A 건수 (환경 미비 등 수행 불가)
* **Not Tested:** N/T 건수
* **Retest:** Retest 건수 (수정 후 재검증 대기)
* **Progress:** (Pass + Fail + N/A) / Total (백분율) — N/T·Retest 미실행으로 제외
* **Success Rate:** Pass / (Pass + Fail) (백분율)

#### Section 2: Defect Status (Row 10–14)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 10 | A10:K10 | `2. Defect Status` | Section Header |
| 11 | A:B, C:D, E:F, G:H, I:J, K단독 | Total / Open / Fixed (QA 대기) / Reject / Closed / Resolution Rate | Table Header |
| 12 | 동일 머지 | 값 | Defect 카드 색상 (10.1.2), 14pt bold |
| 13 | A단독, B:C, D:E, F:G, H:I, J단독, K단독 | Priority / P0 (Blocker) / P1 (Critical) / P2 (Major) / P3 (Minor) / Total / Comment | Table Header |
| 14 | 동일 머지 | 값 | Priority 글자색 (P0=Red, P1=Orange, P2=Gold, P3=Green), 12pt bold |

* **Resolution Rate:** `(Closed + Reject) / Total` — 백분율 `0.0%` 포맷, Blue bold
* **Comment (K14):** Priority 특기사항 (예: "P0 1건 Open (PROJ-XXXX)"), 9pt wrap

#### Section 3: Open & Reopened Defects (Row 15~)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| 15 | A15:K15 | `3. Open & Reopened Defects` | Section Header |
| 16 | A:B, C단독, D단독, E:K | Key / Priority / Status / Summary | Table Header |
| 17~ | 동일 머지 | Open/Reopened 버그 목록 | Data Cell, wrap |

* **Priority (C열):** 조건부 서식 P0~P3 글자색 적용
* **Status (D열):** 조건부 서식 상태별 배경색 — `진행 중`=`#FFF3CD`, `QA 배포됨`=`#D5F5E3`, `다시 열림`=`#F8D7DA`, `NEW`=`#D1ECF1`
* **행 수 가변:** Open 건수 따라 행 증가.
* 행 높이 = `autoResizeDimensions` 자동 피팅

#### Section 4: Fixed — QA 검증 대기

> **시작 행 계산:** Section 3 데이터 마지막 행 + 1 (빈 행 없이 이어짐)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| {S4} | A:K 전체 머지 | `4. Fixed — QA 검증 대기` | Section Header |
| {S4}+1 | A:B, C단독, D:K | Key / Priority / Summary | Table Header |
| {S4}+2~ | 동일 머지 | Fixed 상태 버그 목록 | Data Cell, 교차 행 색상, wrap |

* **Priority (C열):** 조건부 서식 P0~P3 글자색 적용
* **행 수 가변:** Fixed 건수 따라 행 증가.
* 행 높이 = `autoResizeDimensions` 자동 피팅

#### Section 5: Remaining Work & Next Steps

> **시작 행 계산:** Section 4 데이터 마지막 행 + 1 (빈 행 없이 이어짐)

| Row | 머지 | 내용 | 스타일 |
| :--- | :--- | :--- | :--- |
| {S5} | A:K 전체 머지 | `5. Remaining Work & Next Steps` | Section Header |
| {S5}+1 | A단독, B:H, I:K | No. / Item / ETA | Table Header |
| {S5}+2~ | 동일 머지 | 잔여 작업 목록 | Data Cell, wrap |

* **ETA (Estimated Time of Achievement):** 해당 작업 완료 목표일. 예: `2026-04-08`, `4/10 (수)`
* **ETA:** 엔지니어 수동 입력.
* **행 수 가변:** 잔여 작업 수 따라 행 증가.

#### 가변 행 계산 규칙

Section 3~5 = 데이터 건수 따라 행 가변. 각 Section 시작 행 = **이전 Section 데이터 마지막 행 + 1** (빈 행 없이 이어짐).

* **서식 적용 시 행 인덱스 계산 예시:**
  - Section 3 데이터: Row 17 ~ Row {17 + Open건수 - 1}
  - Section 4 Header: Row {17 + Open건수} ← **바로 다음 행**
  - Section 4 Table Header: Row {17 + Open건수 + 1}
  - Section 4 데이터: Row {17 + Open건수 + 2} ~
* **서식 범위 endIndex = 데이터 마지막 행 포함 필수.** Google Sheets API 범위 = `[startIndex, endIndex)` (exclusive) → 데이터 N건 시 `endIndex = startIndex + N`. 마지막 행 누락 시 교차 행 색상, 머지, 테두리 빠짐.
* **가변 Section 머지 범위가 타 Section 데이터 영역 침범 금지.** Section Header 머지(`A:K 전체 머지`) = 해당 Header 행만 적용.

### 10.3. 조건부 서식

| 대상 | 조건 | 적용 | 비고 |
| :--- | :--- | :--- | :--- |
| Section 3 Priority (C열) | `P0` | 글자색 `#FF0000`, bold | Red |
| | `P1` | 글자색 `#FF8C00`, bold | Orange |
| | `P2` | 글자색 `#DAA520`, bold | Gold |
| | `P3` | 글자색 `#4CAF50`, bold | Green |
| Section 3 Status (D열) | `진행 중` | 배경색 `#FFF3CD`, bold | 노랑 |
| | `QA 배포됨` | 배경색 `#D5F5E3`, bold | 연두 |
| | `다시 열림` | 배경색 `#F8D7DA`, bold | 분홍 |
| | `NEW` | 배경색 `#D1ECF1`, bold | 하늘 |
| Section 4 Priority (C열) | P0~P3 | Section 3 동일 | — |

### 10.4. 열 너비 / 행 높이

#### 열 너비 (px)

| A | B | C | D | E | F | G | H | I | J | K |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 80 | 80 | 60 | 60 | 60 | 55 | 50 | 65 | 60 | 75 | 110 |

#### 행 높이 (px) — 기본값(21) 이외

| Row | 높이 | 용도 |
| :--- | :--- | :--- |
| 1 | 48 | Title |
| 2 | 28 | Subtitle |
| 3 | 32 | Section 1 Header |
| 5 | 40 | Overall Value |
| 10 | 32 | Section 2 Header |
| 15 | 32 | Section 3 Header |
| {S4} | 32 | Section 4 Header (가변) |
| {S5} | 32 | Section 5 Header (가변) |
| Section 3 데이터 | 자동 | Open Defects (`autoResizeDimensions`) |
| Section 4 데이터 | 자동 | Fixed Defects (`autoResizeDimensions`) |

### 10.5. 자동화 로직 — 데이터 수집 및 생성 규칙

#### 10.5.0. 핵심 원칙

* QA Result(Section 9) 동일 — **사실 기반 작성** 원칙.
* TC 시트 + Jira 데이터 실시간 수집 작성.

#### 10.5.1. Test Execution Progress (Section 1)

* TC 시트 I열(Test Result) 집계 → Category별 데이터 산출.
* **Row 5 (Overall):** Category 행(Row 7~9) 합산 수식 사용.
* **Row 7+ (Category별) — 수식:**

> `{r}` = Category 행 번호, `{시트명}` = TC 시트명, `{end}` = TC 시트 데이터 마지막 행

| 셀 | 수식 | 설명 |
| :--- | :--- | :--- |
| A{r} | *(시트명)* | Category명 |
| C{r} | `=COUNTA('{시트명}'!I9:I{end})` | Total |
| E{r} | `=COUNTIF('{시트명}'!I9:I{end},"Pass")` | Pass |
| F{r} | `=COUNTIF('{시트명}'!I9:I{end},"Fail")` | Fail |
| G{r} | `=COUNTIF('{시트명}'!I9:I{end},"N/A")` | N/A |
| H{r} | `=COUNTIF('{시트명}'!I9:I{end},"N/T")` | Not Tested |
| I{r} | `=COUNTIF('{시트명}'!I9:I{end},"Retest")` | Retest |
| J{r} | `=IF(C{r}=0,"",(E{r}+F{r}+G{r})/C{r})` | Progress |
| K{r} | `=IF((E{r}+F{r})=0,"",E{r}/(E{r}+F{r}))` | Success Rate |

#### 10.5.2. Defect Status (Section 2)

* Jira `parent = {Epic Key} AND issuetype = Bug` JQL로 전체 버그 조회. **페이지네이션 필수.**
* 상태별 분류:
  - **Open:** `NEW`, `진행 중`, `QA 배포됨`, `다시 열림`
  - **Fixed (QA 대기):** `FIXED`
  - **Reject:** `REJECT`
  - **Closed:** `완료`
* **Resolution Rate:** `(Closed + Reject) / Total`
* Priority별 건수 = Section 9.4.1 매핑표 동일 (Highest=P0, High=P1, Medium=P2, Low/Lowest=P3)

#### 10.5.3. Open & Fixed Defect 목록 (Section 3, 4)

* Jira 조회 결과에서 Open/Fixed 상태 이슈 추출 → 목록 작성.
* Key, Priority, Status(Open만), Summary 표시.
* Priority 순(P0→P3) 정렬.

#### 10.5.4. Remaining Work (Section 5)

* 아래 항목 기본 생성:
  1. FIXED N건 리그레션 테스트
  2. N/T N건 (미수행 영역 요약) 테스트 수행
  3. Bug fix 및 리그레션 테스트 준비
  4. Open Defect N건 수정 후 재검증
  5. 전체 리그레션 테스트
* **N건:** 실제 집계값 반영. 미수행 영역 = 주요 카테고리 괄호 안 요약.
* **Owner / ETA:** 엔지니어 수동 입력. 자동 채움 금지.

### 10.6. 서식 적용 순서 (체크리스트)

| # | 항목 | 비고 |
| :--- | :--- | :--- |
| 1 | 데이터 입력 | 값, 수식 |
| 2 | 머지 | 전 영역 셀 병합 |
| 3 | 폰트/색상/정렬 | Section별 batch_format_cells |
| 4 | 조건부 서식 | Priority 글자색, Status 배경색 |
| 5 | 열 너비 / 행 높이 | `updateDimensionProperties`, `autoResizeDimensions` |
| 6 | **테두리 (반드시 마지막)** | 7개 테이블 영역, `#D5D8DC` thin |
* 빈 상태로 시트 생성, 필요 시 엔지니어 추가.

---

## 11. PDF 산출 룰 (내부 공유 표준)

> QA Report 를 PDF 스냅샷으로 뽑아 내부 공유하는 것을 표준 산출물로 한다. (고객사 공유판은 별도 결정 전까지 스코프 아웃 — 2026-07-02)

### 11.1. 트리거

| 시점 | 산출물 |
| :--- | :--- |
| Release Train **QA OK-Sign** | QA Result Report PDF (§11.4 템플릿) |
| **Hotfix 검증 완료** | Hotfix QA Report PDF (§11.4 템플릿, Hotfix 변형) |
| **현장(UAT) Sign-off** | UAT QA Report PDF (§11.4 템플릿, UAT 변형) |
| 그 외 | 요청 기반 |

> 2026-10-16: 리포트 HTML 템플릿을 이 문서 §11.4~§11.6 으로 통합했다. 따로 있던 Hotfix 템플릿 문서는 없앴다 — 세 종류가 같은 뼈대를 쓰고 섹션만 빠진다.

### 11.2. 네이밍

* Release: `{버전}_QA_Report_{YYYY-MM-DD}.pdf`
* Hotfix: `{버전}_Hotfix_QA_Report_{YYYY-MM-DD}.pdf` (기존 룰 유지)
* UAT: `{버전}_UAT_QA_Report_{YYYY-MM-DD}.pdf`
* `{버전}` = 배포 차수(Version 페이지 표기, 예 `10.1th`, `11th_S01`). `{YYYY-MM-DD}` = 검증 완료일.

### 11.3. 원칙

* **원본-파생**: PDF 는 파생물. 수정은 항상 원본(HTML/시트) → 재출력. PDF 직접 수정 금지.
* **생성 방법 (표준)**: 팀 리포트 폴더에 **HTML 작성 → headless 브라우저 인쇄 스크립트**. Google Sheets export 방식은 품질 낮아 사용 금지.
  - ⚠️ **인쇄 스크립트에 파일명을 반드시 인자로 준다.** 인자 없이 돌면 폴더 전체가 재렌더된다.
  - 섹션 구성과 HTML 뼈대는 §11.4, 변환 스크립트는 §11.5, 생성기가 지킬 검사는 §11.6
  - 데이터 정합: 수치·Verdict 는 QA Result 시트 탭과 일치시킬 것 (시트 = 데이터 원본, HTML = 발행본)
* **스타일 (2026-08-21 규약 변경)**: HTML 에 `<style>` 를 새로 짜지 않는다. 공용 CSS
  [`assets/report.css`](./assets/report.css) 한 벌을 링크하고 **클래스만** 쓴다.
  발행 전 **디자이너 세션 검토**를 거친다 — 규약 상세 [`REPORT_STYLE_POLICY.md`](./REPORT_STYLE_POLICY.md).
  > 이전 판은 특정 산출물 파일(`10.1th_Hotfix_...html`)을 "스타일 원형"으로 지목했다.
  > 산출물이 스타일 원본을 겸하면 그 파일을 고칠 때마다 규격이 조용히 바뀐다. 폐기.
* ⚠️ **발행 전 글리프 감사 (필수)**: headless 브라우저 인쇄에서 `−`(U+2212) 등 일부 문자가
  PDF 에서 **소실**된다. `−` 는 ASCII 하이픈과 육안 구분이 안 돼 아래 "최종 검수"로 못 잡는다.
  절차는 [`VERIFICATION_GUIDE.md`](./VERIFICATION_GUIDE.md) §4.
* **보관**: 팀 리포트 폴더 + 사내 저장소만. 외부 호스팅 금지 (고객 데이터 민감성 정책과 일관).
* 발송 전 숫자·버전·날짜 최종 검수 1회. **(육안 검수는 글리프 소실을 못 잡는다 — 위 항목 별도 수행)**

### 11.4. 리포트 HTML 템플릿 (Sign-off · Hotfix · UAT 공통)

> 구조의 정답은 실제로 발행한 스프린트 Sign-off 리포트(2026-09-17, A4 7쪽, CONDITIONAL PASS)다. 아래 뼈대는 그 리포트에서 데이터와 고객 정보를 걷어 낸 것이다.
> **이 템플릿을 쓰는 세션은 내용만 쓴다.** 스타일은 [`assets/report.css`](./assets/report.css) 한 벌이고 HTML 은 클래스만 쓴다(§11.3 · [`REPORT_STYLE_POLICY.md`](./REPORT_STYLE_POLICY.md)).

#### 11.4.1. 섹션 구성과 종류별 차이

| # | 블록 | 내용 | Sign-off | Hotfix | UAT |
| :--- | :--- | :--- | :---: | :---: | :---: |
| — | 표지 `.cover` | 리포트 종류 · 제목 · 한 줄 요약 · 대상 모듈 버전 칩 · Date/QA Lead/Sprint/Scope/Environment | ● | ● | ● |
| — | 판정 히어로 `.verdict` | 판정 도장 + 조건 목록 + 판정 문장 | ● | ● | ● |
| 01 | QA Opinion | 수치 타일 4칸(TC·검출 결함·수정 완료·나머지) + 조건 근거 콜아웃 + 환경 참고 콜아웃 | ● | ● | ● |
| 02 | Release Version | 모듈별 버전 정의 그리드 + 출처 각주 | ● | ● | ○ |
| 03 | Test Case Result | KPI 5칸 + 시트별 결과 비율 바 + 집계 표 + N/A 사유 | ● | ○ | ● |
| 04 | Defect Summary | 결함 요약 문장 + 우선순위 축 + 상태별 목록 + 결함 표 | ● | ○ | ○ |
| 05 | Verification Details | 검증 영역별 번호 목록 + 소계 + 결과 칩 | ● | ● | ● |
| 06 | 판정 및 잔여 항목 | Sign-off 조건 · Known Issue/보류 결함 블록 | ● | ● | ● |
| — | 부속 데이터 | UAT 의 성능 측정 등 별도 데이터(예: 실물 인식률) | — | — | ● |

● 필수 · ○ 해당 있을 때만 · — 없음. **번호는 빠진 섹션을 건너뛰지 않고 다시 매긴다.**

#### 11.4.2. 판정 · 결과 클래스

| 판정 | 히어로 | 도장 문구 |
| :--- | :--- | :--- |
| `PASS` | `.verdict` | `PASS` |
| `CONDITIONAL PASS` | `.verdict.is-hold` | 라벨 `Conditional` + 값 `PASS` |
| `FAIL` | `.verdict.is-fail` | `FAIL` |
| `ON HOLD` | `.verdict.is-hold` | 라벨 `On hold` |

| 결과·상태 | 칩 |
| :--- | :--- |
| PASS · Fixed | `.chip.c-ok` |
| FAIL · Open | `.chip.c-bad` |
| N/A · Known Issue · Won't Fix · Postponed | `.chip.c-na` |
| N/T · 정보 | `.chip.c-info` |

* 색 값은 `assets/report.css` 안에만 있다. **여기에 hex 를 다시 적지 않는다** — 두 군데 적히는 순간 어느 쪽이 원본인지 알 수 없다.
* 결과 비율 바의 폭(`style="width:…%"`)만은 데이터라 인라인을 허용한다. 그 외 인라인 `style=` 금지.

#### 11.4.3. HTML 뼈대

반복 블록은 한 줄씩만 적었다. `{{…}}` 는 시트·Jira 에서 읽어 채운다.

```html
<!DOCTYPE html>
<html lang="ko"><head>
<meta charset="UTF-8">
<title>{{REPORT_TITLE}}</title>
<link rel="stylesheet" href="assets/report.css">
</head><body>

<div class="cover">
  <div class="eyebrow">QA Sign-off Report</div>              <!-- Hotfix: QA Hotfix Report / UAT: UAT Sign-off Report -->
  <h1>{{RELEASE}} · {{SPRINT}} — {{CUSTOMER}}</h1>
  <p class="deck">{{한 줄 요약 — 범위와 판정}}</p>
  <div class="mods"><span class="mod">{{모듈}} <b>{{버전}}</b></span></div>
  <div class="meta">
    <div><dt>Date</dt><dd>{{DATE}}</dd></div>
    <div><dt>QA Lead</dt><dd>{{작성자}}</dd></div>
    <div><dt>Sprint</dt><dd>{{SPRINT}}</dd></div>
    <div><dt>Scope</dt><dd>{{N}}개 시트 {{TOTAL}} TC</dd></div>
    <div><dt>Environment</dt><dd>{{검증 환경 · 운영 장비와 다르면 그 사실}}</dd></div>
  </div>
</div>

<div class="verdict is-hold">                                 <!-- §11.4.2 -->
  <div class="stamp"><div class="lbl">Conditional</div><div class="val">PASS</div></div>
  <div class="body">
    <div class="hd">조건부 통과 — CONDITIONAL PASS</div>
    {{범위 한 문장}}<ol>
      <li><b>{{조건 대상}}</b> — {{무엇을 언제 어디서 추가 검증}}</li>
    </ol>
    <b>{{판정 문장 — 사람이 쓴 원문 그대로}}</b>
  </div>
</div>

<h2><span class="num">01</span>QA Opinion</h2><div class="rule"></div>
<div class="stats">
  <div class="stat"><div class="v">{{TOTAL}}<small> TC</small></div><div class="k">{{N}}개 시트 · FAIL {{F}}</div><div class="s">PASS {{P}} / N/A {{NA}} / N/T {{NT}} · Success Rate {{RATE}}%</div></div>
  <div class="stat"><div class="v">{{D}}<small> 건</small></div><div class="k">검출 Defect</div><div class="s">P0 {{}} / P1 {{}} / P2 {{}} / P3 {{}}</div></div>
  <div class="stat"><div class="v">{{FIXED}}<small> 건</small></div><div class="k">수정 완료</div><div class="s">{{P0 처리 한 줄}}</div></div>
  <div class="stat"><div class="v">{{REST}}<small> 건</small></div><div class="k">나머지</div><div class="s">Known Issue {{}} · 수정 안 함 {{}} · Postponed {{}}</div></div>
</div>
<div class="note n-warn"><span class="lbl">조건 근거</span><ol><li>{{QA 리드 의견 원문}}</li></ol></div>
<div class="note n-flat"><span class="lbl">환경 참고</span><ul><li>{{장비·환경 특기}}</li></ul></div>

<h2><span class="num">02</span>Release Version</h2><div class="rule"></div>
<dl class="kv nb">
  <dt>{{제품}} · {{모듈}}</dt><dd class="ver"><span class="new">{{버전}}</span></dd>   <!-- 바뀐 것: <span class="old">구</span><span class="arw">→</span><span class="new">신</span> -->
</dl>
<div class="foot-note">* 출처: {{버전 페이지 이름 · 판 번호}}</div>

<h2><span class="num">03</span>Test Case Result</h2><div class="rule"></div>
<div class="kpis">
  <div class="kpi k-tot"><div class="v">{{TOTAL}}</div><div class="k">Total</div><div class="s">{{N}}개 시트 합산</div></div>
  <div class="kpi k-ok"><div class="v">{{P}}</div><div class="k">Pass</div><div class="s">N/T {{NT}}</div></div>
  <div class="kpi k-bad"><div class="v">{{F}}</div><div class="k">Fail</div><div class="s">TC 기준</div></div>
  <div class="kpi k-na"><div class="v">{{NA}}</div><div class="k">N / A</div><div class="s">사유는 아래</div></div>
  <div class="kpi k-rate"><div class="v">{{RATE}}<small>%</small></div><div class="k">Success Rate</div><div class="s">PASS ÷ (Total - N/A)</div></div>
</div>
<div class="suites">
  <div class="srow"><div class="shd"><span class="nm">{{시트 이름}}</span><span class="ct">PASS {{}} · N/A {{}} · 총 {{}}</span></div>
    <div class="sbar"><div class="sseg sp" style="width:{{PASS%}}%"></div><div class="sseg sn" style="width:{{NA%}}%"></div></div></div>
</div>
<table><thead><tr><th>Category</th><th class="n">Total</th><th class="n">PASS</th><th class="n">FAIL</th><th class="n">N/A</th><th class="n">N/T</th><th class="n">Success Rate</th></tr></thead><tbody>
  <tr><td>{{시트 이름}}</td><td class="n">{{}}</td><td class="n">{{}}</td><td class="n">{{}}</td><td class="n">{{}}</td><td class="n">{{}}</td><td class="n"><b>{{}}%</b></td></tr>
  <tr><td><b>합계</b></td><td class="n"><b>{{TOTAL}}</b></td><td class="n"><b>{{P}}</b></td><td class="n"><b>{{F}}</b></td><td class="n"><b>{{NA}}</b></td><td class="n"><b>{{NT}}</b></td><td class="n"><b>{{RATE}}%</b></td></tr>
</tbody></table>
<div class="note n-flat"><span class="lbl">N/A {{NA}}건 사유</span><ul><li>{{시트}} {{n}}건: {{사유 — 시트 비고에 없으면 「사유 보완 필요」, 지어 넣지 않는다}}</li></ul></div>

<h2><span class="num">04</span>Defect Summary</h2><div class="rule"></div>
<p>{{결함 요약 한 문장 — 검출 수, 우선순위 분포, 수정 완료 수, 나머지 분류}}</p>
<div class="axes"><div class="ax"><span class="t">P0</span><span class="r"><span class="v">{{}}<small> 건</small></span></span></div></div>
<table><thead><tr><th class="n">No.</th><th>Key</th><th>Pri.</th><th>Status</th><th>Summary</th></tr></thead><tbody>
  <tr><td class="n">1</td><td><b>{{PROJ-0000}}</b></td><td>P0</td><td><span class="chip c-ok">Fixed</span></td><td>{{요약}}</td></tr>
</tbody></table>

<h2><span class="num">05</span>Verification Details</h2><div class="rule"></div>
<table><thead><tr><th>Test Area</th><th>Key Verification Items</th><th>Result</th></tr></thead><tbody>
  <tr><td class="area">{{영역}}<span>{{세부}}</span></td>
      <td><ol><li>{{PROJ-0000}} {{검증 항목 — 테스터 언어}}</li></ol><div class="hint">{{n}}건 중 {{p}}건 PASS / {{na}}건 N/A</div></td>
      <td class="c"><span class="chip c-ok">PASS</span></td></tr>
</tbody></table>

<h2><span class="num">06</span>판정 및 잔여 항목</h2><div class="rule"></div>
<div class="decision">
  <div class="block b-check"><div class="bh"><span class="dot"></span>Sign-off 조건 (이행 필요)</div><ul><li>{{조건}}</li></ul></div>
  <div class="block b-watch"><div class="bh"><span class="dot"></span>Known Issue · 보류 결함</div><ul><li><b>{{PROJ-0000}}</b> ({{Pri}}, {{상태}}) — {{요약}}</li></ul></div>
</div>

<div class="foot">Generated {{DATE}} · QA · {{COMPANY}} · {{CUSTOMER}}</div>
</body></html>
```

* **언어:** 헤더·라벨 = 영문, 내용(의견·검증 항목) = 한국어. 판정은 전체 대문자.
* **검증 항목:** 콤마 나열 금지 → 번호 목록 + 소계 줄(`.hint`).
* **사실 기반:** 시트·Jira 에 실존하는 값만. 유추·허위 금지. 사람의 의견·판정 문장은 **원문 그대로** 넣는다.
* **판정·조건이 세 자리(히어로 · 01 조건 근거 · 06 조건)에 서면** 자리마다 역할을 하나씩 준다 — 히어로 = 판정과 조건 이름, 01 = 사람의 근거 원문, 06 = 이행할 일.
* **문장을 다른 자리로 옮기면 지시어를 다시 읽는다.** 「위 내용과」가 가리키는 대상이 바뀐다(2026-09-17 실례). 원문 보존 검사(글자 그대로 있나)는 이걸 못 잡는다.

#### 11.4.4. Hotfix · UAT 변형

* **Hotfix**: 범위가 작아 03·04 는 해당 있을 때만. 05 는 Hotfix 대상 영역 1~3개. 01 의 타일은 검증 항목 수·PASS·결함 수 정도로 줄인다.
* **UAT**: 현장 결과를 03 으로, 현장 측정(예: 실물 인식 성능)을 부속 데이터 섹션으로. 02 는 현장 설치 버전이 사내와 다를 때만.

### 11.5. PDF 변환 (headless Edge)

> 별도 PDF 라이브러리 불필요. Windows 기본 Edge 사용. 외부 호스팅 안 함 → 리포트 호스팅 정책 부합.

```powershell
param([string]$File)          # ⚠️ 인자 필수 — 아래 경고 참조

$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$html = $File
$out  = [IO.Path]::ChangeExtension($html, ".pdf")
$url  = "file:///" + ($html -replace '\\','/')
Start-Process -FilePath $edge -ArgumentList @(
  "--headless","--disable-gpu","--no-pdf-header-footer",
  "--print-to-pdf=`"$out`"","`"$url`""
) -Wait -WindowStyle Hidden
```

* `--no-pdf-header-footer` = 페이지 상하단 URL/날짜 자동 삽입 제거.
* 입력은 `file:///` 절대 경로로 준다 — 상대 경로면 DNS 조회로 가서 종료 코드 0 에 PDF 가 없다.
* ⚠️ **파일명을 반드시 인자로 준다.** 인자를 안 받거나 기본값으로 폴더를 훑는 형태로 만들면 **폴더 전체가 재렌더**된다. 실제로 남의 산출물까지 덮어쓴 사고가 있었다.
* **글리프 감사 (필수)**: 실측으로 `−`(U+2212) · `⚡`(U+26A1) · `✓`(U+2713) 는 PDF 에서 소실, `→ ÷ ↳ ※ ① ② ⟳ ✗ — ↑ ↔` 는 정상. **`✗` 는 살고 `✓` 는 죽는다** — 짐작으로 고를 수 없다. 소스 HTML + 산출 PDF 두 층위를 다 감사한다([`VERIFICATION_GUIDE.md`](./VERIFICATION_GUIDE.md) §4).
* **렌더 확인**: 쪽마다 눈으로 본다. 강제 쪽나눔이 빈 쪽을 만들고(8쪽 → 6쪽으로 줄인 실례), 병합 칸 열 위치를 짐작하면 값이 엉뚱한 칸에 찍힌다.

### 11.6. 생성기가 지킬 검사

리포트를 스크립트로 만들면 아래를 **assert 로 넣는다** — 하나라도 어긋나면 리포트를 만들지 않고 죽는다. 전부 실제로 갈라진 적이 있는 자리다.

1. **문장 속 수치 ↔ 집계 칸**: 시트에서 사람이 쓴 문장(종합 의견)의 수치가 수식 칸과 같은가. 결과 한 건이 N/A→PASS 로 바뀌자 수식 칸은 따라가고 문장은 옛 수 그대로였다.
2. **결함 문장 ↔ Jira 목록**: 문장의 결함 수·수정 완료 수가 넣기 직전 JQL 로 다시 센 목록과 같은가.
3. **버전표 ↔ 버전 페이지**: 리포트의 버전표가 그 시점 버전 페이지의 판과 같은가(판 번호를 같이 적는다). 발행 당일 버전 페이지가 한 판 올라가 있었다.
4. **의견 구조**: 종합 의견의 빈 줄 수와 첫 줄·결함 줄·판정 줄 위치 — 디자인 정리안이 이 자리 매핑에 기대므로, 시트 문구가 바뀌어 매핑이 어긋나면 죽어야 한다.
5. **집계 범위**: 시트의 결과 열을 「이름이 정확히 일치하는 열」로 찾는다. 「Result 가 들어간 첫 열」로 찾았다가 `Expected Result` 를 센 실례가 있다. 시트 탭 자체 요약 수식이 마지막 행을 빠뜨린 적도 있으니 **행 단위로 직접 센 값**과 대조한다.
6. **생성기는 저장소에 둔다.** 세션 임시 폴더에 두었다가 사라진 실례가 있다 — 산출물만 남고 위 검사 장치가 함께 없어진다.

---

## 12. QA 메일 공유 양식 (2026-07-03 도입)

> 원칙: **기록은 시스템(Drive PDF), 메일은 알림만.** 결과 상세를 메일 본문에 쓰지 않는다 — 링크로 대체. 메일 1통 = 5분 내 작성 목표.
> PDF 는 Google Drive 업로드 후 링크 공유 (§11 네이밍 룰 그대로).

### 12.1. QA Start 메일

```
제목: [QA Start] {고객사} {차수} 릴리스 QA 시작 안내

안녕하세요, QA팀 {이름}입니다.
{고객사} {차수} 릴리스 QA를 시작합니다.

- 대상: {제품/컴포넌트 및 버전 — Confluence Version 기준}
- 범위: {주요 티켓/기능 1줄}
- 기간: {시작일} ~ {종료 예정일}
- TC: {TC 시트 링크}
- (선택) 주요 Task: {하이라이트 N건 — §12.5 선별. 전수는 QA Plan 링크}
- (선택) Code Freeze: {QA 착수 시점부터 — 신규 머지 중단, 버그 수정만 허용}
- (선택) QA OK-Sign 예정: {날짜} (Sign-off = 배포 승인)

Sign-off 시 결과 리포트 링크로 재공유 드리겠습니다.
```

> 정해진 날짜에 나가는 릴리스(릴리스 트레인)라면 선택 줄 세 개를 넣는다. **Code Freeze·OK-Sign 날짜를 메일에 박는 것** 자체가 「이번 배포의 게이트는 QA」라는 신호다.

### 12.2. QA Sign-off 메일

```
제목: [QA Sign-off] {고객사} {차수} 릴리스 QA 완료 — {VERDICT}

안녕하세요, QA팀 {이름}입니다.
{고객사} {차수} 릴리스 QA를 완료했습니다.

- Verdict: {PASS / CONDITIONAL PASS / FAIL}
- 결과: TC {N}건 — PASS {n} / FAIL {n} / N/A {n} (Success Rate {x}%)
- Defect: {n}건 ({차단 여부 1줄, 예: 릴리스 차단 사유 없음})
- 특이사항: {Known Issue/UAT 계획 등 1줄, 없으면 생략}

▶ QA Report: {Drive PDF 링크}
상세 내용은 리포트를 확인해 주시기 바랍니다.
```

### 12.3. 운영 규칙

* 수치·Verdict 는 발행된 PDF 리포트와 일치시킬 것 (리포트가 원본, 메일은 요약).
* 특이사항은 최대 1줄 — 길어지면 리포트 §Known Issue 로 보내고 메일에는 "리포트 §N 참조".
* 이력 축적: 발행 시 Confluence QA Reports 인덱스(도입 시)에 한 줄 추가 — 차수/일자/Verdict/링크.

### 12.4. Hotfix 검증 완료 메일 (PDF 첨부와 한 세트)

> **원칙:** PDF 는 첨부(상세·아카이브). **판정·결정 요청은 메일 본문 텍스트로 박아 열지 않고도 읽히게.** "첨부 참고"로만 끝내면 결정건은 안 움직인다 → 결정 필요건은 **담당 지목 + 명시 요청**.

* **제목에 판정 포함** — 열기 전 보이게.
* **본문 순서:** ① 판정 → ② 검증 결과(영역별 1줄) → ③ 결정 필요(★) → ④ "상세는 첨부 참고"
* **결정 필요건:** "참고 부탁" 금지. **담당자 지목 + "결정 부탁드립니다" 직접 요청.** 없으면 ③ 생략.
* 순수 텍스트라 메일 플랫폼과 무관하게 렌더가 안 깨진다.

```
제목: [QA] {버전} Hotfix 검증 완료 — {VERDICT}

안녕하세요, QA {작성자}입니다.
{버전} Hotfix 검증 완료되어 결과 공유드립니다.

■ 판정: {VERDICT}
■ 검증 결과
  - {Area1}: {1줄 요약} ({PASS/FAIL})
  - {Area2}: {1줄 요약} ({PASS/FAIL})

■ 결정 필요 (★)         ← 없으면 블록 삭제
  {이슈 요약 1~2줄}. {결정 요청 내용} 부탁드립니다. (담당: {지목}님)

상세 내용은 첨부 리포트 참고 부탁드립니다.
```

## 12.5. 주요 Task 하이라이트 선별 (경영진/유관부서 공유용, 2026-08-04 제정)

> **2층 구조**: 전수 = QA Plan 상세 검증 대상(AI 자동) / **하이라이트 = 사람 선별(5~8건)**.
> 선별은 자동화하지 않는다 — "경영진에게 무엇이 주요인가"는 사업·고객 맥락 판단이라 **사람 고유 영역**이다.

### 12.5.1. 분업 (AI 밑작업 / 사람 선별)

| 단계 | 담당 | 산출 |
| :--- | :--- | :--- |
| 전수표 + 하이라이트 빈칸 컬럼 생성 | **AI** | 릴리스 이슈 전수에 `★` 마킹용 빈 칸 |
| 하이라이트 5~8건 마킹 | **사람(QA 리드)** | 아래 기준으로 선별 |
| 마킹된 것만 메일/보고로 재조립 | **AI** | §12.1 "주요 Task" 줄 + (선택) 경영진 보고 문서 |

### 12.5.2. 선별 기준 (사람이 이걸로 고름)

| 뽑을 기준 | 이유 |
| :--- | :--- |
| **P0 / P1** | 핵심 기능·장애급 |
| **고객 가시성 큰 것** | 고객이 바로 체감(배출·정산·화면 등) |
| **리스크 큰 변경** | 돈·보안·데이터 관련 |
| **고객·경영진 직접 요청건** | 윗선이 챙기는 것 |

→ 나머지(내부 로그 개선·리팩터·사소 개선)는 전수에만 남기고 하이라이트에서 제외.

### 12.5.3. 원칙

* **경영진은 전수를 보지 않는다.** 메일·보고엔 하이라이트만(5~8건), 전수·상세는 시스템(Plan/시트) 링크.
* Sign-off 시에도 동일 — §12.2 결과 메일은 하이라이트 기준 특이사항만, 전수 결과는 리포트 링크.
* **사람 입력 = 티켓 키만.** 순서를 중요도순으로 주면 그 순서로 정렬, 강조점이 있으면 옆에 한 마디(선택).
* **AI 처리**: 각 티켓의 제목·설명·코멘트를 읽어 ① 코드 용어·내부 약어를 빼고 **비즈니스·고객 관점으로 다시 쓰고** ② 모듈·우선순위·변경 유형을 채우고 ③ QA 포인트·리스크 초안을 쓴다.
* ⚠ **추측 번역 금지**: 티켓 설명이 부실해 의미가 불명확하면 **사람에게 되묻는다** — 추측으로 경영진에게 틀린 설명이 나가는 것이 제일 나쁘다.
* 대상 범위 = 그 스프린트·릴리스에 담긴 것만.

## 13. QA Plan 원칙 (2026-07-23 제정 — AI Native 프로세스)

> 시트 탭 레이아웃 같은 팀 고유 형식은 빼고, 어느 팀이든 쓸 수 있는 원칙만 남겼다.

**프로세스 순서**: 티켓 분석 → **QA Plan** → TC 설계 → 독립 검증 패스(TC_DESIGN_GUIDE §6.5.8) → 실행(테스트 엔지니어) → QA Result → **스프린트 회고**.

**스프린트 회고(정례)**: Result 발행 후 1회 — TC 시트 Comment 열에서 "설계가 못 본 현상"(TC 에 없던 발견)을 모아 → 원인 분류 → 규격(TC_DESIGN_GUIDE/QA_REPORT)에 반영. 편향이 쌓이는 것을 고치는 장치다.

### 13.1. 섹션 구성 (12개) 과 작성 주체

| # | 섹션 | 내용 | 작성 주체 |
| :--- | :--- | :--- | :--- |
| 1 | 수행 계획 | 개발/테스트 설계/테스트 수행/UAT 일정 + 조정 가능 단서 | **사람**(일정 확정) — AI 는 스프린트 기간에서 초안 |
| 2 | QA 목표 | 차수 핵심 목표 3~4개 + Sign-off 조건 | **AI 초안**(티켓 분석 기반) → 사람 승인 |
| 3 | QA 전략 | **제품 검증 방법론만**: Risk-based 우선순위 / 티켓↔TC 매핑 구조(1 티켓→N TC) / 회귀 범위. 협업 현황·설계 프로세스는 넣지 않는다 | AI 초안 → 사람 승인 |
| 4 | Entry Criteria | 테스트 환경 구성 + 빌드 배포 완료 | 고정 템플릿 |
| 5 | Exit Criteria | P0/P1 전체 PASS + Regression 완료 (차수별 가감) | 고정 템플릿 + 차수 조정 |
| 6 | 테스트 대상 환경 | OS/Browser/Device | 환경 사전 참조 — 사람 확정 |
| 7 | 상세 검증 대상 | 검증 분야(UI/UX·인증·보안·호환성 H/W·로그·예외) × 세부 전략(티켓 매핑) | **AI 자동 생성** — 티켓 분석의 티켓→분야 분류 |
| 8 | QA 정보 | 장비 실물 구성 | 환경 사전 참조 |
| 9 | 결함 처리 기준 | Highest(우회 불가·흐름 차단)/High(주요 요구 미충족)/Medium(우회 존재)/Low(UI·문구) | 고정 |
| 10 | 테스트 산출물 설명 | Test Suite(Task TC + Regression TC) / QA Result | 고정 템플릿 |
| 11 | 참고 링크 | QA Workspace / 스프린트 에픽 / QA Dashboard | 반자동 |
| 12 | 참고 사항 | 환경 제약 등 특기 | 사람 |

### 13.2. 작성 규칙

* 목표·전략·상세 검증 대상의 모든 티켓 언급은 **티켓 키 병기** — 다른 세션이 Plan 만 읽고 범위를 복원할 수 있어야 한다.
* 검증 분야 명칭은 고정 6종 유지 — 변경 없는 분야도 "변경 사항 없음 — Regression 범위" 로 적는다(**누락과 무변경을 구분**).
* AI 초안 → 사람 승인 후 확정 — **승인 전 Plan 기반 TC 설계 착수 금지**.
* 세부 검증 항목은 번호 목록(`1. 2. 3.`) — 줄바꿈 나열 금지 (Result §9.7 검증 항목 규칙과 동일).
* **축약어 금지** — 작성자만 아는 압축 표현 금지. 업계 통용어는 허용하되 **첫 등장에 괄호 풀이 1회**: "Cash 정합성 관련 기능(고객 수령 금액 정확성)" ✅ / "금전 정합" ❌(자작 축약).
* **섹션 정합 검토 의무** — Plan 작성/갱신 후 **작성 컨텍스트를 공유하지 않은 서브에이전트**로 1회 검토: 각 섹션 내용이 §13.1 정의에 맞는 성격인지(목표 = 결과형 "무엇을 보증", 전략 = 방법형 "어떻게"), 섹션 사이 중복이 없는지, 티켓 키가 빠지지 않았는지.

### 13.3. 산출물 원칙 (역할 인터페이스)

| 단계 | 담당 | 산출물 |
| :--- | :--- | :--- |
| 티켓 분석 | AI | 분석 문서 (git md) |
| QA Plan | AI 초안 + 사람 승인 | QA Workspace Plan 탭 (본 §13) |
| TC 설계 | AI | Task TC 시트 (TC_DESIGN_GUIDE §6.5/§8) |
| 실행 | **테스트 엔지니어(사람)** | TC 시트 Test Result + Comment (특이사항·스크린샷) |
| 결함 등록 | AI (사람 확인) | Jira Bug (TC_DESIGN_GUIDE §8.3) |
| QA Result/리포트 | AI | QA Result(§9) + PDF(§11) + 메일 초안(§12) |

* 원칙: **본문 원본 = git md/시트.** Jira·Confluence 에는 요약+링크만 (이중 기입 금지).
* **스펙 확정 게이트 = 사람(테스트 엔지니어)** — AI 분석·설계 산출물의 현장 사실(장비 결선·운영 정책)은 사람 확인을 거친다.