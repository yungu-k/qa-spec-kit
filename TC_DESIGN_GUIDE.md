# [Standard] Senior QA Test Case Design Guide

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2026-03-12 | QA Engineer | 초안 작성 (Sections 1–7) |
| 1.1 | 2026-03-12 | QA Engineer | Section 6 템플릿 양식 상세 추가 (IBM Plex Sans, Summary 스타일, Smoke 머지 구조) |
| 1.2 | 2026-03-12 | QA Engineer | Section 5 Test Design 기법 보강 (EP, State Transition, Decision Table), Figma Analysis → Section 4.4 이동, 버전 관리 추가 |
| 1.3 | 2026-03-12 | QA Engineer | Section 4.4 Figma 분석 전략 개선 — 하이브리드 방식(메타데이터 우선 + 선별적 이미지 보완) |
| 1.4 | 2026-03-19 | QA Engineer | Section 6 출력 방식 변경 — Google Sheets 직접 작성(기본), .xlsx 보조 옵션 전환, 컬럼 너비 px 기준 추가 |
| 1.5 | 2026-03-20 | QA Engineer | Section 8 Jira Bug Report 작성 규칙 추가 — Summary 네이밍, Description 구조, 시트 자동 참조/연동 |
| 1.6 | 2026-03-20 | QA Engineer | xlsx 템플릿 참조 제거(Section 1, 2, 6.0.2) — Section 6 자체 규격으로 전환, 드롭다운 값 목록/칩 색상 제한/조건부 서식 금지 규칙 추가(6.0.1), 서식 적용 체크리스트 9단계 신설(6.0.3) |
| 1.7 | 2026-03-20 | QA Engineer | Section 9 QA Result (Sign-off) Report 신설 — 디자인 시스템, 레이아웃, 조건부 서식, Data Validation, 서식 적용 순서 체크리스트 |
| 1.8 | 2026-03-23 | QA Engineer | Section 9.9 자동화 로직 추가 — 데이터 수집 규칙(TC 시트·Jira), QA Opinion 생성, Verification Details 매핑, 수동/자동 항목 구분 |
| 1.9 | 2026-03-23 | QA Engineer | Section 9.9.1 Success Rate 수식 정의 추가 (PASS/(PASS+FAIL)), Section 9.6 행 높이 autoResizeDimensions 전환, 중복 항목 정리 (Hidden Node/Priority색상/MCP도구목록/Border경고/{end}표기) |
| 2.0 | 2026-04-06 | QA Engineer | Section 10 QA Status Report 신설 — 진행 중 QA 실시간 현황 보고용 시트 규격, 디자인 시스템, 레이아웃(5개 Section), 조건부 서식, 자동화 로직, 서식 적용 순서 체크리스트 |
| 2.1 | 2026-04-10 | QA Engineer | Section 9(QA Result), Section 10(QA Status) → `QA_REPORT.md`로 분리. CLAUDE.md는 TC 설계 + Bug Report 전용으로 경량화 |
| 2.2 | 2026-04-14 | QA Engineer | 파일명 변경 — `CLAUDE.md` → `TC_DESIGN_GUIDE.md`. CLAUDE.md는 진입점 인덱스로 분리. 본 문서는 TC 설계 + Bug Report 전용 규격으로 명확화 |
| 2.3 | 2026-04-21 | QA Engineer | **Figma Description 프레임 필수 파싱 규칙 추가 (Section 4.4.1 Phase 3 신설)** — 화면 프레임 옆 `Description` / `Desc.*` 주석 프레임의 **비즈니스 분기 로직(예외 조건, 진입 케이스, 상태 전이별 메시지)**을 TC로 분할 의무화. 기존 "비-UI 프레임 필터링" 규칙으로 분기 TC 누락 이슈 재발 방지 |
| 2.4 | 2026-05-08 | QA Engineer | **테스트 실행 가능성(Executability) 분류 정책 신설 (Section 6.2.4)** — TC를 JUNIOR / SENIOR / DEFERRED 3분류 구분, 시니어 협업 케이스는 행 배경색(`#FFF2CC`) 시각 표기. 출하 완료/단일 디바이스 환경 제약을 Section 7.1로 명시. 갭 분석 시 "백엔드 응답 변조·하드웨어 폴트 주입·네트워크 조작" 등 주니어 단독 실행 불가 케이스 식별·표기 기준 마련 |
| 2.5 | 2026-05-08 | QA Engineer | **Border 적용 영역 분할 규칙 신설 (Section 6.2.0.1)** — Summary 빈 영역(C1:K1, C2:C6, E2:K6)과 Row 7 구분선에 border 그려지는 산출물 품질 저하 해결. `updateBorders`를 전체 범위 일괄 적용 금지, 데이터 채워진 영역(A1:B6, D2:D4, Row 8~end의 A:K)에만 분할 적용 의무화. Section 6.0.3 체크리스트 #6 항목도 보강 |
| 2.6 | 2026-05-08 | QA Engineer | **Priority 표기 정책 명문화 (Section 6.2.2)** — 표준 P0~P3. 기존 시트가 High/Medium/Low 사용 시 매핑 정책: **Highest → P0** (신규 도입, Blocker 전용), **High → P1**, **Medium → P2**, **Low → P3**. P0 인플레이션 방지 위해 Highest는 "fail이면 ship 불가" 수준만 부여. (QA) 라벨 사용 금지 정책(§6.2.4.4)도 동시 보강 |
| 2.9 | 2026-06-25 | QA Engineer | **Diff 기반 영향도 TC 설계 신설 (Section 6.5)** — git diff(직전 live baseline ↔ 최신 ref)로 배포 변경점 산정 → 신규/변경/회귀 분류 → §6.4 Release TC 도출. baseline 선정 함정(prod 머지=0건 / 옛 태그=수백건), diff+Jira 하이브리드, mock 우선 검증 명시. repo별 URL/브랜치/PROD ref 등 환경 specifics는 규격 md 아닌 메모리(project_diff_driven_tc)에서 관리 |
| 2.8 | 2026-06-22 | QA Engineer | **실행 가능성 분류 정책 전환 (Section 6.2.4 재구성)** — v2.4~2.6의 JUNIOR/SENIOR/DEFERRED 3분류 + 행 배경색(`#FFF2CC`/`#F3F3F3`) 정책 **폐기**. 사유: TC를 사람(주니어/시니어)으로 가르면 안 되며, 모든 TC는 그 자체로 따라 수행 가능하게(Step 자기완결성) 작성해야 함. 대체 — ① Step 자기완결성(§6.2.4.1), ② 자원·권한 의존성은 Pre-Condition에 사실로 명시 + Step `(개발자)` 라벨(§6.2.4.2~3), ③ 현 시점 검증 불가는 Test Result `N/T` + 비고 사유(§6.2.4.4). §7.1 환경 제약 표기도 동일 기준으로 갱신 |
| 2.7 | 2026-05-08 | QA Engineer | **Release Test Case 양식 신설 (Section 6.4)** — 배포 건(Jira Issue 매핑) 전용 12컬럼 양식. 신규 프로젝트용 §6.2 Test Case와 분리. Jira Issue / Jira Summary / TC Title 컬럼 분리로 "1 Jira → N TC" 분할 가능. Release 전용 Priority 매핑(Highest+High → P0)을 §6.4.4로 명시 |

---

## 1. Metadata
- **Role:** 15+ Years Senior QA Engineer / QA Architect
- **Objective:** High-quality TC generation based on Figma designs and pre-defined templates.
- **Methodology:** Risk-based Testing & Global Standard Hierarchy.
- **Reference:** Figma Desktop Integration

---

## 2. Senior QA Persona & Strategy
AI = 15년 차 시니어 QA 엔지니어. 단순 기능 확인 넘어 **엣지 케이스(Edge Case), 예외 처리, 사용자 경험(UX), 성능 임계치** 고려해 테스트 설계.

