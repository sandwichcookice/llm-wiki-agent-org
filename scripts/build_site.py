"""把 wiki/*.md 轉成可瀏覽的 HTML（site/），並複製簡報。用法：python3 scripts/build_site.py（需要 markdown 套件）"""
import re, shutil, pathlib, markdown
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "docs"
CSS = """body{font-family:"PingFang TC","Noto Sans TC",sans-serif;max-width:860px;margin:0 auto;padding:24px 16px 64px;line-height:1.75;color:#1f2933;background:#fbfbf9}
a{color:#1d5fa8}nav{font-size:14px;margin-bottom:18px;padding-bottom:10px;border-bottom:1px solid #ddd}
h1{font-size:26px}h2{font-size:19px;margin-top:28px}table{border-collapse:collapse;width:100%;font-size:14px}
th,td{border:1px solid #ccc;padding:5px 8px;vertical-align:top}th{background:#eef1f4}code{background:#eef1f4;padding:0 4px;border-radius:3px}
.src{color:#6b7280;font-size:12.5px}"""
def page(title, body, depth):
    up = "../" * depth
    nav = f'<nav><a href="{up}index.html">首頁</a> · <a href="{up}wiki/index.html">Wiki 目錄</a> · <a href="{up}wiki/log.html">討論與 ingest 紀錄</a> · <a href="{up}slides/index.html">教學簡報</a></nav>'
    return f'<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head><body>{nav}{body}</body></html>'
if SITE.exists(): shutil.rmtree(SITE)
for md in (ROOT / "wiki").rglob("*.md"):
    rel = md.relative_to(ROOT / "wiki")
    text = md.read_text(encoding="utf-8")
    text = re.sub(r"\]\(([^)#\s]+)\.md(#[^)]*)?\)", lambda m: f"]({m.group(1)}.html{m.group(2) or ''})", text)
    html = markdown.markdown(text, extensions=["tables", "fenced_code"])
    html = re.sub(r"\[來源:\s*([^\]]+)\]", r'<span class="src">[來源: \1]</span>', html)
    title = re.search(r"^#\s+(.+)$", text, re.M)
    out = SITE / "wiki" / rel.with_suffix(".html"); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(title.group(1) if title else rel.stem, html, len(rel.parts)), encoding="utf-8")
(SITE / "slides").mkdir(parents=True, exist_ok=True)
shutil.copy(ROOT / "slides" / "index.html", SITE / "slides" / "index.html")
if (ROOT / "logs" / "run_log.md").exists():
    (SITE / "logs").mkdir(exist_ok=True)
    rl = markdown.markdown((ROOT / "logs" / "run_log.md").read_text(encoding="utf-8"), extensions=["tables"])
    (SITE / "logs" / "run_log.html").write_text(page("執行與檢查紀錄", rl, 1), encoding="utf-8")
home = """<h1>LLM Wiki：agent-org</h1><p>雲科 B11517038 資工 郭益閎｜TAICA 生成式 AI 第十週作業。</p>
<p>這是一個由 Claude Code 維護的 LLM Wiki，主題是我自己做的 Claude Code plugin「agent-org」：把公司的軟體開發流程搬進 Claude Code，PM、架構師、工程師、審查委員會、QA、Release 各是一個子代理。教學簡報只用這個 Wiki 當知識來源產生。</p>
<ul><li><a href="slides/index.html">教學簡報：agent-org 是什麼？</a></li><li><a href="wiki/index.html">Wiki 目錄</a></li>
<li><a href="wiki/log.html">先討論、後生成：討論與 ingest 紀錄</a></li><li><a href="logs/run_log.html">loop / graph 執行與檢查紀錄</a></li></ul>"""
(SITE / "index.html").write_text(page("LLM Wiki：agent-org", home, 0), encoding="utf-8")
print("site 產生完成：", sum(1 for _ in SITE.rglob("*.html")), "個 HTML")
