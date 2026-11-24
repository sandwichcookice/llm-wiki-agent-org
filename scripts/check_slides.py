"""教學簡報的程式檢查。用法：python3 scripts/check_slides.py
規則：至少 8 張；每張 <section class="slide"> 都有 data-sources；
每個來源都是 wiki/ 裡存在的頁；頁尾的來源連結和 data-sources 一致；標題不重複。"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
html = (ROOT / "slides" / "index.html").read_text(encoding="utf-8")
slides = re.findall(r'<section class="slide"([^>]*)>(.*?)</section>', html, re.S)
errors, titles = [], []
if len(slides) < 8: errors.append(f"投影片只有 {len(slides)} 張，至少要 8 張")
for i, (attrs, body) in enumerate(slides, 1):
    t = re.search(r"<h[12][^>]*>(.*?)</h[12]>", body, re.S)
    title = re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else ""
    if not title: errors.append(f"第 {i} 張沒有標題")
    if title in titles: errors.append(f"第 {i} 張標題重複：{title}")
    titles.append(title)
    m = re.search(r'data-sources="([^"]*)"', attrs)
    srcs = [s.strip() for s in m.group(1).split(",") if s.strip()] if m else []
    if not srcs: errors.append(f"第 {i} 張「{title}」沒有 data-sources"); continue
    for s in srcs:
        if not (ROOT / "wiki" / s).exists(): errors.append(f"第 {i} 張「{title}」引用不存在的頁 {s}")
    links = set(re.findall(r'href="\.\./wiki/([^"]+)\.html"', body))
    want = {s[:-3] for s in srcs}
    if links != want: errors.append(f"第 {i} 張「{title}」頁尾連結 {sorted(links)} 和 data-sources {sorted(want)} 不一致")
print(f"檢查 {len(slides)} 張投影片，錯誤 {len(errors)} 個")
for e in errors: print(" ✗", e)
sys.exit(1 if errors else 0)