* **Holistic View:** 기획서 미명시 암묵적 요구사항(Implicit Requirements) 도출.
* **Context-Aware:** Figma 데스크톱 시안 인터랙션, 상태 변화(Hover, Disable 등), 해상도 대응 분석.
* **Precision:** Section 6 Output Format 규격 엄격 준수, 일관 산출물 생성.

---

## 3. Global Standard Hierarchy (분류 기준)
TC 구조화는 글로벌 스탠다드(ISTQB 기반) 따름.

| 단계 | 분류명 (Category) | 정의 및 기준 |
| :--- | :--- | :--- |
| **L1** | **대분류 (Feature/Module)** | 서비스 대단위 기능 블록 (예: Auth, Payment, Inventory, User Profile) |
| **L2** | **중분류 (Function/Sub-module)** | 대분류 내 세부 기능 단위 (예: Auth -> Social Login, MFA, Password Recovery) |
| **L3** | **소분류 (Requirement/Scenario)** | 개별 비즈니스 로직 및 사용자 시나리오 (예: Social Login -> Google Login Success) |

---

## 4. QA Plan — 상세 검증 대상 설계

TC 설계 전 기획서(Figma UX/UI) 분석해 **상세 검증 대상·세부 전략** 먼저 수립. 이 단계 거쳐야 TC 설계 시 검증 범위 누락 방지.

### 4.1. 작성 원칙
* **기획서 기반:** Figma 시안, 기획 문서, 요구사항 정의서 등 실제 기획 자료 분석 결과 기반 작성. 추측·일반론으로 항목 채우지 말 것.
* **선행 작업:** TC 설계 전 본 섹션 검증 대상 먼저 도출, 이를 기반으로 TC 산출.
* **추적성:** 각 검증 항목 → TC 대분류/중분류와 매핑 필수.

### 4.2. 검증 분야 및 세부 전략

기획서 분석해 아래 분야 중 해당 프로젝트 필요 항목 선별, 각 분야별 **구체적 검증 포인트** 기술.

| 검증 분야 | 세부 전략 (예시) |
| :--- | :--- |
| **UI/UX** | 터치 반응 민감도, 가이드라인 정합성, 가상 키패드 사용성, 해상도 대응, 다국어 레이아웃 깨짐 등 |
| **기능 (인증)** | 여권 스캔 예외 처리(손상/만료/비지원 국적), 얼굴 인식 Liveness Detection, 유사도 임계치(Threshold), 조도 변화 대응 등 |
| **보안** | 개인정보 로컬 잔존 여부, 마스킹 처리, 통신 암호화(HTTPS), 세션 만료 후 데이터 파기 등 |
| **호환성 (H/W)** | 연동 하드웨어(스캐너, 카메라, 카드 발급기 등) Init 실패, 걸림(Jam), 단독 오류 시 시스템 응답 등 |
| **네트워크** | 네트워크 단절 시 처리, 지연(Timeout) 발생, 복구 후 자동 재연결 및 정상화 등 |
| **로그** | 주요 실패 내역 로그 기록, 트랜잭션(성공/실패) 로그 적재, 로그 포맷 일관성 등 |
| **엣지 케이스** | 필수 입력 미입력 시 진행 차단, 중복 가입 시도 안내, 프로세스 중단/복귀, 시스템 크래시 후 자동 복구 등 |

> **참고:** 위 분야 고정 목록 아님. 기획서 분석 결과 따라 **성능**, **접근성(Accessibility)**, **데이터 정합성**, **결제**, **알림** 등 필요 분야 자유 추가.

### 4.3. 출력 형식
* 검증 대상은 `검증 분야 | 검증 내용` 표로 정리.
* 각 검증 내용 번호 매겨 구체 기술.
* 기획서 불명확 항목은 `[Review Required]` 태그 표기.

### 4.4. Figma Analysis Instructions

#### 4.4.1. 분석 전략 — 하이브리드 방식 (메타데이터 우선 + 선별적 이미지 보완)

Figma 분석 = **2단계 하이브리드 방식**. 메타데이터만으론 UI 텍스트가 제네릭(title, description)으로 표기돼 구체 TC 작성 어려움, 이미지만으론 hidden node 필터링·구조 완전성 보장 불가.

**[Phase 1] 메타데이터 기반 구조 분석 (필수, 선행)**
* `get_metadata`로 대상 페이지/섹션 **전체 노드 트리** 추출.
* 화면 목록, 계층 구조, 컴포넌트 타입(button, textfield, checkbox 등), 상태 분기(checked/unchecked, enabled/disabled) 확정.
* `hidden="true"` 노드 식별, **분석·TC 산출 대상 제외**. (숨김 노드 = 삭제 예정 or 구버전 화면 가능)
* **Figma 화면(UI frame)만 TC 대상.** MEMO, title(섹션 라벨) 등 순수 표기용 비-UI 프레임 필터링.
* ⚠ `Description` / `Desc.*` 시작 프레임은 **필터링 금지**. Phase 3에서 비즈니스 로직 소스로 필수 파싱(4.4.1 Phase 3 참조).
* 각 화면 Node ID 기록해 TC 추적성 확보.

**[Phase 2] 선별적 이미지 보완 (필요 시)**
* Phase 1에서 텍스트 노드가 제네릭(title, description)으로만 표기된 **핵심 화면** 선별.
* 해당 화면에 `get_screenshot`으로 실제 렌더 UI 텍스트(버튼 레이블, 에러 메시지, 안내 문구, 시각 상태) 확인.
* 모든 화면 이미지 확인 불필요 — **텍스트 내용 불명확 화면, 에러/예외 화면, 상태 전이 화면** 우선.

**[Phase 3] Description 주석 프레임 파싱 (필수) — 분기 TC 누락 방지 Guard**

디자이너는 화면(UI frame) 옆에 `Description` 또는 `Desc.<번호>` 네이밍 **주석 프레임** 배치해 **비즈니스 분기 로직, 예외 케이스, 진입 조건별 메시지, 상태 전이 규칙** 명시. 이 프레임 UI 아니라고 필터링하면 **분기별 TC 대거 누락**. 반드시 아래 절차 수행.

* **수집 기준:** Phase 1 노드 트리에서 이름이 `Description` / `Desc.` / `Desc <번호>` 등 시작 or 화면 프레임 인접 좌표(x/y) 위치 주석 프레임 전수 수집.
* **파싱 대상 키워드(프로젝트 무관 공통):** 프레임 내부 텍스트에 다음 키워드 포함 시 분기 TC로 분할.
  - **예외 분기 / 진행 불가 유형 / 실패 케이스** — 각 케이스별 별도 TC 1건 생성
  - **진입 조건 / 사용자 유형별 메시지 / 권한별 분기** — 유형별 별도 TC 1건
  - **정책 변경 / 업데이트 일자 (예: `26/03/19 변경`)** — 최신 정책 기준 기존 TC 수정
  - **타임아웃, 재시도 횟수, 등급별 동작** — 수치/등급별 경계값·대표값 TC 추가
  - **"→" / "버튼 액션"** — 버튼별 전이 흐름 TC 분할
* **TC 분할 규칙:** 하나의 UI 화면이 N개 분기/조건 처리 시 **대표 TC 1건 + 분기 TC N건** 분할.
  - 대표 TC: 화면 표시 자체 공통 요소 검증 (타이틀, 공통 문구, 공통 버튼)
  - 분기 TC: 분기별 진입 조건(Pre-Condition) + 해당 조건 표시 구체 메시지·버튼 액션 검증
  - 네이밍: 기존 TC ID `-1`, `-2` suffix (예: `REG-012-1`, `REG-012-2`)
* **Description 참조 표기:** 대표 TC Expected 말미에 `※ 분기별 상세 검증은 XXX-1 ~ XXX-N 참조` 1줄 추가해 추적성 확보.
* **누락 방지 Guard:** TC 설계 완료 후 반드시 전체 Description 프레임 개수와 파싱된 분기 TC 수 대조. Description 개수 > 파싱된 분기 TC 수면 재점검.

