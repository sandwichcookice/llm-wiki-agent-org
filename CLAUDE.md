# LLM Wiki：agent-org（把公司開發流程搬進 Claude Code 的多 Agent 組織）

這個資料夾是一個由 LLM（Claude Code）維護的知識庫，主題是使用者自己做的 Claude Code plugin「agent-org」。人負責挑資料與討論方向，LLM 負責寫頁面、維持連結與一致性。教學簡報只能用這裡的 Wiki 當知識來源。

## 資料夾

- `raw/`：原文，抓下來後不修改。每篇開頭有 id、title、origin（出處）、collected（收集時間）。
- `wiki/index.md`：所有頁面的目錄，每頁一行。
- `wiki/log.md`：每次 ingest 的紀錄：LLM 的提案、使用者回饋、寫了哪些頁。
- `wiki/sources/<id>.md`：一篇原文一頁摘要，檔名就是 raw 的 id。
- `wiki/concepts/<slug>.md`：概念頁，同一個概念只能有一頁，新資料用合併的方式更新。
- `slides/index.html`：由 Wiki 產生的教學簡報。
- `logs/run_log.md`：兩張 graph 每個節點的執行與檢查紀錄。

## 頁面格式

- 第一行 `# 標題`，第二段一句話定義。
- 每一段內容結尾都要有來源標記 `[來源: <id>]`，id 必須是 `raw/` 裡存在的檔名；多個來源用 `[來源: a, b]`。
- 頁面之間用相對連結，例如 `[Reflection](reflection.md)`、`[原文摘要](../sources/ng-agentic-patterns.md)`。
- 概念頁最後有「相關頁面」清單。
- 用繁體中文寫，英文專有名詞第一次出現時保留原文。

## Ingest 流程（先討論、後生成）

1. 取得原文，存到 `raw/`。
2. **討論**：先提出 3 到 5 個重點、要新增或更新的頁面、不確定的地方，交給使用者回饋。使用者回饋前不得寫入 wiki。
3. 寫入：依原文與回饋寫來源頁、新增或合併概念頁、更新 index，並在 log.md 記下提案與回饋原文。
4. 檢查：跑 `python3 scripts/lint_wiki.py`；再由另一個沒有參與寫作的子代理只讀原文與新頁面，判斷每段是否被原文支持。失敗就帶著錯誤回到步驟 3，最多重做 2 次。

## 查詢與產生簡報

- 回答問題或做簡報時，先讀 index.md，再只讀相關頁面，不用 Wiki 以外的知識補內容。
- 簡報每張投影片要列出它引用的 Wiki 頁面，投影片上的每個重點都要在引用頁找得到依據。

## Lint 規則（scripts/lint_wiki.py 會檢查）

- 所有內部連結指向存在的檔案。
- 每個內容段落都有 `[來源: id]`，且 id 存在於 raw/。表格無法在格子外加標記，所以表格的來源寫在緊接表格的下一段。
- index.md 列出所有 sources/ 與 concepts/ 頁面。
- 每篇 raw 原文都有對應的 sources/ 頁。
