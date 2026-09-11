# [품질 앵커] 유닛 테스트 — 칩 교환 금액 계산 helper

> repo: 자동화 오케스트레이터  ·  프레임워크: vitest  ·  테스트 파일: `src/lib/exchange.test.ts`  ·  작성일: 2026-07-01
> (예시 — 실제 대상은 repo 소스로 계약 재확인. 값·경계는 스펙 확인 후 확정)

## 대상 계약
- **입력**: `calcChips(cashAmount: number, unit: number)` — 투입 현금, 최소 교환단위
- **출력**: `{ chips: number, remainder: number }` — 지급 칩 수, 잔돈
- **부작용**: 없음(순수 함수)
- **에러 경로**: `unit <= 0` → throw `InvalidUnitError`; `cashAmount < 0` → throw

## 케이스 목록

| # | 테스트 이름 | 무엇을 검증 | 구분 |
| :- | :-- | :-- | :-- |
| 1 | returns_full_chips_on_exact_multiple | 딱 떨어지는 금액 → 잔돈 0 | 정상 |
| 2 | returns_remainder_below_unit | 단위 미만 잔돈 반환 | 경계(BVA) |
| 3 | zero_chips_when_below_unit | 단위 미만 투입 → 칩 0, 전액 잔돈 | 경계 |
| 4 | zero_cash_returns_zero | 0원 투입 | 경계 |
| 5 | throws_on_zero_unit | unit 0 → 에러 | 예외 |
| 6 | throws_on_negative_cash | 음수 → 에러 | 예외 |

## 테스트 코드
```ts
import { describe, it, expect } from 'vitest'
import { calcChips, InvalidUnitError } from './exchange'

describe('calcChips', () => {
  it('returns_full_chips_on_exact_multiple', () => {
    expect(calcChips(1000, 100)).toEqual({ chips: 10, remainder: 0 })
  })

  it('returns_remainder_below_unit', () => {
    expect(calcChips(1050, 100)).toEqual({ chips: 10, remainder: 50 })
  })

  it('zero_chips_when_below_unit', () => {
    expect(calcChips(50, 100)).toEqual({ chips: 0, remainder: 50 })
  })

  it('zero_cash_returns_zero', () => {
    expect(calcChips(0, 100)).toEqual({ chips: 0, remainder: 0 })
  })

  it('throws_on_zero_unit', () => {
    expect(() => calcChips(1000, 0)).toThrow(InvalidUnitError)
  })

  it('throws_on_negative_cash', () => {
    expect(() => calcChips(-100, 100)).toThrow()
  })
})
```

## 실행 결과
```
 ✓ src/lib/exchange.test.ts (6)
   ✓ calcChips (6)
 Test Files  1 passed (1)
      Tests  6 passed (6)
```
- **역검증**: `exchange.ts` 의 `Math.floor` → `Math.round` 로 바꾸니 #2 red 확인(1050/100 이 11칩으로 과지급 잡힘) → 테스트 유효. 원복 완료.

## 커버 못 한 것 / 의심점
- **N/T**: 실제 카세트 잔량 연동(HW mock 필요) — 순수 계산 범위 밖. 통합 테스트 스코프.
- **의심점**: 단위 미만 투입 시 "칩 0 + 전액 잔돈"이 스펙인지, "투입 거부"가 스펙인지 애매. **버그 단정 아님** — cashrecycler 스펙/에러코드 확인 후 사람 QA confirm. [[feedback_spec_check_before_jira]]