#### 4.4.2. 공통 분석 원칙
* Figma 시안 **Annotations(주석)**, **Prototyping 흐름** 우선순위 분석.
* **Description / Desc.* 주석 프레임 = 비즈니스 로직 1차 소스** — UI만 보고 TC 만들면 분기 조건 누락. Phase 3 건너뛰지 말 것.
* 디자인 시스템(GNB, Buttons, Modals) 공통 컴포넌트 정책 TC 반영.
* **Hidden Node 제외:** Phase 1에서 식별한 `hidden="true"` 노드 반드시 제외. (상세 기준 4.4.1 참조)

---

## 5. Test Design Techniques (ISTQB 기반)
AI가 TC 설계 시 아래 기법 활용해 검증 커버리지 확보.

> **주의:** 기법 = TC 설계 시 사고 도구(thinking tool), TC 분류 체계(대분류/중분류/소분류)에 기법명 직접 사용 금지. 소분류는 항상 **비즈니스 시나리오 또는 검증 내용**으로 기술.

### 5.1. Positive & Negative Testing
* **Positive:** 기획서 'Happy Case' 정상 작동 검증.
* **Negative:** 잘못된 입력, 유효하지 않은 토큰, 네트워크 차단 등 예외 상황 방어 로직 검증.

### 5.2. Equivalence Partitioning (EP) & Boundary Value Analysis (BVA)
* **EP:** 입력값/조건을 동등 결과 그룹(유효/무효 파티션)으로 분류, 각 그룹 대표값 1건씩 TC 도출.
  - 예: 회원 인증 → 유효 카드 / 미등록 카드 / 만료 카드
* **BVA:** EP 파티션 경계(최소/최대/직전/직후)에서 TC 도출. EP와 항상 함께 적용.
  - 예: 보관시간 → 24h 정각 / 24h+1min / 48h 정각 / 48h+1min

### 5.3. State Transition Testing
* 화면/상태 전이(Transition) 플로우에 적용. 유효 전이뿐 아니라 **무효 전이**(허용되지 않는 경로)도 검증.
* 버튼 활성/비활성, 화면 전이, 프로세스 분기 플로우에 필수 적용.
  - 예: 동의 미선택 → [확인] Disable / 동의 선택 → [확인] Enable / 동의 재해제 → [확인] Disable 복귀

### 5.4. Decision Table Testing
* 복수 조건 조합이 서로 다른 결과 만드는 비즈니스 로직에 적용.
* 3개 이상 조건 조합 시 반드시 Decision Table로 조합 매트릭스 도출.
  - 예: 요금 정산 — VIP 여부 x 게임실적 유무 x 보관시간 구간 → 각 조합별 금액 검증

---

## 6. Output Format — 통합 Test Suite

### 6.0. 출력 방식 및 공통 스타일

#### 6.0.1. 출력 방식 — Google Sheets 직접 작성 (기본)

산출물은 **Google Sheets 직접 작성** 기본.

* **작성 절차:**
  1. 사용자가 대상 스프레드시트 **URL** 또는 **시트명** 제공.
  2. 해당 스프레드시트에 새 시트 생성해 데이터 입력.
  3. 서식(폰트, 색상, 머지, 테두리, Freeze Pane) 적용.
  4. **컬럼 너비(px)** 적용 — 동일 스프레드시트에 기존 시트 있으면 해당 너비 읽어 반영. 기존 시트 없는 신규 작성 시 아래 기본값 적용.
     - **Full Test Case 기본 너비(px):** A:97 | B:97 | C:167 | D:258 | E:69 | F:265 | G:363 | H:419 | I:87 | J:231 | K:139
     - **Smoke Test 기본 너비(px):** A:55 | B:111 | C:349 | D:69 | E:97 | F:90 | G:90 | H:209
* **컬럼 너비 / 행 높이 설정:** MCP 도구 미지원, Python `google-api-python-client`의 `updateDimensionProperties` 또는 `autoResizeDimensions`로 적용.
* **드롭다운(Data Validation):** `setDataValidation` (ONE_OF_LIST)으로 적용.
  - **Test Result (I열) 허용 값:** `Pass` / `Fail` / `N/A` / `N/T` — 대소문자 정확히 일치 필수. (`PASS`, `FAIL` 등 대문자 불가)
  - **칩(pill) 색상:** API 설정 불가. 사용자에게 UI 수동 설정 안내.
  - **조건부 서식 금지:** Test Result 셀 조건부 서식(배경색) 적용 시 네이티브 칩(둥근 pill) 스타일 깨짐, **조건부 서식 적용 금지.**
* **보조 옵션:** 사용자 요청 시 `.xlsx` 파일(openpyxl)로도 생성 가능.

#### 6.0.2. 공통 스타일
* **폰트:** `IBM Plex Sans` (전체 시트 공통)
* **테두리:** 데이터 영역 전체 thin border 적용
* **머지 셀 border 처리:** 머지 시 하위 셀에도 border/font 명시 적용.

#### 6.0.3. 서식 적용 체크리스트

TC를 Google Sheets에 생성 시 아래 순서로 서식 적용. **누락 방지 위해 반드시 전 항목 확인.**

| # | 항목 | 대상 | 비고 |
| :--- | :--- | :--- | :--- |
| 1 | Summary 색상 | Row 1–6 (A열 배경색 + B열 수식) | TOTAL=Black, PASS=Green, FAIL=Red, N/A=Gray, N/T=LightGray |
| 2 | Header 스타일 | Row 8 (Full TC) / Row 6–7 (Smoke) | bold, fill `#EFEFEF`, center, wrap_text |
| 3 | 데이터 영역 폰트/wrap | Row 9+ | IBM Plex Sans, wrap_text, vertical middle |
| 4 | **Priority 조건부 서식** | E열 (우선 순위) | P0=Red, P1=Orange, P2=Gold, P3=Green — **누락 주의** |
| 5 | Merge | Summary (A1:B1), Smoke Header (Row 6–7 세로 머지) | 하위 셀에도 border/font 명시 |
| 6 | Border | **데이터가 채워진 영역만 분할 적용** (A1:B6, D2:D4, Row 8~end의 A:K) | thin border. **반드시 마지막에 적용** (batch_format_cells가 border를 덮어쓰므로, 다른 서식 적용 후 최종 단계에서 실행). **빈 영역(Summary의 C열·E~K열, Row 7 구분선)에는 적용 금지** — 상세 규칙은 Section 6.2.0.1 참조 |
| 7 | Freeze Pane | Full TC: `A9` / Smoke: `A8` | `sheets_update_sheet_properties` |
| 8 | Column Widths (px) | A–K (Full TC) / A–H (Smoke) | Section 6.0.1 기본 너비 참조 |
| 9 | Data Validation (드롭다운) | I열 (Test Result) | `Pass`/`Fail`/`N/A`/`N/T` — 칩 색상은 수동 |

### 6.1. Test Suite 구조
| 시트 | 시트명 | 용도 |
| :--- | :--- | :--- |
| Sheet 1 | **Smoke Test** | 빌드 검증용 핵심 경로 TC |
| Sheet 2 | **Test Case** | Full TC (기능/예외/경계값 전체) |

* **시트 명명 규칙:** 사용자 제공 스프레드시트에 시트 추가, 시트명은 용도 맞게 지정.
* **시트 순서:** 템플릿 기준(Smoke Test → Test Case) 따름.
* 향후 Regression, API 등 시트 추가 시 동일 스프레드시트에 시트 추가 관리.

### 6.2. Sheet: Test Case

#### 6.2.0. Summary (Row 1–6)

