# [Template] Hotfix QA Verification Report (PDF)

Hotfix / 소규모 배포건 검증 완료 보고용 **간단 PDF** 리포트 템플릿.

> **정식 Sign-off 와 구분:** 39행 Google Sheets 풀포맷 QA Result 는 [`QA_REPORT.md`](./QA_REPORT.md) §9 사용. 본 템플릿은 Hotfix 처럼 항목 수 적고 빠른 PDF 산출이 필요할 때 사용.

---

## 1. 작성 규칙 (QA_REPORT.md 준수)

* **언어:** 헤더/라벨 = 영문, 내용(QA Opinion, 검증 항목) = 한국어
* **Verdict:** 전체 대문자 — `PASS` / `CONDITIONAL PASS` / `FAIL` / `ON HOLD`
* **검증 항목:** 콤마 나열 금지 → 번호 목록 + 마지막 줄 `— N건 전체 Pass/N/A` 요약
* **사실 기반:** 실제 검증 결과만 기술. 유추/허위 금지.
* **강조색:** 치명/구조적 리스크 문구 = Red(`#D11A1A`) inline 표기 가능.

### Verdict → 배지 색상 (QA_REPORT §9.3)

| Verdict | 색상 |
| :--- | :--- |
| `PASS` | `#34A853` |
| `CONDITIONAL PASS` | `#FFC107` |
| `FAIL` | `#D11A1A` |
| `ON HOLD` | `#999999` |

### Result 셀 색상 (Verification Details)

| 값 | 색상 |
| :--- | :--- |
| `PASS` | `#1E8449` |
| `FAIL` | `#CD1C1C` |
| `N/A` | `#7F8C8D` |

---

## 2. 섹션 구조

1. **QA Opinion** — 메타 표(Verdict / Date / QA Lead / Epic) + 종합 의견 본문
2. **Verification Details** — Test Area별 핵심 검증 항목 + Result
3. **Decision Required (Known Issue)** — *(선택)* 잔여 리스크 / 의사결정 필요건. 없으면 섹션 삭제.

---

## 3. HTML 템플릿

> `{{PLACEHOLDER}}` 치환 후 PDF 변환. Verification 행 / Decision 블록은 건수 따라 복제·삭제.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
  @page { size: A4; margin: 18mm 16mm; }
  * { box-sizing: border-box; }
  body { font-family: "IBM Plex Sans", "Malgun Gothic", "맑은 고딕", sans-serif; color: #1c2833; font-size: 10.5pt; line-height: 1.5; margin: 0; }
  .title { background: #2C3E50; color: #fff; padding: 14px 18px; font-size: 16pt; font-weight: 700; border-radius: 4px; }
  .subtitle { color: #5D6D7E; font-size: 9.5pt; margin: 6px 2px 18px; }
  h2 { background: #34495E; color: #fff; font-size: 11pt; font-weight: 700; padding: 7px 12px; margin: 22px 0 0; border-radius: 3px; }
  table { width: 100%; border-collapse: collapse; margin-top: 0; }
  th, td { border: 1px solid #B3B3B3; padding: 7px 9px; vertical-align: top; }
  th { background: #EAECEE; font-weight: 700; font-size: 9.5pt; }
  td { font-size: 10pt; }
  .meta th { width: 18%; text-align: left; }
  .meta td { width: 32%; }
  .verdict { display: inline-block; padding: 3px 12px; border-radius: 3px; color: #fff; font-weight: 700; background: {{VERDICT_COLOR}}; }
  .area { width: 22%; background: #F7F8F9; font-weight: 700; }
  .res-pass { color: #1E8449; font-weight: 700; text-align: center; }
  .res-fail { color: #CD1C1C; font-weight: 700; text-align: center; }
  .res-na { color: #7F8C8D; font-weight: 700; text-align: center; }
  ol { margin: 0 0 0 16px; padding: 0; }
  ol li { margin: 2px 0; }
  .flag { background: #FEF9E7; border-left: 4px solid #F1C40F; padding: 10px 14px; margin-top: 4px; font-size: 10pt; }
  .flag b { color: #B9770E; }
  .red { color: #D11A1A; }
  .foot { margin-top: 24px; color: #95A5A6; font-size: 8.5pt; text-align: right; }
</style>
</head>
<body>
  <div class="title">{{REPORT_TITLE}}</div>
  <div class="subtitle">{{SUBTITLE}}</div>

  <h2>1. QA Opinion</h2>
  <table class="meta">
    <tr><th>Verdict</th><td><span class="verdict">{{VERDICT}}</span></td><th>Date</th><td>{{DATE}}</td></tr>
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
      <td class="res-pass">{{RESULT}}</td>  <!-- class: res-pass / res-fail / res-na -->
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
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
$html = "<작성한 .html 경로>"
$out  = "C:\Users\공윤구\Desktop\QA\Report\<리포트명>.pdf"
$url  = "file:///" + ($html -replace '\\','/')
Start-Process -FilePath $edge -ArgumentList @(
  "--headless","--disable-gpu","--no-pdf-header-footer",
  "--print-to-pdf=`"$out`"","`"$url`""
) -Wait -WindowStyle Hidden
```

* `--no-pdf-header-footer` = 페이지 상하단 URL/날짜 자동 삽입 제거.
* 한글 폰트 = `Malgun Gothic` fallback 내장(IBM Plex Sans 미설치여도 정상).

### 파일 네이밍 룰 (고정)

```
{버전}_Hotfix_QA_Report_{YYYY-MM-DD}.pdf
```

* 예: `10.1th_Hotfix_QA_Report_2026-06-29.pdf`
* `{버전}` = 배포 차수(Version 페이지 표기, 예 `10.1th`). `{YYYY-MM-DD}` = 검증 완료일.
* 저장 위치: `C:\Users\공윤구\Desktop\QA\Report\`

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

안녕하세요, QA 공윤구입니다.
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
