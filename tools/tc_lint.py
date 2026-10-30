#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tc_lint.py — TC 표의 금지 패턴·꼴 검사기 (표준 라이브러리만).

규칙의 정본은 TC_QUICKSTART.md 다. 이 파일은 그 규칙 중 **기계가 셀 수 있는 것**만 잰다.
잴 수 없는 것(문구가 코드와 글자 그대로 같은가, 조작이 실제로 가능한가)은 반증 라운드 몫이다.

입력
  .csv / .tsv / .json / .md(파이프 표) — 확장자로 고르고, --format 으로 바꾼다.
  JSON 은 행 객체의 배열, 또는 {"rows": [...]}.
  md 는 머리 줄에 Pre/Step/Expected 열이 있는 표만 읽는다. 칸 안 줄바꿈은 <br>.

쓰는 법
  python3 tools/tc_lint.py --self-test            # 먼저: 검사기가 빨강을 낼 수 있는지
  python3 tools/tc_lint.py tc.csv
  python3 tools/tc_lint.py tc.json --col-pre pre --col-step step --col-exp exp --col-title title
  python3 tools/tc_lint.py TC_QUICKSTART.md --md-heading '고친 예'   # 그 제목 아래 표만
  python3 tools/tc_lint.py tc.csv --screen-text strings.txt          # 「」 인용·[버튼] 이 화면 문구 목록에 있나