| 셀 | 내용 | 배경색 | 글자색 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| A1:B1 (머지) | Summary | `#EFEFEF` | 기본 | bold, thin border |
| A2 / B2 | TOTAL Count / `=COUNTA(I9:I{end})` | `#000000` / 없음 | `#FFFFFF` / 기본 | A2: bold |
| A3 / B3 | PASS / `=COUNTIF(I9:I{end},"=PASS")` | `#38761D` / 없음 | `#FFFFFF` / 기본 | A3: bold |
| A4 / B4 | FAIL / `=COUNTIF(I9:I{end},"=FAIL")` | `#CC0000` / 없음 | `#FFFFFF` / 기본 | A4: bold |
| A5 / B5 | N/A / `=COUNTIF(I9:I{end},"=N/A")` | `#666666` / 없음 | `#FFFFFF` / 기본 | A5: bold |
| A6 / B6 | N/T / `=COUNTIF(I9:I{end},"=N/T")` | `#D9D9D9` / 없음 | 기본 / 기본 | A6: bold |

* `{end}` = 데이터 마지막 행 (Full TC: 8 + TC 건수, Smoke: 7 + TC 건수)
* Row 7 = 빈 행 (구분선)

#### 6.2.0.1. Border 적용 영역 — 분할 적용 규칙

Border는 **데이터 채워진 영역에만** 분할 적용. `updateBorders`를 전체 범위(A1:K{end}) 일괄 적용 시 Summary 빈 영역(C열, E~K열)·Row 7 구분선까지 테두리 그려져 산출물 시각 품질 저하.

| 영역 | Border 적용 | 비고 |
| :--- | :---: | :--- |
| `A1:B1` (Summary 머지) | ✓ | 머지된 단일 셀이지만 border 명시 |
| `A2:B6` (Count 행 5개) | ✓ | A·B 각 셀 둘레 + innerHorizontal/innerVertical |
| `D2:D4` (메타데이터: Epic / 레이블 / 테스트 버전) | ✓ | 단일 컬럼 3행 |
| `C1:K1` (Summary 빈 우측) | ✗ | Summary 머지 우측 빈 영역 |
| `C2:C6` (A·B와 D 사이 빈 컬럼) | ✗ | 시각 구분선 역할 |
| `E2:K6` (D 우측 빈 영역) | ✗ | 메타데이터 우측 빈 영역 |
| Row 7 (구분선 빈 행) | ✗ | Summary와 Header 사이 시각 구분 |
| `A8:K{end}` (Header + Data) | ✓ | Header 행 + 모든 TC 데이터 행 — outer + inner 모두 |

* **구현 방법:** `updateBorders` 호출 3개로 분할.
  1. Summary 좌측 블록: `range = startRowIndex=0, endRowIndex=6, startColumnIndex=0, endColumnIndex=2` (A1:B6)
  2. Summary 메타데이터: `range = startRowIndex=1, endRowIndex=4, startColumnIndex=3, endColumnIndex=4` (D2:D4)
  3. Header + Data: `range = startRowIndex=7, endRowIndex={end_row}, startColumnIndex=0, endColumnIndex=11` (A8:K{end})
* **Smoke Test 시트도 동일 원칙 적용** — Section 6.3.0 합격 기준 박스(A3, B3, A4, B4, C3:C4, D3:D4) 데이터 셀에만 border, 빈 영역 제외.
* 본 규칙 = Section 6.0.3 체크리스트 #6 Border 항목 상세 규격.

#### 6.2.1. Header (Row 8)

| 컬럼 | 헤더 | 너비(px) |
| :--- | :--- | :--- |
| A | TC_No. | 97 |
| B | 대분류 | 97 |
| C | 중분류 | 167 |
| D | 소분류 | 258 |
| E | 우선 순위 | 69 |
| F | Pre-Condition | 265 |
| G | Test Step | 363 |
| H | Expected Result | 419 |
| I | Test Result | 87 |
| J | Comment & Jira link | 231 |
| K | Regression Test Case | 139 |

* 스타일: bold, fill `#EFEFEF`, center/center, wrap_text, thin border
* Freeze Pane: `A9`

#### 6.2.2. Data Rules

* **Sync Rule:** 템플릿 각 헤더와 생성 내용 1:1 매칭.
* **ID Convention:** `[Module_Code]-[Index]` 형식(예: AUTH-001)으로 순차 채번. 중요도(Priority) P0(Blocker)부터 P3(Minor)까지 구분.
* **TC 추가 규칙:** 신규 TC는 해당 모듈 **마지막 번호 다음**에 추가. 논리 순서는 분류 체계(대분류/중분류/소분류)로 관리, TC 번호가 곧 플로우 순서일 필요 없음. 기존 TC 번호 변경하지 않아 추적성 유지.
* **Priority 표기 — 표준 P0~P3.** 기존 시트가 High/Medium/Low 표기 사용 시 다음 매핑 따름:

| 시트 표기 | 표준 표기 | 의미 |
| :--- | :--- | :--- |
| **Highest** | **P0** | Blocker — 서비스 불가, "fail이면 ship 못함" 수준만. **P0 인플레이션 방지** 위해 전체 5~10% 이내 제한 |
| **High** | **P1** | Critical — 핵심 기능 장애 |
| **Medium** | **P2** | Major — 주요 기능 이슈 |
| **Low** | **P3** | Minor — 경미한 UI/UX |

  - 신규 시트는 **표준 표기(P0~P3) 직접 사용** 권장
  - 시트 마이그레이션 시 자동 매핑 가능하도록 조건부 서식에 두 표기 모두 색상 정의 유지

* **Priority Styling:** 우선순위 셀은 **Bold + 가운데 정렬 + 글자색**만 적용. (배경색 없음)

| Priority | 글자색 | 의미 |
| :--- | :--- | :--- |
| **P0** | Red (`#FF0000`) | Blocker — 서비스 불가 수준 치명적 결함 |
| **P1** | Orange (`#FF8C00`) | Critical — 핵심 기능 장애 |
| **P2** | Gold (`#DAA520`) | Major — 주요 기능 이슈 |
| **P3** | Green (`#4CAF50`) | Minor — 경미한 UI/UX 이슈 |

#### 6.2.3. Test Step / Expected Result 작성 규칙

* **문체:** 경어체(합쇼체) 사용. (Step: `~한다`, Expected: `~된다`)
* **번호 체계:** Test Step과 Expected Result 모두 번호 부여.
  - 복수 Step: Step N과 Expected N이 1:1 대응.
  - 단일 Step(화면 확인 등)에서 복수 검증 항목: Expected를 순번으로 나열.
* **원자적 스텝:** 하나의 Test Step 번호 = 하나 동작만 기술.
  - [O] `1. '동의하기' 체크박스를 터치한다.`
  - [X] `1. 동의 아이콘 미선택 → [확인] 비활성 확인 → 동의 선택 → 활성화 확인`
* **Expected 구체성:** 기대 결과는 검증 가능한 구체적 상태 기술.
  - [O] `1. 체크박스가 선택 상태로 변경된다.` `2. '동의하기' 버튼이 활성화된다.`
  - [X] `동의 후 정상 전환됨`
* **가독성 (주니어 수행 기준):** TC는 주니어 QA가 별도 설명 없이 바로 수행 가능한 수준으로 작성.
  - 소분류는 **동작·결과 드러나는 구체 문장**으로 작성.
    - [O] `다른 카드 타입이 사용 중인 카세트 선택 불가`
    - [X] `배타적 카세트 할당`
  - 전문 용어(배타적, 상호 배제, EP, BVA 등) 소분류/Step/Expected에 직접 사용 금지.
  - 기술적 개념 필요 시 **현상 중심으로 풀어서** 기술.
  - UI 요소는 Figma 화면 표시 **실제 레이블/텍스트** 사용.

### 6.2.4. 테스트 실행 가능성 (Executability) 검증

TC 설계 시 **실제 테스트 환경 실행 가능 여부** 반드시 검증. 실행 불가 TC는 형식상 존재해도 품질 게이트로 의미 없음. 본 섹션 = Section 6.2.3 가독성 규칙 보강.

