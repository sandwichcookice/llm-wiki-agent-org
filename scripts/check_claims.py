"""第二版新增的檢查（在「查詢 Wiki」之後、撰寫之前執行）。用法：python3 scripts/check_claims.py v2
1. 每個論點的錨點（anchor）必須逐字出現在它指定的 Wiki 頁（忽略 ** 與空白差異）。
2. 投影片的 src 必須正好等於它所有論點用到的頁，避免「內容來自別頁、卻標這一頁」。
3. TERMS 裡的術語，第一次出現必須在名詞解釋那張投影片（含）之後。"""
import sys, re, importlib.util, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("s", ROOT / "slides" / "build" / f"slides_{sys.argv[1]}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
norm = lambda s: re.sub(r"\s+", "", s.replace("**", ""))
TERMS = ["子代理", "brief", "run", "hook", "worktree", "org.py", "PRD", "決策信", "VETO", "BLOCK"]
errors, n = [], 0
gi = next((i for i, s in enumerate(m.SLIDES) if s.get("glossary")), None)
if gi is None: errors.append("沒有名詞解釋投影片")
for i, s in enumerate(m.SLIDES, 1):
    pages = set()
    for c in s["claims"]:
        n += 1; pages.add(c["page"])
        f = ROOT / "wiki" / c["page"]
        if not f.exists(): errors.append(f"第 {i} 張：頁面不存在 {c['page']}"); continue
        if norm(c["anchor"]) not in norm(f.read_text(encoding="utf-8")):
            errors.append(f"第 {i} 張「{s['title']}」：錨點不在 {c['page']} → {c['anchor'][:30]}")
    if set(s["src"]) != pages: errors.append(f"第 {i} 張「{s['title']}」：src {sorted(s['src'])} ≠ 論點用到的頁 {sorted(pages)}")
    text = s["title"] + " ".join(c["text"] for c in s["claims"]) + s.get("ex", "")
    if gi is not None and i - 1 < gi:
        for t in TERMS:
            if re.search(rf"(?<![A-Za-z]){re.escape(t)}(?![A-Za-z])", text): errors.append(f"第 {i} 張在名詞解釋之前就用了「{t}」")
print(f"檢查 {len(m.SLIDES)} 張、{n} 個論點，錯誤 {len(errors)} 個")
for e in errors: print(" ✗", e)
sys.exit(1 if errors else 0)
