# [Template] Hotfix QA Verification Report (PDF)

Hotfix / 소규모 배포건 검증 완료 보고용 **간단 PDF** 리포트 템플릿.

> **정식 Sign-off 와 구분:** 39행 Google Sheets 풀포맷 QA Result 는 [`QA_REPORT.md`](./QA_REPORT.md) §9 사용. 본 템플릿은 Hotfix 처럼 항목 수 적고 빠른 PDF 산출이 필요할 때 사용.

---

## 0. 스타일 규약 (2026-08-21 확정)

**이 템플릿을 쓰는 세션은 내용만 쓴다. 스타일은 짜지 않는다.**
스타일의 원본은 [`assets/report.css`](./assets/report.css) 한 벌이고,
리포트 HTML 은 **클래스만** 쓴다. `<style>` 신설 · 인라인 `style=` · 임의 hex **금지.**

발행 전 **디자이너 세션 검토 + 글리프 감사**를 거친다. 규약 상세는
[`REPORT_STYLE_POLICY.md`](./REPORT_STYLE_POLICY.md), 역할 경계는
[`SESSION_ROLES.md`](./SESSION_ROLES.md) §5.

---

## 1. 작성 규칙 (QA_REPORT.md 준수)

* **언어:** 헤더/라벨 = 영문, 내용(QA Opinion, 검증 항목) = 한국어
* **Verdict:** 전체 대문자 — `PASS` / `CONDITIONAL PASS` / `FAIL` / `ON HOLD`
* **검증 항목:** 콤마 나열 금지 → 번호 목록 + 마지막 줄 `— N건 전체 PASS/N/A` 요약
* **사실 기반:** 실제 검증 결과만 기술. 유추/허위 금지.
* **강조:** 치명/구조적 리스크 문구는 `class="red"`. **색을 직접 쓰지 않는다.**

### Verdict → 배지 클래스

| Verdict | 클래스 |
| :--- | :--- |
| `PASS` | `verdict pass` |
| `CONDITIONAL PASS` | `verdict cond-pass` |
| `FAIL` | `verdict fail` |
| `ON HOLD` | `verdict on-hold` |

### Result 셀 클래스 (Verification Details)

| 값 | 클래스 |
| :--- | :--- |
| `PASS` | `res-pass` |
| `FAIL` | `res-fail` |
| `N/A` | `res-na` |
| `N/T` (현 시점 검증 불가) | `res-nt` |

> 색 값은 전부 `assets/report.css` 안에 있다. **여기에 hex 를 다시 적지 않는다** —
> 두 군데 적히는 순간 어느 쪽이 원본인지 알 수 없게 된다.

---

## 2. 섹션 구조

1. **QA Opinion** — 메타 표(Verdict / Date / QA Lead / Epic) + 종합 의견 본문
2. **Verification Details** — Test Area별 핵심 검증 항목 + Result
3. **Decision Required (Known Issue)** — *(선택)* 잔여 리스크 / 의사결정 필요건. 없으면 섹션 삭제.

---

## 3. HTML 템플릿

> `{{PLACEHOLDER}}` 치환 후 PDF 변환. Verification 행 / Decision 블록은 건수 따라 복제·삭제.
> **`<style>` 블록이 없는 게 정상이다** — 스타일은 `assets/report.css` 한 벌뿐(§0).
> HTML 을 리포트 폴더에 두면 `href` 의 상대 경로를 그 위치에 맞게 조정한다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="assets/report.css">
</head>
<body>
  <div class="title">{{REPORT_TITLE}}</div>
  <div class="subtitle">{{SUBTITLE}}</div>

  <h2>1. QA Opinion</h2>
  <table class="meta">
    <tr><th>Verdict</th><td><span class="verdict {{VERDICT_CLASS}}">{{VERDICT}}</span></td><th>Date</th><td>{{DATE}}</td></tr>
    <tr><th>QA Lead</th><td>{{QA_LEAD}}</td><th>Epic</th><td>{{EPIC}}</td></tr>
  </table>
  <table><tr><td>{{QA_OPINION}}</td></tr></table>

  <h2>2. Verification Details</h2>
  <table>
    <tr><th style="width:22%">Test Area</th><th>Key Verification Items</th><th style="width:14%">Result</th></tr>
    <!-- 행 복제 단위 -->
    <tr>
      <td class="area">{{AREA_NAME}}</td>
      <td>
        <ol>
          <li>{{ITEM_1}}</li>
          <li>{{ITEM_2}}</li>
        </ol>
        — {{ITEM_SUMMARY}}
      </td>
      <td class="res-pass">{{RESULT}}</td>  <!-- class: res-pass / res-fail / res-na / res-nt -->
    </tr>
  </table>

  <!-- 잔여 리스크 없으면 아래 섹션 통째 삭제 -->
  <h2>3. Decision Required (Known Issue)</h2>
  <div class="flag">
    <b>{{ISSUE_TITLE}}</b><br>
    {{ISSUE_DESC}}<br><br>
    → <b>의사결정 필요:</b> {{DECISION_ASK}}
  </div>

  <div class="foot">Generated {{DATE}} · QA · {{COMPANY}} · {{CUSTOMER}}</div>
