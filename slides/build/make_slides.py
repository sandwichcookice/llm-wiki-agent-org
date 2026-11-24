"""由 slides/build/slides_<ver>.py 的投影片資料產生 slides/index.html。用法：python3 slides/build/make_slides.py v1"""
import sys, importlib.util, pathlib, html
HERE = pathlib.Path(__file__).resolve().parent
ver = sys.argv[1]
spec = importlib.util.spec_from_file_location("s", HERE / f"slides_{ver}.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
names = {}
for line in (HERE.parent.parent / "wiki" / "index.md").read_text(encoding="utf-8").splitlines():
    if line.startswith("| [concepts/"):
        path = line.split("](")[1].split(")")[0]; names[path] = line.split("|")[2].strip()
secs = []
for i, s in enumerate(m.SLIDES, 1):
    srcs = ",".join(s["src"])
    foot = " · ".join(f'<a href="../wiki/{p[:-3]}.html" target="_blank">{p.split("/")[-1][:-3]}</a>' for p in s["src"])
    ex = f'<div class="ex"><b>{s.get("ex_label","生活化例子")}</b>{s["ex"]}</div>' if s.get("ex") else ""
    tag = "h1" if i == 1 else "h2"
    secs.append(f'<section class="slide" data-sources="{srcs}"><div class="kicker">{s.get("kicker","")}</div><{tag}>{s["title"]}</{tag}><div class="body">{s["body"]}</div>{ex}<footer class="cite">本頁依據 Wiki：{foot}</footer></section>')
page = f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>agent-org 是什麼？</title><style>
:root{{--bg:#f7f5f0;--ink:#1d2430;--muted:#667085;--acc:#c2410c;--card:#fff;--line:#e3ded4}}
*{{box-sizing:border-box}}html,body{{margin:0;height:100%;background:var(--bg);color:var(--ink);font-family:"PingFang TC","Noto Sans TC",sans-serif}}
.slide{{display:none;position:absolute;inset:0;padding:56px max(24px,8vw) 70px;overflow:auto}}.slide.on{{display:block}}
.kicker{{color:var(--acc);font-weight:700;letter-spacing:.06em;font-size:15px}}h1{{font-size:clamp(34px,6vw,60px);margin:.2em 0 .3em}}h2{{font-size:clamp(26px,4vw,40px);margin:.2em 0 .6em}}
.body{{font-size:clamp(17px,2.1vw,23px);line-height:1.7;max-width:1000px}}.body li{{margin:.35em 0}}.body table{{border-collapse:collapse;font-size:.82em;background:var(--card)}}.body th,.body td{{border:1px solid var(--line);padding:6px 10px;text-align:left}}.body th{{background:#efe9df}}
.ex{{margin-top:22px;max-width:1000px;background:var(--card);border-left:5px solid var(--acc);padding:12px 16px;font-size:clamp(15px,1.8vw,19px);line-height:1.6}}.ex b{{display:block;color:var(--acc);font-size:.85em;margin-bottom:2px}}
.flow{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}.flow span{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 10px;font-size:.85em}}.flow span.g{{background:#fde8dc;border-color:var(--acc);color:var(--acc);font-weight:700}}
.cite{{position:absolute;left:max(24px,8vw);bottom:46px;font-size:13px;color:var(--muted)}}.cite a{{color:var(--muted)}}
#bar{{position:fixed;left:0;right:0;bottom:0;height:40px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font-size:13px;color:var(--muted);border-top:1px solid var(--line);background:var(--bg)}}
#bar button{{border:1px solid var(--line);background:var(--card);border-radius:6px;padding:4px 12px;font-size:14px;cursor:pointer}}
</style></head><body>
{''.join(secs)}
<div id="bar"><button id="prev" aria-label="上一張">← 上一張</button><span id="pos"></span><span>LLM Wiki × agent-org｜雲科 B11517038 資工 郭益閎</span><button id="next" aria-label="下一張">下一張 →</button></div>
<script>
const S=[...document.querySelectorAll('.slide')];let i=Math.max(0,Math.min(S.length-1,(parseInt(location.hash.slice(1))||1)-1));
function show(n){{i=Math.max(0,Math.min(S.length-1,n));S.forEach((s,k)=>s.classList.toggle('on',k===i));document.getElementById('pos').textContent=(i+1)+' / '+S.length;history.replaceState(null,'','#'+(i+1));}}
document.getElementById('prev').onclick=()=>show(i-1);document.getElementById('next').onclick=()=>show(i+1);
addEventListener('keydown',e=>{{if(['ArrowRight','PageDown',' '].includes(e.key))show(i+1);if(['ArrowLeft','PageUp'].includes(e.key))show(i-1);}});show(i);
</script></body></html>"""
(HERE.parent / "index.html").write_text(page, encoding="utf-8")
print(f"{ver}: {len(secs)} 張投影片寫入 slides/index.html")