종료 코드: 0 = 위반 0 · 1 = 위반 있음(또는 self-test 실패) · 2 = 입력을 못 읽음/검사할 행 0
행이 0 이면 통과가 아니라 2 다 — 빈 집합의 집계는 늘 통과 쪽으로 기운다.
"""
import argparse
import csv
import io
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:  # pragma: no cover
    pass

# ---------------------------------------------------------------- 열 이름
ALIASES = {
    "id": ["TC_No.", "TC_No", "TC", "tc", "id", "ID", "No."],
    "title": ["소분류", "TC Title", "title", "Title"],
    "pre": ["Pre-Condition", "Pre", "pre", "precondition", "사전 조건"],
    "step": ["Test Step", "Step", "step", "steps"],
    "exp": ["Expected Result", "Expected", "exp", "expected"],
}

# ---------------------------------------------------------------- 금지 패턴 (Pre/Step/Expected 세 칸)
# (규칙 ID, 설명, 정규식)
FORBIDDEN = [
    ("F1", "경로·URL", re.compile(r"(?<![\w.])/[A-Za-z_{.][\w.{}-]*/|https?://")),
    ("F2", "소스 파일 확장자",
     re.compile(r"\w\.(?:js|jsx|ts|tsx|java|kt|py|rb|go|php|cs|cpp|c|h|xml|sql|jsp|ftl|vue|html|css|scss|"
                r"properties|ya?ml|json|ini|conf|cfg)\b", re.I)),
    ("F3", "색상 hex", re.compile(r"(?<![\w&])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")),
    ("F4", "응답·코드 모양",
     re.compile(r"\{\s*[\"']?[A-Za-z_]\w*[\"']?\s*[:,}=]|\b[a-z_][a-z0-9_]*\s*=\s*[\w\"'{\[]|\bHTTP\s*\d{3}\b|"
                r"\b(?:true|false|null|undefined)\b")),
    ("F5", "호출 횟수",
     re.compile(r"\d+\s*(?:회|번)\s*(?:호출|요청|전송|발생한다)|정확히\s*\d+\s*(?:회|번)|호출\s*(?:횟수|수)|"
                r"\b\d+\s*times\b|\bcalled\b", re.I)),
    ("F6", "CSS 셀렉터",
     re.compile(r"(?<![\w&])#[A-Za-z_][\w-]*|(?<![\w.])\.[a-z][\w-]*[a-z0-9]\b|data-[a-z-]+=|nth-child|"
                r"querySelector|getBy[A-Z]\w*")),
    ("F7", "mock·스텁 용어",
     re.compile(r"\b(?:mock\w*|stub\w*|spy|fake|fixture|intercept\w*)\b|목업|모킹|스텁|가로채|변조|"
                r"page\.route", re.I)),
    # 대소문자 무시를 걸지 않는다 — 걸면 camelCase 식이 영어 낱말 전부에 맞는다
    ("F8", "API·호출명",
     re.compile(r"\bAPI\b|엔드포인트|[Ee]ndpoint|\b[a-z]+(?:[A-Z][a-z0-9]+)+\b|\b[a-z]+_[a-z0-9_]+\b|"
                r"[A-Za-z_]\w*\(\)|호출한다|호출된다|호출하")),
]

# Step 칸에만 거는 것: 테스트 장치·개발 도구 조작
STEP_ONLY = [
    ("F9", "테스트 장치 조작(Step 금지)",
     re.compile(r"응답.{0,25}?(?:준다|주고|고정|강제|돌려준다)|로그\S*\s*확인|상황을\s*(?:재현|연출)|재현한다|연출한다|"
                r"시뮬레이션|콘솔\S*\s*(?:확인|연다|본다)|"
                r"개발자\s*도구|DB\S*\s*(?:조회|확인)|설정 파일|강제로?\s*설정|주입한다")),
]

# Expected 칸에만 거는 것
EXP_ONLY = [
    ("S9", "주관 판정어", re.compile(r"정상\s*(?:동작|작동|처리|적으로)|올바르게|문제\s*없이|잘\s*(?:된다|동작)")),
]

TYPES = ("콘텐츠 검증", "기본 동작", "예외 사항", "안전")
TITLE_RE = re.compile(r"^(%s) · (.+?) → (.+)$" % "|".join(TYPES))
NUM_RE = re.compile(r"^(\d+)\.\s+\S")
QUOTED_BTN_RE = re.compile(r"[\"'‘“「『][^\"'’”」』]{1,30}[\"'’”」』]\s*버튼")
BARE_BTN_RE = re.compile(r"버튼")
BRACKET_RE = re.compile(r"\[([^\[\]]*)\]")
QUOTE_RE = re.compile(r"「([^」]+)」|『([^』]+)』|“([^”]+)”|\"([^\"]+)\"|‘([^’]+)’|'([^']+)'")
QUOTED_NAME_RE = re.compile(r"'[^']{1,30}'|‘[^’]{1,30}’|「[^」]{1,30}」|\"[^\"]{1,30}\"")
REQ_RE = re.compile(r"요청(?:이|을)?\s*(?:이뤄|이루어|전송|발생|간다)")
REQ_OK_RE = re.compile(r"영수증|출력|인쇄|알림|메시지|문자|메일|기록")
UNCONFIRMED = "[확인 필요]"
DEV_LABEL = "(개발자)"


def lines_of(cell):
    return [ln.strip() for ln in (cell or "").replace("\r", "").split("\n") if ln.strip()]


def check_numbered(col, cell, issues, lo, hi, rule):
    ls = lines_of(cell)
    if not ls:
        issues.append((col, rule, "비어 있다", ""))
        return ls
    nums = []
    for ln in ls:
        m = NUM_RE.match(ln)
        if not m:
            issues.append((col, rule, "번호 목록이 아니다(「1. …」꼴)", ln))
            return ls
        nums.append(int(m.group(1)))
    if nums != list(range(1, len(nums) + 1)):
        issues.append((col, rule, "번호가 1부터 차례가 아니다 %s" % nums, ""))
    if hi is not None and not (lo <= len(ls) <= hi):
        issues.append((col, rule, "%d줄 — %d~%d줄이어야 한다" % (len(ls), lo, hi), ""))
    return ls


def lint_row(row, cfg):
    """row: dict(id,title,pre,step,exp) → [(칸, 규칙, 설명, 발췌)]"""
    issues = []
    pre, step, exp, title = row.get("pre", ""), row.get("step", ""), row.get("exp", ""), row.get("title", "")

    # ---- 금지 패턴
    for col, cell in (("Pre", pre), ("Step", step), ("Expected", exp)):
        text = (cell or "").replace(UNCONFIRMED, "")
        for rid, desc, rx in FORBIDDEN:
            m = rx.search(text)
            if m:
                issues.append((col, rid, desc, m.group(0)))
        if col == "Step":
            for rid, desc, rx in STEP_ONLY:
                m = rx.search(text)
                if m:
                    issues.append((col, rid, desc, m.group(0)))
        if col == "Expected":
            for rid, desc, rx in EXP_ONLY:
                m = rx.search(text)
                if m:
                    issues.append((col, rid, desc, m.group(0)))

    # ---- 꼴
    pls = check_numbered("Pre", pre, issues, 1, cfg.pre_max, "S1")
    for ln in pls:
        body = re.sub(r"^\d+\.\s+", "", ln)
        if not re.search(r"상태\.?$", body):
            issues.append(("Pre", "S2", "「~ 상태」로 끝나지 않는다", ln))
            break

    sls = check_numbered("Step", step, issues, 1, cfg.step_max, "S3")
    for ln in sls:
        if not re.search(r"다\.?$", ln):
            issues.append(("Step", "S4", "조작 문장(「~한다」)으로 끝나지 않는다", ln))
            break

    # [버튼] 표기
    for col, cell in (("Step", step), ("Expected", exp)):
        for ln in lines_of(cell):
            m = QUOTED_BTN_RE.search(ln)
            if m:
                issues.append((col, "S5", "버튼 이름은 [이름] 으로", m.group(0)))
                break
            if col == "Step" and BARE_BTN_RE.search(ln) and not BRACKET_RE.search(ln):
                issues.append((col, "S5", "버튼을 [이름] 없이 불렀다", ln))
                break
        for m in BRACKET_RE.finditer(cell or ""):
            if m.group(0) == UNCONFIRMED:
                continue
            if not m.group(1).strip():
                issues.append((col, "S5", "빈 [ ]", m.group(0)))

    check_numbered("Expected", exp, issues, 1, None, "S6")

    # 소분류
    if cfg.check_title:
        t = (title or "").strip()
        if not TITLE_RE.match(t):
            issues.append(("소분류", "S7", "「유형 · 동작 → 결과」꼴이 아니다(유형: %s)" % "/".join(TYPES), t))
        elif len(t) > cfg.title_max:
            issues.append(("소분류", "S7", "%d자 — %d자 이하로" % (len(t), cfg.title_max), t))

    # TC 하나 = 조작 하나
    btns = {b for b in BRACKET_RE.findall(step or "")
            if b.strip() and ("[%s]" % b) != UNCONFIRMED and not re.fullmatch(r"[\d\s]+", b)}
    # 따옴표로 부른 이름도 센다 — [ ] 를 안 쓴 나쁜 TC 가 이 검사를 비켜 가지 않게
    btns |= {q for q in QUOTED_NAME_RE.findall(step or "")}
    if len(btns) > cfg.max_buttons:
        issues.append(("Step", "S8", "누르는 버튼이 %d개 — TC 하나 = 조작 하나(짝 조작은 둘까지)" % len(btns),
                       " ".join("[%s]" % b for b in sorted(btns))))
    if "→" in (step or ""):
        issues.append(("Step", "S8", "Step 한 줄에 「→」로 여러 동작을 이었다", "→"))

    # 경고(종료 코드에 안 들어감 — --strict 면 들어감)
    warns = []
    for ln in lines_of(exp):
        if REQ_RE.search(ln) and not REQ_OK_RE.search(ln):
            warns.append(("Expected", "W1", "「요청이 이뤄진다」는 밖에서 확인되는 것(영수증 등)만", ln))
    if DEV_LABEL in (step or "") or DEV_LABEL in (pre or ""):
        warns.append(("Step", "W2", "(개발자) 행 — 화면 없는 순수 API 기능인지 사람이 본다", ""))
    if cfg.screen_text is not None:
        for col, cell in (("Expected", exp),):
            for m in QUOTE_RE.finditer(cell or ""):
                q = next(g for g in m.groups() if g)
                if q.strip() == UNCONFIRMED or UNCONFIRMED in q:
                    continue
                if q not in cfg.screen_text:
                    issues.append((col, "T1", "화면 문구 목록에 없는 인용(지어낸 문구 의심)", q))
        for col, cell in (("Step", step), ("Expected", exp)):
            for b in BRACKET_RE.findall(cell or ""):
                b = b.strip()
                if not b or ("[%s]" % b) == UNCONFIRMED or re.fullmatch(r"[\d\s]+", b):
                    continue
                if b not in cfg.screen_text:
                    issues.append((col, "T2", "화면 문구 목록에 없는 버튼 이름", "[%s]" % b))
    return issues, warns


# ---------------------------------------------------------------- 입력
def pick(colnames, wanted, explicit):
    if explicit:
        if explicit not in colnames:
            print("열 '%s' 이 없다. 있는 열: %s" % (explicit, ", ".join(colnames)), file=sys.stderr)
            raise SystemExit(2)
        return explicit
    for a in ALIASES[wanted]:
        if a in colnames:
            return a
    return None


def parse_md(text, heading_re):
    tables, cur_heading, i = [], "", 0
    ls = text.splitlines()
    while i < len(ls):
        ln = ls[i]
        if ln.startswith("#"):
            cur_heading = ln.lstrip("#").strip()
        if ln.lstrip().startswith("|") and i + 1 < len(ls) and re.match(r"^\s*\|?\s*:?-{2,}", ls[i + 1]):
            block = []
            while i < len(ls) and ls[i].lstrip().startswith("|"):
                block.append(ls[i])
                i += 1
            if heading_re is None or re.search(heading_re, cur_heading):
                tables.append((cur_heading, block))
            continue
        i += 1
    rows = []
    for heading, block in tables:
        def cells(line):
            s = line.strip()
            if s.startswith("|"):
                s = s[1:]
            if s.endswith("|"):
                s = s[:-1]
            parts = re.split(r"(?<!\\)\|", s)
            return [p.strip().replace("\\|", "|").replace("<br>", "\n").replace("<br/>", "\n") for p in parts]
        head = cells(block[0])
        for b in block[2:]:
            c = cells(b)
            d = dict(zip(head, c + [""] * (len(head) - len(c))))
            d["__heading__"] = heading
            rows.append(d)
    return rows


def load(path, fmt, heading_re):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        text = f.read()
    fmt = fmt or os.path.splitext(path)[1].lstrip(".").lower()
    if fmt == "json":
        data = json.loads(text)
        if isinstance(data, dict):
            data = data.get("rows", [])
        return [{k: ("\n".join(v) if isinstance(v, list) else ("" if v is None else str(v))) for k, v in r.items()}
                for r in data]
    if fmt in ("csv", "tsv"):
        return list(csv.DictReader(io.StringIO(text), delimiter="\t" if fmt == "tsv" else ","))
    if fmt in ("md", "markdown"):
        return parse_md(text, heading_re)
    print("모르는 형식: %s (csv/tsv/json/md)" % fmt, file=sys.stderr)
    raise SystemExit(2)


def normalize(raw_rows, args):
    if not raw_rows:
        return []
    names = list(raw_rows[0].keys())
    col = {k: pick(names, k, getattr(args, "col_" + k)) for k in ALIASES}
    missing = [k for k in ("pre", "step", "exp") if not col[k]]
    rows = []
    for idx, r in enumerate(raw_rows, 1):
        if missing:
            continue  # md 의 다른 표(예: 규칙 표)는 건너뛴다
        rows.append({
            "id": (r.get(col["id"]) if col["id"] else "") or "#%d" % idx,
            "title": r.get(col["title"], "") if col["title"] else "",
            "pre": r.get(col["pre"], ""), "step": r.get(col["step"], ""), "exp": r.get(col["exp"], ""),
            "_has_title": bool(col["title"]),
        })
    return rows


# ---------------------------------------------------------------- 실행·보고
def run(rows, cfg, out=sys.stdout):
    total_err, form_bad, pat_hits, warn_n, unconfirmed = 0, 0, 0, 0, 0
    for r in rows:
        cfg.check_title = r.get("_has_title", True) and not cfg.no_title
        issues, warns = lint_row(r, cfg)
        unconfirmed += sum((r.get(k) or "").count(UNCONFIRMED) for k in ("pre", "step", "exp"))
        if any(i[1].startswith("S") for i in issues):
            form_bad += 1
        pat_hits += sum(1 for i in issues if i[1].startswith(("F", "T")))
        for col, rid, desc, ex in issues:
            print("✗ %-10s %-8s %-3s %s%s" % (r["id"], col, rid, desc, ("  | " + ex) if ex else ""), file=out)
        for col, rid, desc, ex in warns:
            print("△ %-10s %-8s %-3s %s%s" % (r["id"], col, rid, desc, ("  | " + ex) if ex else ""), file=out)
        total_err += len(issues)
        warn_n += len(warns)
    n = len(rows)
    rate = 100.0 * (n - form_bad) / n if n else 0.0
    print("— 행 %d · 금지 패턴 %d · 꼴 준수 %d/%d (%.1f%%) · 경고 %d · [확인 필요] %d"
          % (n, pat_hits, n - form_bad, n, rate, warn_n, unconfirmed), file=out)
    failed = total_err > 0 or (cfg.strict and warn_n > 0)
    return failed, total_err


class Cfg:
    pre_max = 2
    step_max = 3
    title_max = 45
    max_buttons = 2
    strict = False
    no_title = False
    check_title = True
    screen_text = None


# ---------------------------------------------------------------- self-test
CLEAN = [
    {"id": "C-1", "title": "기본 동작 · 회원증 인식 → 대출 목록 화면",
     "pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 리더에 댄다.",
     "exp": "1. 대출 목록 화면으로 넘어간다.\n2. 「대출할 책을 올려 주세요」 안내가 보인다."},
    {"id": "C-2", "title": "예외 사항 · 반납 기한 지난 책 → 대출 막힘",
     "pre": "1. 대출 목록 화면 진입 상태\n2. 회원에게 반납 기한이 지난 책이 있는 상태",
     "step": "1. 책을 받침대에 올린다.\n2. [대출하기] 를 누른다.",
     "exp": "1. 「연체 도서가 있어 대출할 수 없습니다」 안내가 보인다.\n2. 영수증이 나오지 않는다."},
    {"id": "C-3", "title": "안전 · 덮개 열림 → 대출 중단",
     "pre": "1. 대출 목록 화면 진입 상태\n2. 본체 덮개가 열려 있는 상태",
     "step": "1. [대출하기] 를 누른다.", "exp": "1. 점검 중 안내 화면으로 바뀐다.\n2. 영수증 출력 요청이 이뤄진다."},
]
# (기대 규칙, 행) — 행마다 **그 규칙 하나**를 일부러 어긴다
DIRTY = [
    ("F1", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. /loan/list 로 이동한다."}),
    ("F2", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. loan.js 가 화면을 그린다."}),
    ("F3", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. 버튼이 #ff0000 으로 바뀐다."}),
    ("F4", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. {result:0} 이 온다."}),
    ("F5", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. 조회가 정확히 1회 일어난다."}),
    ("F6", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. .loan-list 가 보인다."}),
    ("F7", {"pre": "1. 대출 서버 mock 이 켜진 상태", "step": "1. 회원증을 댄다.", "exp": "1. 목록이 보인다."}),
    ("F8", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. readMemberCard 가 끝난다."}),
    ("F9", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원 조회 응답을 서버 오류로 준다.", "exp": "1. 안내가 보인다."}),
    ("F9", {"pre": "1. 반납 화면 진입 상태", "step": "1. 반납구 걸림 상황을 재현한다.", "exp": "1. 안내가 보인다."}),
    ("S1", {"pre": "1. 첫 화면 진입 상태\n2. 프린터 연결 상태\n3. 서버 연결 상태", "step": "1. 회원증을 댄다.",
            "exp": "1. 목록이 보인다."}),
    ("S2", {"pre": "1. 대출기를 켠다", "step": "1. 회원증을 댄다.", "exp": "1. 목록이 보인다."}),
    ("S3", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 댄다.\n2. 올린다.\n3. 누른다.\n4. 뗀다.",
            "exp": "1. 목록이 보인다."}),
    ("S4", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증 인식 확인", "exp": "1. 목록이 보인다."}),
    ("S5", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. '대출하기' 버튼을 누른다.", "exp": "1. 목록이 보인다."}),
    ("S6", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "목록이 보인다."}),
    ("S7", {"title": "회원증 인식", "pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.",
            "exp": "1. 목록이 보인다."}),
    ("S8", {"pre": "1. 관리자 화면 진입 상태", "step": "1. [잠금], [해제], [초기화], [재시작] 을 차례로 누른다.",
            "exp": "1. 차례로 바뀐다."}),
    ("S8", {"pre": "1. 관리자 화면 진입 상태", "step": "1. '잠금', '해제', '재시작' 을 차례로 누른다.",
            "exp": "1. 차례로 바뀐다."}),
    ("S9", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.", "exp": "1. 정상 동작한다."}),
    ("T1", {"pre": "1. 대출기 첫 화면 진입 상태", "step": "1. 회원증을 댄다.",
            "exp": "1. 「어서 오세요, 회원님」 안내가 보인다."}),
    ("T2", {"pre": "1. 대출 목록 화면 진입 상태", "step": "1. [바로 대출] 을 누른다.", "exp": "1. 목록이 보인다."}),
]
SELFTEST_SCREEN = "대출할 책을 올려 주세요\n연체 도서가 있어 대출할 수 없습니다\n대출하기\n잠금\n해제\n초기화\n재시작\n"


def self_test():
    cfg = Cfg()
    cfg.screen_text = SELFTEST_SCREEN
    ok = True
    print("[1] 깨끗한 더미 %d행 — 위반 0 이어야 한다" % len(CLEAN))
    for r in CLEAN:
        issues, _ = lint_row(r, cfg)
        mark = "통과" if not issues else "실패"
        print("   %s %s %s" % (mark, r["id"], "" if not issues else issues))
        ok &= not issues
    print("[2] 일부러 어긴 더미 %d행 — 행마다 그 규칙이 잡혀야 한다" % len(DIRTY))
    for rid, r in DIRTY:
        r = dict(r)
        r.setdefault("title", "기본 동작 · 회원증 인식 → 목록")
        issues, _ = lint_row(r, cfg)
        got = sorted({i[1] for i in issues})
        hit = rid in got
        print("   %s %-3s 잡힘=%s" % ("통과" if hit else "실패", rid, ",".join(got) or "-"))
        ok &= hit
    print("[3] 검사할 행이 0 인 입력은 통과가 아니다(종료 코드 2)")
    import tempfile
    sys.stdout.flush()
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "empty.md")
        with open(p, "w", encoding="utf-8") as f:
            f.write("# 표 없음\n\n본문만 있다.\n")
        rc = main([p])
    print("   %s 종료 코드=%s" % ("통과" if rc == 2 else "실패", rc))
    ok &= rc == 2
    print("self-test: %s" % ("통과 — 검사기가 잡을 수 있다" if ok else "실패 — 검사기를 먼저 고쳐라"))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(description="TC 표 금지 패턴·꼴 검사 (정본 규칙: TC_QUICKSTART.md)")
    ap.add_argument("file", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--format", choices=["csv", "tsv", "json", "md"])
    ap.add_argument("--md-heading", help="md 에서 이 정규식에 맞는 제목 바로 아래 표만 읽는다")
    for k in ALIASES:
        ap.add_argument("--col-" + k, dest="col_" + k, help="%s 열 이름 (기본: %s)" % (k, " / ".join(ALIASES[k])))
    ap.add_argument("--pre-max", type=int, default=2)
    ap.add_argument("--step-max", type=int, default=3)
    ap.add_argument("--title-max", type=int, default=45)
    ap.add_argument("--max-buttons", type=int, default=2)
    ap.add_argument("--no-title", action="store_true", help="소분류 검사를 끈다")
    ap.add_argument("--screen-text", help="화면 문구 원문 파일 — Expected 의 「」 인용과 Step·Expected 의 [버튼] 이 이 안에 글자 그대로 있어야 한다")
    ap.add_argument("--strict", action="store_true", help="경고도 실패로 센다")
    a = ap.parse_args(argv)

    if a.self_test:
        return 0 if self_test() else 1
    if not a.file:
        ap.error("파일을 주거나 --self-test")
    cfg = Cfg()
    cfg.pre_max, cfg.step_max, cfg.title_max, cfg.max_buttons = a.pre_max, a.step_max, a.title_max, a.max_buttons
    cfg.strict, cfg.no_title = a.strict, a.no_title
    if a.screen_text:
        with open(a.screen_text, encoding="utf-8-sig") as f:
            cfg.screen_text = f.read()
    try:
        rows = normalize(load(a.file, a.format, a.md_heading), a)
    except (OSError, ValueError) as e:
        print("입력을 못 읽었다: %s" % e, file=sys.stderr)
        return 2
    if not rows:
        print("검사할 행이 0 — 통과가 아니다(열 이름·--md-heading 을 확인)", file=sys.stderr)
        return 2
    failed, _ = run(rows, cfg)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