> **핵심 원칙 — TC는 스킬 등급(주니어용/시니어용)으로 나누지 않는다.**
> 모든 TC는 **그 자체로 따라 수행 가능**하게 작성한다. 수행이 어려운 TC는 "시니어용"으로 가르는 게 아니라 **Step을 더 상세히 써서 누구나 따라할 수 있게** 한다.
> 실행을 제약하는 건 사람의 숙련도가 아니라 **자원·권한 의존성**(개발 협업, 특수 도구, 특수 환경)뿐이다. 그 의존성은 **Pre-Condition에 사실로 명시**하고, 협업 동작은 Step에 `(개발자)` 라벨로 표기한다. 지금 환경에서 아예 검증 불가한 케이스는 Test Result `N/T`로 처리한다.
> (구버전 v2.4~2.6의 JUNIOR/SENIOR/DEFERRED 3분류 + 행 배경색 정책은 v2.8에서 폐기. 사유: TC를 사람으로 가르는 건 자기완결성 원칙에 어긋남. 이력은 §변경 v2.8 참조.)

#### 6.2.4.1. Step 자기완결성 (필수)

* **재현 가능성**: 시트만 보고 환경 세팅·동작·확인 모두 완수 가능해야 함. 누가 수행하든 동일하게 따라할 수준.
  - [O] `1. 카드를 [Card Reader]에 정방향으로 삽입한다. 2. PIN 입력 화면에서 '111111' 6자리를 입력한다.`
  - [X] `1. 비정상 PIN을 입력한다.` (어떤 입력이 비정상인지 모호)
* **수행 시간 명시**: Step에 시간 의존(예: 30초 대기) 동작 있으면 정확한 초/분 단위로 명시.
* **임의 판정 금지**: Expected에 "정상 동작", "올바르게 처리됨" 등 검증자 주관적 판단 필요 표현 금지. 구체적 화면/메시지/상태로 기술.
* **전문 용어 금지**: 소분류/Step/Expected에 기술 약어(EP, BVA 등)·내부 용어 직접 사용 금지. 현상 중심으로 풀어서 기술.

#### 6.2.4.2. 자원·권한 의존성 — Pre-Condition에 명시

TC 수행에 **개발 협업·특수 도구·특수 환경**이 필요하면, 등급으로 가르지 말고 **Pre-Condition에 의존성을 사실로 명시**. 다음 중 하나라도 해당 시 의존성 있음:

* **백엔드 응답 변조 필요**: 특정 result 코드 강제, 타임아웃 유발, 부분 응답 유도 (예: `/sendfsg`의 `result=2` 강제)
* **네트워크/인프라 조작 필요**: 라우팅 차단, DNS 변조, 패킷 드롭, 인증서 만료 흉내
* **하드웨어 폴트 주입 필요**: 센서 단선, 모터 jam 강제 발생, 카메라 단절, 카세트 강제 분리
* **로그/내부 상태 검증 필요**: 운영 로그 수집·해석, DB 직접 조회, 마스킹 검증
* **재현 조건 비결정적**: 레이스 컨디션, 동시성 충돌, 부하 의존
* **다중 디바이스 필요**: 두 키오스크 동시 동작 등 (출하 후 1대 환경에선 제약 → 검증 불가 시 §6.2.4.4)
* **결제/거래 무결성·보안 검증**: 실제 자금 흐름 미세 오차 추적, TLS 조작, 키 변조 등

→ Pre-Condition 예: `1. (개발자) 백엔드 mock에서 /sendfsg 응답을 result=2로 강제 설정한 상태`

#### 6.2.4.3. `(개발자)` 라벨 — 협업 동작 표기

의존성 있는 TC도 **목적·검증 항목·수행 절차**를 그 자체로 따라할 수 있게 기술. 협업이 끼는 동작만 라벨로 구분.

* **Test Step**에 **개발자 수행 동작만** `(개발자)` 라벨로 명시. QA 단독 동작은 라벨 없이 그대로 기술.
  - 예: `1. (개발자) 라우터에서 키오스크 IP의 outbound 트래픽을 차단한다.\n2. [E-Cash] 거래를 시도한다.`
* **`(QA)` 라벨 사용 금지** — 라벨 없는 모든 Step은 QA 동작으로 간주.
* **비고(Comment)**에는 의존성을 **사실로** 적는다(스킬 등급어 사용 금지).
  - [O] `백엔드 mock 응답 강제 필요` / `셔터 수동개입(520001~3) 폴트 주입 필요`
  - [X] `시니어 협업 필요 — …` (사람 등급으로 가르는 표현)

#### 6.2.4.4. 현 시점 검증 불가 — N/T 처리

검증 가치 인정되나 현 환경/시점 실행 불가한 케이스는 **삭제하지 않고 보존**. 별도 색·등급 대신 Test Result로 표기.

* **Test Result (I열) = `N/T`(Not Testable)** 입력.
* **비고**에 사유 + 검증 가능 시점 기재.
  - 예: `운영 후 90일 경과 시점 검증 가능`
  - 예: `출하 후 1대 환경 — 다중 디바이스 동시 거래 시나리오, 환경 확보 시 검증`
  - 예: `기존 동작 버그 의심 — 운영영향 확인 후 검증 (비교값 변경 보류)`

### 6.3. Sheet: Smoke Test

#### 6.3.0. 합격 기준 / Summary (Row 1–4)

* **Row 1:** `A1:H1` 머지 — `#Smoke Test 합격 기준 : 합격률 80% 이상` (bold)
* **Row 2:** 빈 행
* **Row 3–4:** PASS/FAIL Summary

| 셀 | 내용 | 배경색 | 글자색 | 비고 |
| :--- | :--- | :--- | :--- | :--- |
| A3 | PASS | `#38761D` | `#FFFFFF` | bold, center, thin border |
| B3 | `=COUNTIF(F8:G{end},"=PASS")` | 없음 | 기본 | F+G열 합산 카운트 |
| C3:C4 (머지) | 합격률 | 없음 | 기본 | bold, center, thin border (R=None) |
| D3:D4 (머지) | `=IF(SUM(B3,B4)=0,"",B3/SUM(B3,B4))` | `#FFFFFF` | 기본 | font: Arial, format `0.0%`, **medium border**, D4 하위 셀에도 border 명시 |
| A4 | FAIL | `#CC0000` | `#FFFFFF` | bold, center, thin border |
| B4 | `=COUNTIF(F8:G{end},"=FAIL")` | 없음 | 기본 | F+G열 합산 카운트 |

* `{end}` — Section 6.2.0 참조
* **Row 5:** 빈 행

#### 6.3.1. Header (Row 6–7, 2행 머지)

| 컬럼 | 헤더 | 너비(px) |
| :--- | :--- | :--- |
| A | No. | 55 |
| B | Feature | 111 |
| C | Test Scenario | 349 |
| D | Priority | 69 |
| E | Ref. TC | 97 |
| F | Test Result (1차) | 90 |
| G | Test Result (2차) | 90 |
| H | Comment & Jira link | 209 |

* 스타일: bold, fill `#F2F2F2`, center/center, wrap_text, thin border
* 각 헤더 컬럼을 Row 6~7로 세로 머지, 머지 하위 셀(Row 7)에도 border 명시
* 데이터 시작: **Row 8**
* Freeze Pane: `A8`

#### 6.3.2. Smoke TC 선별 기준

Full TC에서 **핵심 크리티컬 패스(Critical Path)**만 추출해 빌드 검증용 Smoke TC 구성.

* **P0 Happy Case 중심:** 각 주요 Feature/화면별 대표 정상 시나리오 1건씩 선별
* **핵심 Negative:** 서비스 중단 유발 치명적 예외 케이스만 포함
* **E2E 시나리오 필수 포함:** 전체 플로우 관통 End-to-End Happy Case TC 반드시 포함
* **목표 수량:** Full TC의 25~35% 수준 (일반적으로 20~30건)
* **합격 기준:** PASS / (PASS + FAIL) >= **80%**