</body>
</html>
```

---

## 4. PDF 변환 (headless Edge)

> 별도 PDF 라이브러리 불필요. Win11 기본 Edge 사용. 외부 호스팅 안 함 → 리포트 호스팅 정책 부합.

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
* 한글 폰트 = `Malgun Gothic` fallback 내장(IBM Plex Sans 미설치여도 정상).
* ⚠️ **파일명을 반드시 인자로 준다.** 인자를 안 받거나 기본값으로 폴더를 훑는 형태로 만들면
  **폴더 전체가 재렌더**된다. 실제로 남의 산출물까지 덮어쓴 사고가 있었다.

### ⚠️ 발행 전 글리프 감사 (필수)

**브라우저 headless 인쇄 파이프라인에서는 폰트에 없는 문자가 조용히 사라진다.**
실측: `−`(U+2212) · `⚡`(U+26A1) · `✓`(U+2713) 는 **PDF 에서 소실**,
`→ ÷ ↳ ※ ① ② ⟳ ✗ — ↑ ↔` 는 정상. **`✗`(U+2717)는 살고 `✓`(U+2713)는 죽는다** —
짐작으로 고를 수 없다.

`−` 는 **ASCII 하이픈과 육안 구분이 안 돼** 검수로는 절대 못 잡는다.
아래 §5 의 "발송 전 최종 검수" 로도 안 걸린다.

→ **소스 HTML + 산출 PDF 두 층위를 다 감사한다.** 절차·self-test·엔티티 우회 함정은
[`VERIFICATION_GUIDE.md`](./VERIFICATION_GUIDE.md) §4.

### 파일 네이밍 룰 (고정)

```
{버전}_Hotfix_QA_Report_{YYYY-MM-DD}.pdf
```

* 예: `10.1th_Hotfix_QA_Report_2026-06-29.pdf`
* `{버전}` = 배포 차수(Version 페이지 표기, 예 `10.1th`). `{YYYY-MM-DD}` = 검증 완료일.
* 저장 위치: 팀 리포트 폴더 (사내 저장소·공유 드라이브). **외부 호스팅 금지** — `QA_REPORT.md` §11.3

---

## 5. 사용 예시 (10.1th Hotfix, PROJ-1804)

| 필드 | 값 |
| :--- | :--- |
| REPORT_TITLE | `QA Report — 10.1th Hotfix (CustomerA)` |
| VERDICT / COLOR | `CONDITIONAL PASS` / `#FFC107` |
| Test Area | NFC Reader Issue (PASS) / Conveyor Camera 녹화 (PASS) |
| Decision | NFC "Back to Normal" 오탐 구조 한계 → 추가 패치 여부 결정 |

---

## 6. 메일 본문 요약 (PDF 첨부와 한 세트)

> **원칙:** PDF 는 첨부(상세·아카이브). **판정·결정요청은 메일 본문 텍스트로 박아 zero-click 으로 읽히게.** "첨부 참고"로만 끝내면 결정건은 안 움직임 → 결정 필요건은 **담당 지목 + 명시 요청**.

### 작성 규칙

* **제목에 판정 포함** — 열기 전 보이게. 예: `[QA] {버전} Hotfix 검증 완료 — {VERDICT}`
* **본문 순서 (위에서부터 읽힘):** ① 판정 → ② 검증 결과(Area별 1줄) → ③ 결정 필요(★) → ④ "상세는 첨부 참고"
* **결정 필요건:** "참고 부탁" 금지(수동). **담당자 지목 + "결정 부탁드립니다" 직접 요청.** 없으면 ③ 생략.
* 메일 플랫폼(다우오피스/Gmail) 무관 — 순수 텍스트라 렌더 안 깨짐.

### 본문 템플릿

```
제목: [QA] {버전} Hotfix 검증 완료 — {VERDICT}

안녕하세요, QA {작성자}입니다.
{버전} Hotfix 검증 완료되어 결과 공유드립니다.

■ 판정: {VERDICT}
■ 검증 결과
  - {Area1}: {1줄 요약} ({Pass/Fail})
  - {Area2}: {1줄 요약} ({Pass/Fail})

■ 결정 필요 (★)         ← 없으면 블록 삭제
  {이슈 요약 1~2줄}. {결정 요청 내용} 부탁드립니다. (담당: {지목}님)

상세 내용은 첨부 리포트 참고 부탁드립니다.
```

### 예시 (10.1th)

```
제목: [QA] 10.1th Hotfix 검증 완료 — CONDITIONAL PASS

안녕하세요, QA {작성자}입니다.
10.1th Hotfix 검증 완료되어 결과 공유드립니다.

■ 판정: CONDITIONAL PASS
■ 검증 결과
  - NFC Reader: retry 수정 + 실패알림 미발송 확인 (Pass)
  - Conveyor Camera 녹화: 신규 dll 재검증, 특이사항 없음 (Pass)

■ 결정 필요 (★)
  NFC "Back to Normal" 오탐 — 물리 이슈 미해결인데 정상 복구 알림이
  발송되는 구조적 한계. 추가 패치 여부 결정 부탁드립니다. (담당: ○○○님)

상세 내용은 첨부 리포트 참고 부탁드립니다.
```
