"""LLM Wiki 的程式檢查：連結、來源標記、index 完整度。用法：python3 scripts/lint_wiki.py"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
raw_ids = {p.stem for p in RAW.glob("*.md")}
pages = sorted(list((WIKI / "sources").glob("*.md")) + list((WIKI / "concepts").glob("*.md")))
errors = []
LINK = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
SRC = re.compile(r"\[來源:\s*([^\]]+)\]")
for page in pages + [WIKI / "index.md"]:
    if not page.exists():
        errors.append(f"缺少檔案 {page.relative_to(ROOT)}"); continue
    text = page.read_text(encoding="utf-8")
    rel = page.relative_to(ROOT)
    for target in LINK.findall(text):
        if target.startswith("http"): continue
        if not (page.parent / target).resolve().exists():
            errors.append(f"{rel}: 連結不存在 → {target}")
    for ids in SRC.findall(text):
        for i in [x.strip() for x in ids.split(",")]:
            if i not in raw_ids: errors.append(f"{rel}: 來源 id 不存在 → {i}")
    if page.name == "index.md": continue
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text)]
    in_related = False
    for k, b in enumerate(blocks):
        if not b or b.startswith("#"):
            in_related = b.startswith("## 相關頁面"); continue
        if in_related or SRC.search(b): continue
        nxt = blocks[k + 1] if k + 1 < len(blocks) else ""
        if b.startswith("|") and SRC.search(nxt): continue  # 表格的來源寫在緊接的下一段
        errors.append(f"{rel}: 段落沒有來源標記 → {b[:40]}…")
index = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
for p in pages:
    if p.relative_to(WIKI).as_posix() not in index:
        errors.append(f"index.md 沒列出 {p.relative_to(WIKI).as_posix()}")
for rid in raw_ids:
    if not (WIKI / "sources" / f"{rid}.md").exists(): errors.append(f"raw/{rid}.md 沒有對應的 sources 頁")
print(f"檢查 {len(pages)} 頁，{len(raw_ids)} 篇原文，錯誤 {len(errors)} 個")
for e in errors: print(" ✗", e)
sys.exit(1 if errors else 0)