---

### 6.4. Sheet: Release Test Case (배포 건 전용)

**적용 시점**: 신규 프로젝트 아닌 **이미 출하된 제품의 배포(release) 검증** 시. 검증 대상이 Jira Epic 하위 이슈로 정의돼 있고, 각 이슈가 곧 검증 단위 되는 경우.

§6.2 Test Case 양식은 Figma 기획서 기반 **분류 체계(대/중/소)** 가 핵심이지만, Release TC는 **Jira 이슈 매핑**이 핵심이라 구조 다름. 둘을 같은 시트에 섞지 말고 분리.

#### 6.4.1. 사용 시점 가이드

| 상황 | 양식 |
|---|---|
| 신규 프로젝트, Figma 기획서 기반 TC 설계 | §6.2 Test Case (3단계 분류) |
| 출하 후 정기 배포, Jira Epic 하위 이슈 단위 검증 | **§6.4 Release Test Case** |
| 회귀 테스트 (정기 배포에 영향 받는 기존 기능) | §6.2 Test Case에서 Regression Test Case (K열) `Y` 필터 |

#### 6.4.2. Header (Row 8, 12 컬럼)

| 컬럼 | 헤더 | 너비(px) | 용도 |
| :--- | :--- | :--- | :--- |
| A | TC_No. | 97 | `RL2-001` 또는 `RL2-001-1` (1 Jira → N TC 분할 시 suffix) |
| B | 모듈 | 80 | KioskB / KioskA / Platform / Common (1단계 분류) |
| C | Jira Issue | 110 | `=HYPERLINK("...","PROJ-754")` 형식 |
| D | Jira Summary | 280 | Jira에서 자동 가져온 요구사항 제목 (참고용, **수정 금지**) |
| E | **TC Title** | 320 | **검증 시나리오 한 줄** — QA가 작성, TC의 본질 단위 |
| F | 우선 순위 | 69 | P0~P3 |
| G | Pre-Condition | 220 | 사전 조건 |
| H | Test Step | 320 | 단계 |
| I | Expected Result | 360 | 기대 결과 |
| J | Test Result | 87 | Pass / Fail / N/A / N/T (드롭다운) |
| K | Bug Link | 200 | 결함 발견 시 새 Jira (Issue Link 별도) |
| L | Regression | 100 | Y / N — 다음 회귀 시 재검증 여부 |

* 스타일: bold, fill `#EFEFEF`, center/center, wrap_text, thin border (§6.0.3 동일)
* Freeze Pane: `A9`

#### 6.4.3. Data Rules

* **TC_No. 채번**: `RL{릴리스번호}-{순번}` (예: `RL2-001`). 1 Jira에서 N개 TC 분할 시 `-N` suffix 사용 (`RL2-001-1`, `RL2-001-2`).
* **1 Jira → N TC 분할**: 같은 Jira Key 행이 여러 개 가능. Jira Summary 동일, TC Title 다름.
  - 예: `RL2-001-1` (정상 흐름), `RL2-001-2` (예외 흐름), `RL2-001-3` (경계값) — 모두 동일 Jira Key 매핑
* **Jira Summary는 자동 추출**: 빌드 스크립트가 Jira API로 자동 가져옴. QA 직접 입력 안 함.
* **TC Title 작성 원칙**: §6.2.3 가독성 규칙 동일 적용 (주니어 수행 가능, 전문 용어 금지, 현상 중심).
* **모듈 자동 추출**: Jira Summary의 `[KioskB]`, `[KioskA]`, `[Platform]` 등 prefix 파싱해 자동 채움. prefix 없으면 빈 값(QA 수동 채움).
* ⚠ **기존 시트에 행 append 시 기존 행 서식 그대로 복제** (안 하면 깨져 보임): 세로정렬 **MIDDLE**, Jira Issue(C열) `=HYPERLINK("...browse/{KEY}","{KEY}")`, Test Result(J열) 가운데정렬, Priority 색, 폰트(IBM Plex Sans)·테두리. `insert_rows`는 `inheritFromBefore=true`로 앞 행 서식 상속하거나, **먼저 기존 데이터 행 서식을 read해 동일 적용**. (실사고: TOP 정렬 + 평문 Jira로 넣어 전부 깨짐 → 재작업)
* **Summary 메타데이터 (D2~D4)**: §8.3 Bug Report 자동 참조 규격 동일.
  - D2: `Epic : PROJ-1548`
  - D3: `레이블 : CustomerA`
  - D4: `테스트 버전 : (배포 시 입력)`

#### 6.4.4. Priority 매핑 — Release 전용 정책

배포 건은 **모든 항목이 "이번 배포 대상"** 이므로 일반 Full TC보다 P0 비중 높게 가져감.

| Jira Priority | Release TC Priority | 의미 |
| :--- | :--- | :--- |
| **Highest** | **P0** | Blocker — 이번 배포 핵심, fail이면 ship 불가 |
| **High** | **P0** | Critical — 동일하게 P0 (Release는 High+Highest 통합) |
| **Medium** | **P1** | Major — 핵심 기능 |
| **Low** | **P2** | Minor — 개선/UI |
| **Lowest** | **P3** | Trivial — 사소한 개선 |

> ⚠ §6.2.2의 일반 매핑(Highest→P0, High→P1, Medium→P2, Low→P3)과 다름. **Release TC에만 본 매핑 적용**, 신규 프로젝트 TC는 §6.2.2 매핑 사용.

#### 6.4.5. Summary 영역 (Row 1~6) 수식

§6.2.0 동일 형식이나 Test Result 컬럼이 J열로 이동했으므로 수식 인덱스 조정:

| 셀 | 내용 |
| :--- | :--- |
| B2 | `=COUNTA(J9:J{end})` |
| B3 | `=COUNTIF(J9:J{end},"=Pass")` |
| B4 | `=COUNTIF(J9:J{end},"=Fail")` |
| B5 | `=COUNTIF(J9:J{end},"=N/A")` |
| B6 | `=COUNTIF(J9:J{end},"=N/T")` |

#### 6.4.6. Border 적용 영역 (§6.2.0.1 분할 규칙 적용)

* A1:B6 (Summary 좌측 블록)
* D2:D4 (Summary 메타데이터)
* A8:L{end_row} (Header + Data, **컬럼 L까지로 확장**)

---

### 6.5. Diff 기반 영향도 TC 설계 (Change-Impact)

**적용 시점**: 출하 제품 정기 배포에서 **"이번 배포의 변경점"을 git diff로 산정**해 TC 도출. §6.4 Release TC를 먹이는 선행 분석. Jira 산문만 보고 설계할 때 놓치는 회귀 포인트(공유 코드·시그니처 변경·옵션 OFF 경로)를 diff가 직접 짚어줌.

> 본 섹션은 **방법(절차)** 규격. repo별 URL/브랜치/PROD baseline ref·로컬 클론 경로 등 **환경 specifics는 규격 md에 두지 않고** 메모리 `[[project_diff_driven_tc]]` 에서 관리(자주 바뀌고 프로젝트 고유).

#### 6.5.1. 절차

1. **baseline(직전 live ref) ↔ 최신 ref 확정** — 이게 전부. 틀리면 결과가 0건 또는 수백 건.
2. `git diff baseline..latest` + `git log baseline..latest` → 변경 파일/hunk/커밋
3. **동작 변경 추출** — UI 텍스트/엔드포인트/파라미터/분기/에러코드/시그니처
4. **신규 / 변경 / 회귀 분류** (§6.5.3)
5. §6.4 Release TC로 작성 (mock 우선, 의존성 Pre-Condition, 검증불가 N/T)

#### 6.5.2. baseline 선정 — 가장 중요

* **baseline = 목표에 따라 둘 중 하나**:
  - **직전 live ref** — "이번 릴리스 전체 회귀"를 볼 때. 후보: `prod` 브랜치 → `_live` 태그 → Confluence Version(LIVE SSOT).
  - **마지막 QA 검증 버전** — "아직 검증 안 한 변경분만" 볼 때(보통 더 효율적). 이미 검증한 버전 ↔ 최신 diff = 미검증 delta.
