# Figma 변경 감지 + TC 커버리지 갭 분석

Figma 디자인 변경 감지, TC 시트 비교, 커버리지 갭 리포트.

## 입력
- `$ARGUMENTS`: 대상 프로젝트 (`MRK` 또는 `LSK` 또는 `all`)
  - 미입력시 `all`

## 처리 절차

### 1단계: Figma 변경 감지
1. `scripts/figma_snapshot.py` 실행, Figma 페이지별 현재 노드 트리 추출.
2. `snapshots/` 이전 스냅샷과 비교, 변경사항(추가/삭제/변경 화면) 감지.
3. 변경 없으면 "변경 없음" 보고 후 종료.

### 2단계: TC 커버리지 갭 분석
변경 감지시:
1. 변경 화면 목록 추출 (추가 화면, 하위 요소 변경 화면).
2. 대상 스프레드시트 Full Test Case 시트에서 TC 목록 읽기.
3. 변경 화면명과 TC 소분류(D열) 매핑, **미커버 변경 화면** 식별.
4. 결과 리포트:
   - 추가 화면 중 TC 없는 항목
   - 변경 화면 중 TC 업데이트 필요 항목
   - 삭제 화면 중 TC 제거 필요 항목

### 3단계: TC 업데이트 제안
사용자 "반영해줘" 시:
- 추가 화면 TC 신규 설계 (TC_DESIGN_GUIDE.md 규격 준수)
- 삭제 화면 TC N/A 처리 또는 삭제 제안
- 변경 화면 TC Step/Expected 현행화

## 대상 Figma 페이지

| 프로젝트 | 페이지 ID | 페이지명 |
|---|---|---|
| MRK | 2207:14776 | 사용자_멤버십 |
| MRK | 3815:2102 | 어드민콘솔_멤버십 |
| MRK | 1498:9915 | Platform_멤버십 |
| LSK | 2207:14777 | 사용자_짐보관 |
| LSK | 3815:9168 | 어드민콘솔_짐보관 |
| LSK | 2735:830 | Platform_짐보관 |

## Figma 연동
- **토큰:** `figma-token.json` (Personal Access Token)
- **API:** Figma REST API (`/v1/files/:fileKey/nodes`)
- **스냅샷:** `snapshots/` 디렉토리에 페이지별 JSON 저장

## 주의사항
- Ctrl+Z 등 되돌린 경우 lastModified 변경되나, 노드 트리 diff 실질 변경 없음으로 필터링.
- comment, MEMO, Description 등 비-UI 노드 자동 제외.
- hidden 노드 감지하되 TC 대상 제외.
- TC 자동 업데이트는 사용자 확인 후만 수행.