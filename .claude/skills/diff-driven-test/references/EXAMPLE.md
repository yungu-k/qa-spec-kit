# [품질 앵커] Diff 영향도 테스트 — KioskA RFID (PROJ-1613 전례 기반)

> baseline(마지막 검증 ref): `release`(=1.3.1.3, 10.5차 검증완료)  ↔  latest: 최신 head
> 근거: Release 10.5 시트PROJ-1613 RFID 14건 전부 PASS  ·  작성일: 2026-07-01
> (교훈 예시 — baseline 을 PROD 1.3.0.13 으로 잘못 잡아 7건 신규 오검출 후 삭제한 사건)

## 변경 요약
- diff 명령: `git diff origin/prod..origin/release` (로컬 mock 커밋 회피 위해 remote ref 직접)
- **핵심 교훈**: PROD(1.3.0.13) 를 baseline 으로 잡으면 이미 10.5차에서 검증된 RFID 14건이 "신규"로 잡힘 → 오검출. **올바른 baseline = 마지막 검증완료 ref(release 1.3.1.3)** → 미검증 delta 는 실제로 0.

## 영향도 표

| # | 변경점 (테스터 언어) | 분류 | 테스트 케이스 | N/T |
| :- | :-- | :-- | :-- | :-: |
| 1 | Platform > KIOSK Management 'RFID operating mode' 드롭다운 3종 | 변경 | Disabled/Logging Only/Strict 선택별 동작 + 권한별 비활성 확인 | (10.5 검증완료) |
| 2 | Transaction Log > KioskA > History by Chip Cartridge RFID 개수·값 표시 | 변경 | 카트리지별 RFID 개수·값 노출 + 엑셀 export | (검증완료) |
| 3 | UnderPay/OverPay/권종불일치/Detect우선 에러(200018~200021) | 변경 | 각 케이스 화면·거래내역 에러코드 노출 | (검증완료) |

## git 밖 변경 확인
- **DB 스키마**: Platform 측 신규 `tb_cartridge_rfid` 등 — dev 미푸시분 존재(platform-uat). diff 밖 → 별도 확인 필요.

## 미완 / 대기
- Platform RFID(RL2-002-1~4): baseline `platform-rollback-1.0.3.0` ↔ `platform-uat`. 단 **platform-uat 에 미푸시 웹소스 + DB 스키마 변경 존재** → 현 TC 는 푸시분까지만 부분 커버. **dev 푸시 후 재fetch → 재diff 로 보강 예정.**
- **교훈**: bundled commit(RFID 검증분 + 타 모듈/Dashboard 미검증분 번들)은 수동 판별. 버전 태그·코드 상수 없으면 기계 매핑 불가 → 수동.