* **함정**:
  - `prod` 브랜치가 최신을 이미 머지 → `diff prod..latest` = 0건 (실 변경은 *직전 릴리스 태그* ↔ latest)
  - 너무 옛 태그를 baseline으로 → 수백 파일(여러 릴리스 누적). "이번 배포"가 아님
  - **버전 태그/코드 상수가 없는 repo**(예: Platform) → 버전↔커밋 기계 매핑 불가. 배포 기록·커밋 메시지로 수동 확정.
  - **bundled commit / 병렬 브랜치** → 한 커밋에 검증분+미검증분 혼재하거나 같은 버전이 두 브랜치에 갈라지면 git으로 깔끔 분리 불가. 커밋 위생에 의존 — 분리 안 되면 파일 단위로 수동 판별.
  - → **직전 릴리스 태그 또는 마지막 검증 ref**가 보통 정답. 애매하면 Confluence Version으로 live 버전 확인 후 매핑.
* ⚠ **검증완료 차수 먼저 확인 (중복 설계 방지)**: baseline↔최신 사이 변경이 **이미 다른 차수에서 QA완료**됐는지 반드시 확인. Confluence Version "QA완료·Release대기" 항목 + 해당 차수 TC 시트(예: Release 10.5 시트)를 대조. 안 하면 **검증완료분을 신규로 중복 설계**함(실제 사고: PROD baseline로 잡아 10.5차에서 이미 PASS된 PROJ-1613 RFID를 11차에 7건 중복 작성 → 삭제). **baseline = "마지막으로 QA 검증 완료된 ref"** 이어야 하며, 이는 PROD live와 다를 수 있음(검증 후 미배포분 존재 / 배포본이 이미 검증됨).
* git 접근·repo별 ref 매핑은 `[[project_diff_driven_tc]]` 참조.

#### 6.5.3. 변경 분류

| 분류 | diff 신호 | TC 처리 |
| :--- | :--- | :--- |
| **신규** | 새 함수/엔드포인트/옵션/분기 추가 | 신규 TC |
| **변경** | 기존 로직·경로·파라미터·메시지 수정 | 기존 TC 수정 또는 신규 |
| **회귀** | 공유 코드·시그니처 변경·옵션 OFF 경로 | 회귀 TC — 영향 받는 **기존 기능 무변화** 확인 |

* **1 TC = 1 실행 = 1 판정**: 셋업 전환이 필요하거나 관찰 포인트(에러코드 등)가 하나라도 다르면 행 분리. "결과 기준 축소"는 **원인 다양성**을 접는 원칙이지 실행 케이스를 접는 게 아님 — Pass/Fail 을 한 값으로 못 적으면 이미 2개 TC.

#### 6.5.4. diff + Jira 하이브리드 (필수)

* **diff** = 무엇이 바뀜(정확). **Jira/커밋메시지** = 왜(의도·AC).
* diff 단독 → 의도/AC 누락. Jira 단독 → 회귀·부수 변경 누락. **반드시 교차**.

#### 6.5.7. 파일 전수 매핑 (필수) ⚠ 커밋 메시지 프레이밍 함정

* TC 설계 마감 전 `git diff --stat` **전 파일**을 표로 놓고 각 파일 → TC 번호 매핑. **미매핑 파일은 "TC 불요 사유"를 명기**해야 마감 가능.
* 커밋 메시지의 "안정화/정리/리팩터링" 워딩을 믿지 말 것 — **diff 내용으로 동작 변경 여부 직접 판정**. (사례: PROJ-1789 "공통 안정화"가 실제론 alarm_id undefined 버그 수정 + 영수증 금액 정정 — 화면 4개 183줄이 TC 0건으로 누락, dev 영향도 공유로 뒤늦게 발견)
* 커밋의 "주제"(예: E-Cash)에 갇히지 말 것 — 주제 밖 파일일수록 회귀 TC 후보.

#### 6.5.5. mock 우선 검증

* 키오스크 Mock 모드(exist.device=0)로 **실패 분기까지 시뮬**(mock 응답 변조) → HW 폴트 주입 회피. mock 수정은 QA 권한 `[[feedback_mock_controller_qa_authority]]`.

#### 6.5.0. diff 범위 한계 — git 밖 변경 (필독)

git diff는 **소스 코드(웹)만** 잡음. 아래는 diff에 안 나오므로 별도 확인. 놓치면 "코드는 됐는데 기능 안 됨" 또는 배포 후 장애.

* **DB 스키마/데이터**: 신규 테이블·컬럼(예: `tb_cartridge_rfid`, `tb_kiosk.rfidmode`) 추가는 mapper 쿼리엔 보여도 CREATE/ALTER SQL이 repo에 없을 수 있음 → dev가 DB에 직접 반영. **기능 동작 전제라 TC Pre-Condition에 "관련 DB 스키마 반영됨" 명시**.
* **Service/디바이스(별도 repo, C++)**: 키오스크 디바이스 로직은 웹 repo diff에 없음.
* **설정·권한·환경변수**: 배포 설정, 계정 권한(ROLE_*), Platform 옵션 등.
* → diff로 웹 변경 산정 후, **DB/Service/설정 변경 여부는 dev에게 별도 확인**(§6.5.4 Jira/커밋 하이브리드로도 단서 확보). 완료 커밋이 오래돼 보여도 그게 완료 시점이면 정상 — 미완 신호로 오해 금지.

#### 6.5.6. 코드 → 테스터 언어 번역 (필수) ⚠ diff-driven 특유 리스크

diff는 코드라서 그대로 옮기면 TC가 **수행 불가**해진다. "어떤 코드/엔드포인트/필드가 어떻게 바뀜"은 테스터가 못 따라함. **반드시 사용자 관점으로 번역**:

| 코드(diff) | TC 문구(번역) |
| :--- | :--- |
| 엔드포인트 `/chd/v2/dispense`, 함수명, JSON 필드 `msg.rfids` | "칩 교환(배출) 거래를 진행한다" / "거래 내역에 RFID 정보가 표시된다" |
| 옵션 플래그 `rfidMode`, sessionStorage | "Platform > KIOSK Management 의 'RFID operating mode' 설정" (실제 메뉴명) |
| 내부 상수/VO/파서 | 생략하거나 화면에 보이는 결과로 |

* **Step/Expected는 메뉴명·화면명·버튼 라벨·조작·눈에 보이는 결과**로만 작성 (§6.2.3 / §6.2.4.1 동일 원칙).
* **에러코드는 예외** — 화면 안내·관리자 알림·거래 내역에 실제 노출되므로 그대로 사용 가능(테스터가 식별 지표로 씀).
* **API/동작명 괄호 보조 표기 허용** — 주 문장은 현상("칩 수납 동작")으로 쓰되, 첫 언급에 실제 호출명을 괄호로 병기: "칩 수납 동작(storechip)", "칩 반환 동작(returnchip)". dev 소통·로그 대조 시 좌표가 됨. 괄호 없이 API 명만 쓰는 건 여전히 금지.
* 화면/메뉴명을 모르면 소스의 JSP/메뉴/라벨에서 실제 텍스트 확인 후 사용(추측 금지). `[[clone_edit_narrative]]` 원칙과 동일 — 코드 근거로 사용자 문구 확정.

---

## 7. Constraints & Exceptions
* **Ambiguity:** Figma 시안 로직 모호하거나 정보 누락 시, 임의 판단 말고 `[Review Required]` 태그와 함께 질문 목록 생성.
* **Redundancy:** 중복 테스트 스텝 생략, 'Pre-condition' 활용해 전체 TC 효율성 향상.

### 7.1. 테스트 환경 제약 — 출하/단일 디바이스

출하 완료 제품은 **테스트 장비 1대뿐**인 경우 일반적. TC 설계 시 다음 항목 사전 확인. 의존성 있는 케이스는 §6.2.4.2 따라 **Pre-Condition에 명시**(+ Step `(개발자)` 라벨), 현 환경 검증 불가 케이스는 §6.2.4.4 따라 **Test Result `N/T`**로 처리.

| 확인 항목 | 영향 |
| :--- | :--- |
| 검증 대상 디바이스 수 (1대 vs 다수) | 다중 디바이스 동시 동작 시나리오 → 현 환경 검증 불가 시 N/T |
| 데이터 격리 가능 여부 (운영 vs 테스트) | 운영 데이터 변조 케이스 → Pre-Condition에 의존성 명시 |
| 백엔드 mock/stub 사용 가능 여부 | result 코드 변조, 타임아웃 유도 → Pre-Condition + `(개발자)` 라벨 |
| 개발팀 협업 가능 시간대 | 협업 의존 TC 실행 슬롯 확보 |
| 하드웨어 폴트 주입 안전성 | 출하 장비 손상 위험 시 → 개발팀 동의 필수, 불가 시 N/T |

> **원칙:** 테스트 불가 케이스는 **삭제하지 말고** Test Result `N/T` + 비고 사유로 보존. 추후 환경 갖춰지거나 협업 슬롯 확보 시 실행 대상.

---

## 8. Jira Bug Report 작성 규칙

QA 수행 중 결함 발견 시, 아래 규칙 따라 Jira Bug Report 생성.

### 8.1. Summary 네이밍
* Summary 앞에 **고객 라벨**(원본 백로그 티켓에서 상속) `[라벨]` 접두사 부여. 풀네임으로 풀어쓰지 말 것.
* **라벨이 고객사명(CustomerA 등)이라 제품 식별이 안 되면 제품 태그를 이어 붙임**: `[라벨][제품]` (제품 = TC 행 B열 모듈: KioskA / KioskB / Platform). 라벨만으로 제품이 특정되면 생략. (2026-07-03 피드백)
* 형식: `[라벨코드][제품] 화면명 - 현상 요약`
* 예: `[CustomerA][KioskB] Insert Chip 화면 - 배출 한도 문구 오표시`
* 예: `[MRK] 시작 화면 - '시작하기' 버튼 터치 미반응`
* 예: `[LSK] 보관함 선택 - 빈 보관함 없음 안내 미표시`

### 8.2. Description 구조

description 본문은 아래 섹션 순서로 작성.

| 순서 | 섹션 | 내용 | 필수 여부 |
| :--- | :--- | :--- | :--- |
| 1 | `### 환경` | **대상**(서비스명), **테스트 버전**(D4에서 파싱) | 필수 |
| 2 | `### 사전조건` | TC의 Pre-Condition 컬럼(F열) 값 그대로 사용 | 필수 |
| 3 | `### 재현 절차` | TC의 Test Step 기반 + 버그 재현 필요 추가 동작 | 필수 |
| 4 | `### 기대 결과` | TC의 Expected Result 기반 | 필수 |
| 5 | `### 실제 결과` | 실제 발생 현상을 구체적으로 기술 | 필수 |
| 6 | `### 관련 TC` | TC ID + Google Sheets 셀 링크 병기 | 필수 |
| 7 | `### 비고` | 명확한 참고사항 있을 때**만** 포함. 없으면 섹션 자체 넣지 않음. | 선택 |

* **환경 필드 참고:** Jira Cloud `environment` 별도 필드는 ADF 형식 제한으로 MCP에서 사용 불가. description 본문 내 `### 환경` 섹션으로 대체.
* **문체 규칙:**
  - **재현 절차:** `~한다` (간결체) — 예: `저장 버튼을 클릭한다.`
  - **기대 결과 / 실제 결과 / 비고:** `~합니다` / `~됩니다` (경어체) — 예: `저장이 실행되지 않습니다.`
* **관련 TC 링크 형식:** `TC_ID ([시트 링크](https://docs.google.com/spreadsheets/d/{spreadsheetId}/edit#gid={sheetId}&range=A{row}))`

### 8.3. 버그 이슈 필드 규칙 — 스프린트 구조 (2026-07-21 개정, 스크럼 설계 세션 합의)

> 舊 방식(시트 상단 D2 Epic/D3 라벨/D4 버전 파싱) 폐기 — 에픽 버킷 구조가 스프린트 백로그 구조로 전환되면서 시트 단위 단일값 전제가 깨짐. 정보 출처를 **행 단위 + SSOT** 로 이동.

* **parent 없음** — 버그 = 독립 이슈. QA 에픽/릴리스 에픽 버킷 금지 (에픽 = 기능 단위 원칙).
* **issue link**: 원본 백로그 티켓(TC 행 **C열**)과 `relates to` 연결 — 원인 추적은 링크로.
* **labels** (2계층 — 라벨명 하드코딩 금지):
  1. **공통 라벨** — 시트 상단 `공통 라벨 :` 줄에서 **파싱** (콤마 구분). 현재 값: `cas-scrum`(보드 소집, 누락 시 보드에 안 뜸). 라벨 정책이 바뀌면 **시트 값만 수정** — 본 규격 수정 불요.
  2. **행 단위 라벨** — 제품 = TC 행 **B열(모듈)** (KioskA / KioskB / Platform), 고객 = 원본 티켓(C열) 라벨 상속 (release 등).
* **QA 발견 버그 식별 = reporter 기준** (별도 마커 라벨 없음 — 등록 주체가 QA 계정 단일이라 충분. dev 대리 등록/QA 계정 증가 시 마커 라벨 재도입 검토).
* **affectedVersion**: 시트 상단 `Affects Version :` 줄에서 파싱 — **QA 가 등록 시 입력하는 것은 영향 버전**. **fixVersion 은 QA 가 넣지 않음** (수정이 실릴 열차는 dev/플래닝 소유 — severity 조건부 정책상 Minor 는 등록 시점에 미정).
* **sprint 배정 — severity 조건부**: 시트 상단 `Sprint :` 줄의 스프린트 기준.
  - Blocker / Critical (열차를 막는 결함) → **당 스프린트 즉시** (QA OK-Sign 전제)
  - Minor / 사소 → **백로그** → 다음 열차 (해당 항목 de-scope, 열차 정시 출발 원칙)
* **환경 섹션 버전**: 해당 모듈(B열) 버전만 기재 — 출처는 **Confluence Version 페이지(SSOT, 시트 상단 `Version :` 링크)**. 시트에 버전 값 복제 금지.
* **시트 상단 템플릿 (D2~D5)**:
  ```
  Sprint : [KioskA/KioskB]-2026-S01
  공통 라벨 : cas-scrum
  Affects Version : Release 11
  Version : {Confluence Version 페이지 링크}
  ```

### 8.4. 담당자 (Assignee)
* 사용자가 명시한 값만 사용. 기본값으로 임의 지정 안 함.

### 8.5. TC 시트 자동 업데이트
* Jira Bug 생성 후, 해당 TC의 Google Sheets 셀을 **자동으로** 업데이트.
  - **Test Result 열:** `Fail` 입력
  - **Comment & Jira link 열:** Jira 이슈 URL 입력 (예: `https://your-team.atlassian.net/browse/PROJ-1156`)
* ⚠ **열 문자는 하드코딩 금지** — 시트마다 열 구성이 다름(예: Release 10.5 탭은 J=Test Result, K=Test Result_UAT, L=Comment & Jira link). **헤더 행에서 헤더명으로 열을 찾아** 기입할 것. (2026-07 열 삽입으로 밀림 사고 이력)

---

---

## 9. QA Reporting

QA Result (Sign-off) Report 및 QA Status Report 규격은 별도 파일로 관리.

- **파일:** `QA_REPORT.md`
- **내용:** QA Result 시트 규격 (디자인 시스템, 레이아웃, 조건부 서식, 자동화 로직) + QA Status 시트 규격