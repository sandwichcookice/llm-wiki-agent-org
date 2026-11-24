import pathlib, sys
W = pathlib.Path(sys.argv[1]) / "wiki"
pages = {}
# ---------- sources ----------
pages["sources/readme.md"] = """# 來源：agent-org README（v0.1.28）

agent-org plugin 的使用說明，是對外的第一份文件。[來源: readme]

## 摘要

- 定位：把公司式的軟體開發流程搬進 Claude Code；PM、架構師、工程師、審查委員會、QA、Release 各是一個子代理，角色之間只靠文件交接，負責人只在三個關卡簽核，被擋下的地方累積成跨專案的組織記憶。[來源: readme]
- 指令有六個：`/agent-org:ship`（交任務給組織）、`status`、`audit`、`direct`、`setup`、`help`。[來源: readme]
- 大部分篇幅在說「規則怎麼由程式強制」：org.py 帳本、hook、決策信、執行鎖、token 預算、卡住的 run、教訓的回歸案例。[來源: readme]
- 每一節都寫明「做不到的」，例如這套機制防的是忘記和走捷徑，不是蓄意造假。[來源: readme]

## 用在哪些頁

[agent-org 是什麼](../concepts/overview.md)、[規則由程式執行](../concepts/enforcement.md)、[組織監察人](../concepts/auditor.md)。[來源: readme]
"""
pages["sources/design-doc.md"] = """# 來源：Agent 開發組織 設計文件

使用者在 claude.ai 上維護的設計頁（v0.1.28，2026-11-17），用圖說明整個組織。[來源: design-doc]

## 摘要

- 組織架構圖：負責人 → 主持人 → 產品、架構、開發、審查委員會、品質、維運六個部門；知識管理員和組織監察人不在派工線上。[來源: design-doc]
- 開發流程九個階段、三個橘色關卡，以及 S／M／L 三種分級各要跑哪些階段。[來源: design-doc]
- 組織記憶：記錄、提煉、讀取三個時間點，「每個角色從下游學」。[來源: design-doc]
- 版本演進：11/05 的設計做成 plugin，裝在 Mac、DGX Spark、Windows 三台機器，每台跑過全部測試（287 項）；之後參考 Paperclip 把規則改成程式強制。[來源: design-doc]

## 用在哪些頁

[開發流程](../concepts/dev-flow.md)、[分級](../concepts/tiers.md)、[組織記憶](../concepts/org-memory.md)、[設計演進](../concepts/design-evolution.md)。[來源: design-doc]
"""
pages["sources/ship-skill.md"] = """# 來源：主持人流程 /agent-org:ship

skills/ship/SKILL.md，主 session 變成「主持人」時照著做的完整步驟。[來源: ship-skill]

## 摘要

- 主持人分級、派工、記帳、在關卡問負責人；自己不寫程式、不審程式、不投票、不軟化結論。[來源: ship-skill]
- 每次派工：先用 org.py 組出知識 brief，再寫任務 brief，一個 Agent 呼叫做一件事，同一波的工作一起派出。[來源: ship-skill]
- 退回規則：⑥⑦ 任何 BLOCK／VETO／FAIL 退回 ⑤；第三次改派升級處理；安全否決不能被推翻成 PASS。[來源: ship-skill]

## 用在哪些頁

[主持人](../concepts/orchestrator.md)、[審查與退回](../concepts/review-and-bounce.md)、[關卡](../concepts/gates.md)。[來源: ship-skill]
"""
pages["sources/roles.md"] = """# 來源：13 個角色定義與 models.yml

agents/*.md 是每個子代理的指令，models.yml 決定每個角色用哪個模型。[來源: roles]

## 摘要

- 每個角色檔都寫明：看不到負責人的對話，只讀 brief 和它指定的文件；只能寫到 brief 指定的路徑。[來源: roles]
- 模型分配：PM、架構師、Code Reviewer、安全、知識管理員、監察人用 Opus 5.5；工程師、效能、維護者、QA 用 Sonnet 5.5；Release 用 Haiku 5.5；L 級架構師與升級處理用 Fable 5.2。[來源: roles]
- models.yml 註解寫明：換模型是組織的修改，要負責人同意；審查者和工程師要用不同模型。[來源: roles]

## 用在哪些頁

[角色與模型](../concepts/roles.md)。[來源: roles]
"""
pages["sources/review-plan-1117.md"] = """# 來源：11-17 最終審查與補回原設計的計畫

使用者 2026-11-17 在 Claude Code 計畫模式中批准過的計畫檔，記錄「設計和實作哪裡對不上、要怎麼補」。[來源: review-plan-1117]

## 摘要

- 使用者逐項回覆七件事，其中兩件他記得同意過、實作卻漏做或改掉：「等待時先做別的事」和「教訓的固定門檻」。計畫承認這是實作者自己改的，要照原門檻做回來。[來源: review-plan-1117]
- 「CI 必須全綠」原本只是寫給 Code Reviewer 的一句指示，沒有程式去讀 CI 結果，計畫把它排進補做清單。[來源: review-plan-1117]
- 另外設計 Slack 通報、把影子試跑加回模型更新流程、三台機器實機測試、用組織重做 Clawd。[來源: review-plan-1117]
- 這是計畫，不是完成報告；哪些項目已經做完要看 README 和設計文件。[來源: review-plan-1117]

## 用在哪些頁

[設計演進](../concepts/design-evolution.md)。[來源: review-plan-1117]
"""
pages["sources/clawd-run.md"] = """# 來源：實際 run 紀錄：Clawd 每日用量熱力圖

~/agent-org 裡 run 20261110-2158-usage-heatmap 的狀態、審查結論、關卡決策信、回顧與教訓，是 agent-org 第一次完整跑完的 run。[來源: clawd-run]

## 摘要

- L 級，專案第一個 run；2026-11-10 21:58 開始，11-11 13:39 結束。[來源: clawd-run]
- 設計被維護者 BLOCK 一次，第二輪三位設計審查都 PASS；Code Review、QA 都一次通過；關卡 C 合併。[來源: clawd-run]
- 回顧產生 L-0001～L-0004 四條教訓，並指出「逐項 BLOCK 不會被自動記成事件」的記錄缺口。[來源: clawd-run]

## 用在哪些頁

[實例：Clawd 熱力圖](../concepts/case-clawd-heatmap.md)、[審查與退回](../concepts/review-and-bounce.md)、[組織記憶](../concepts/org-memory.md)。[來源: clawd-run]
"""
pages["sources/past-discussions.md"] = """# 來源：使用者過去設計 agent-org 的討論紀錄

從 2026-11-05～11-17 的 Claude Code 對話中，只摘錄使用者自己說過的話，共 48 則，依 6 份資料分類，是這個 Wiki「先討論、後生成」的討論依據。[來源: past-discussions]

## 摘要

- 起點：使用者看完投票式的 court skill 後問「為什麼我們不設計成正常公司的架構呢?」，agent-org 從這裡開始。[來源: past-discussions]
- 記憶：他要「持久化的…像是RAG或是LLM wiki那種」，記下「哪些地方被擋下來過」，而且每個角色都有自己的知識、跨專案共用。[來源: past-discussions]
- 規則：他問「要怎麼確保…他就會依照我們的架構運行」，之後從 Paperclip 的建議清單先選「關卡強制」。[來源: past-discussions]
- 每則都標明是打字、點選選項，還是在選擇題裡自己打字；推測的部分另列一節，Wiki 不把推測寫成事實。[來源: past-discussions]

## 用在哪些頁

幾乎每個概念頁的「為什麼這樣設計」都引用這份。[來源: past-discussions]
"""
# ---------- concepts ----------
pages["concepts/overview.md"] = """# agent-org 是什麼

agent-org 是一個 Claude Code plugin，把公司的軟體開發流程搬進 Claude Code：每個職位是一個子代理，角色之間只靠文件交接，負責人只在三個關卡簽核。[來源: readme, design-doc]

## 為什麼要做

使用者原本在試一個投票式的 court skill，看完後問「為什麼我們不設計成正常公司的架構呢?」，決定改照一般公司的開發流程來設計。[來源: past-discussions]

他也要求這個組織是持久化的，「像是RAG或是LLM wiki那種」，把哪些地方被擋下來過記住，讓下次不再犯。[來源: past-discussions]

## 三個核心想法

1. **分工**：PM 寫需求、架構師做設計、工程師實作、審查委員會與 QA 檢查、Release 發版，主持人只負責派工與記帳。[來源: design-doc, readme]
2. **人只在關鍵點出手**：負責人只在關卡 A、B、C 簽核，其他步驟由主持人推進。[來源: design-doc]
3. **規則由程式執行**：org.py 帳本和 hook 擋住缺文件、審查沒過就往下走的情況，不靠模型記得。[來源: readme]

## 組織不屬於任何專案

角色和主持人做成 plugin 裝在使用者層級，記憶放在 ~/agent-org/，每個專案只是它接的一個案子。[來源: design-doc]

這是使用者的要求：「我在每個專案就都會使用這個組織來完成 不是安插在某個專案內部的持久化」。[來源: past-discussions]

## 相關頁面

- [角色與模型](roles.md)
- [開發流程](dev-flow.md)
- [組織記憶](org-memory.md)
- [規則由程式執行](enforcement.md)
"""
pages["concepts/roles.md"] = """# 角色與模型

agent-org 有 13 個角色定義，每個都是一個子代理，看不到負責人的對話，只讀主持人給的 brief 和文件。[來源: roles, design-doc]

## 角色表

| 角色 | 做什麼 | 模型 |
|---|---|---|
| PM | 把需求寫成 PRD：問題、使用者、可測試的驗收條件 | Opus 5.5 |
| 架構師／架構師 L | 設計文件、ADR、拆任務；L 級改派 architect-l | Opus 5.5／Fable 5.2 |
| 工程師 ×N | 在各自的 git worktree 實作一個任務，附測試 | Sonnet 5.5 |
| Code Reviewer | 看 diff 與設計，回 PASS 或 BLOCK | Opus 5.5 |
| 安全 | 設計與程式審查，可以否決（VETO） | Opus 5.5 |
| 效能、維護者 | L 級設計審查 | Sonnet 5.5 |
| QA | 依 PRD 驗收條件寫測試、跑測試 | Sonnet 5.5 |
| Release | 發佈清單與回滾方案 | Haiku 5.5 |
| 知識管理員 | 回顧時把被擋的原因寫成教訓 | Opus 5.5 |
| 升級處理 | 同一關第三次退回時重做 | Fable 5.2 |
| 組織監察人 | 不屬於任何專案，提改進組織的建議 | Opus 5.5 |

上表的模型取自 models.yml。[來源: roles]

## 為什麼審查者和工程師用不同模型

設計文件說，這是為了降低「同一個模型自己說自己好」的問題。[來源: design-doc]

這一條是 Claude 在監察人設計中列進「底線」清單的，使用者回「5 可以」表示同意；紀錄裡沒有他自己提出這句話。[來源: past-discussions]

## 每個角色都有自己的知識

使用者在設計初期就決定，記憶不是只給工程師和 Reviewer，而是每個角色都有。[來源: past-discussions]

## 寫程式的習慣

使用者指出 AI 喜歡把不可能發生的情況寫成測試、把只用一次的程式抽成函式，要求工程師和 QA 不要這樣做；Code Reviewer 看到「寫錯」和「冗餘」都算阻擋。[來源: past-discussions]

## 相關頁面

- [主持人](orchestrator.md)
- [審查與退回](review-and-bounce.md)
- [組織監察人](auditor.md)
"""
pages["concepts/orchestrator.md"] = """# 主持人

主持人就是使用者開的那個主 session，執行 /agent-org:ship 後負責分級、派工、記帳，並在關卡把問題送到負責人面前。[來源: ship-skill, design-doc]

## 不做的事

主持人不寫程式、不審程式、不投票、也不軟化任何審查結論；在 org 模式開著的專案裡，hook 會擋掉它自己改專案檔案。[來源: ship-skill]

## 怎麼派工

1. 用 org.py 組出這個角色的知識 brief：專案目標、角色常駐清單、相關教訓。
2. 再寫任務 brief：要讀哪些檔、做什麼、不做什麼、輸出寫到哪裡。
3. 一個 Agent 呼叫做一件事，prompt 只有一句「讀這份 brief 並照做」；同一波的工作一起派出。[來源: ship-skill]

子代理每次被叫起來都是全新的上下文，主持人不轉述對話，只給文件路徑。[來源: design-doc]

## 使用者對主持人的要求

- 「有遇到執行問題請問我 不要自己猜測」。[來源: past-discussions]
- 專案目標由主持人改寫成草稿，負責人確認後才採納。[來源: past-discussions]
- 主持人可以讀專案的 CLAUDE.md，自己決定哪些部分放進 brief，因為角色本身看不到它。[來源: past-discussions]

## 相關頁面

- [開發流程](dev-flow.md)
- [關卡與決策信](gates.md)
- [規則由程式執行](enforcement.md)
"""
pages["concepts/dev-flow.md"] = """# 開發流程

一個 L 級的任務會從分級走到回顧，共九個階段、三個關卡；每個階段留下一份文件，下一個階段就讀那份文件。[來源: design-doc]

## 九個階段

| # | 階段 | 誰做 | 留下的文件 |
|---|---|---|---|
| ① | 需求 | PM | prd.md |
| ② | 技術設計 | 架構師 | design.md |
| ③ | 設計審查 | 安全、效能、維護者，平行 | reviews/design-review-*.md |
| ④ | 拆解 | 架構師 | tasks/01…N.md |
| ⑤ | 實作 | 工程師 ×N，各自 worktree | reports/implement-*.md |
| ⑥ | Code Review | Reviewer＋安全＋自動教訓檢查 | reviews/code-review-*.md |
| ⑦ | 測試 | QA | reviews/test-qa.md |
| ⑧ | 發佈 | Release | release.md |
| ⑨ | 回顧 | 知識管理員 | retro.md、knowledge/ |

關卡 A 在 ① 之後、B 在 ③ 之後、C 在 ⑦ 之後。[來源: design-doc]

## 文件交接

所有文件都放在這個 run 的資料夾，不放進專案 repo；主持人推進到下一格前，org.py 會先檢查文件在不在、審查是不是 PASS。[來源: design-doc, ship-skill]

## 回饋線

回顧把這次被擋的地方寫進知識庫，下一次派工時主持人把相關教訓放進 brief，流程因此形成一個跨 run 的迴圈。[來源: design-doc]

## 相關頁面

- [分級](tiers.md)
- [關卡與決策信](gates.md)
- [審查與退回](review-and-bounce.md)
- [組織記憶](org-memory.md)
"""
pages["concepts/tiers.md"] = """# 分級：S／M／L

主持人第一步先判斷改動大小，決定要跑哪些階段，因為「公司也不會為了改一個錯字寫設計文件」。[來源: design-doc]

## 三種分級

| 分級 | 什麼情況 | 跑哪些 | 關卡 | 子代理數 |
|---|---|---|---|---|
| S 小改 | 改字、小 bug、單一檔案 | 主持人寫任務 → 實作 → Code Review → 主持人跑測試 | C | 約 2 |
| M 一般功能 | 單一功能、不動 API 與資料模型 | 一段話需求 → 簡版設計 → 拆解 → 實作 → 審查 → QA → 發佈清單 | B、C | 約 5 |
| L 大型或高風險 | 新模組、API 或資料模型變更、新依賴、安全相關 | 全部九個階段 | A、B、C | 10 個以上 |

[來源: design-doc]

## 拿不準時

分級拿不準時往大的那一級算；一個專案的第一個 run 不會是 S。[來源: design-doc]

S、M 級只有被退回過才做回顧；M 級若 QA 抓到漏網的問題也要回顧；L 級每次都做。[來源: design-doc, ship-skill]

## 相關頁面

- [開發流程](dev-flow.md)
- [實例：Clawd 熱力圖](case-clawd-heatmap.md)
"""
pages["concepts/gates.md"] = """# 關卡與決策信

關卡是負責人唯一要出手的地方：A 問「值得做嗎」、B 選定設計方案、C 決定怎麼落地。[來源: design-doc]

## 決策信

主持人到關卡時先寫一封決策信（要你決定什麼、選項、建議），再問負責人；org.py 要看到「已回覆、結果是繼續」的決策信，才讓 run 離開關卡。[來源: readme, ship-skill]

決策信一封只能回一次；可逆的信過了期限才能照建議做，不可逆的信永遠不會逾時自動照做。[來源: readme]

## 為什麼要有決策信

使用者在設計初期指出：「在通知 我拍版 的這些地方 並沒有明確的設計 怎麼通知 使用什麼 怎麼問我」，決策信就是回應這個問題的設計。[來源: past-discussions]

## 關卡 C 不只是合併

使用者後來決定：「關卡C增加PR選項 和細部實作選項…不局限於只能合併回main」，所以關卡 C 是選「怎麼落地」，不是單純按合併。[來源: past-discussions]

使用者也選定關卡 C 的決策信一律不可逆，不能逾時照建議合併。[來源: past-discussions]

## 相關頁面

- [主持人](orchestrator.md)
- [開發流程](dev-flow.md)
- [規則由程式執行](enforcement.md)
"""
pages["concepts/review-and-bounce.md"] = """# 審查、退回與升級

審查者彼此看不到對方的結論，各自只回「通過」或「阻擋」；沒通過就退回上一步修改，不會往下走。[來源: design-doc]

## 退回規則

- 設計審查（③）有 BLOCK，退回設計（②）。
- Code Review（⑥）或測試（⑦）有 BLOCK、VETO、FAIL，退回實作（⑤）。
- 退回會把那一格之後的文件和關卡回覆全部作廢，每一格都要重做。[來源: ship-skill]

## 第三次退回就升級

同一關退回兩次還沒過，第三次改由升級處理（Fable 5.2）重做一次；還是不過才交給負責人決定，避免 agent 互相繞圈。[來源: design-doc, ship-skill]

## 安全否決不能被抵銷

安全審查的 VETO 不能被其他人的 PASS 抵銷，也不能被改寫成 PASS；負責人要推翻，必須留下書面理由的決策信。[來源: ship-skill]

## 實例

Clawd 熱力圖那次 run，設計第一輪被維護者 BLOCK：兩個平行任務要改同一個檔尾、帳本格式沒有演進規則。第二輪設計修好後三位審查都 PASS。[來源: clawd-run]

## 相關頁面

- [開發流程](dev-flow.md)
- [組織記憶](org-memory.md)
- [實例：Clawd 熱力圖](case-clawd-heatmap.md)
"""
pages["concepts/org-memory.md"] = """# 組織記憶與教訓

組織記憶屬於組織，不屬於任何專案，放在 ~/agent-org/；每個角色都有一份常駐清單，加上派工時按需取出的教訓。[來源: design-doc]

## 三個時間點

1. **記錄**：審查擋下、測試抓到漏的、負責人在關卡說「改」，org.py 自動寫進 episodes。
2. **提煉**：回顧時知識管理員讀事件，合併重複、附上證據，寫成教訓。
3. **讀取**：派工時 org.py 依角色、專案、技術棧、路徑篩出相關教訓放進 brief。[來源: design-doc, readme]

少了讀取這一步，它就只是一個沒人看的資料夾。[來源: design-doc]

## 每個角色從下游學

被擋下的一方記一條「不能這樣做」；如果審查者放行、問題卻在更下游才被發現，審查者也要記一條「這種東西我漏過」。[來源: design-doc]

## 為什麼這樣設計

使用者一開始就說要記住「哪些地方被擋下來過 不能怎麼寫 怎麼寫會有問題」，而且「參與開發的每個角色 應該都要有自己的knowledge」。[來源: past-discussions]

## 教訓會冷藏、升級、自動化

- 冷藏：教訓連續 10 次在範圍內卻沒放進 brief，就當冷藏不再放。
- 升級：要升到跨專案層，證據要來自兩個以上專案，或有負責人同意的決策信。
- 自動化：附上壞案例和好案例，驗證檢查真的抓得到，才改由程式在 Code Review 時自動跑。[來源: readme]

## 實例

Clawd 熱力圖的回顧寫了 L-0001～L-0004 四條教訓，例如「要讓 task 平行，共用的東西全部放進最先、單獨做的那個 task」。[來源: clawd-run]

## 相關頁面

- [審查與退回](review-and-bounce.md)
- [實例：Clawd 熱力圖](case-clawd-heatmap.md)
- [規則由程式執行](enforcement.md)
"""
pages["concepts/enforcement.md"] = """# 規則由程式執行

agent-org 把會影響結果的規則從「寫在說明裡」改成「由程式擋住」：scripts/org.py 是帳本，hooks 在工具呼叫前後檢查。[來源: readme, design-doc]

## 起因

使用者在設計第一天就問：「我們要怎麼確保 我在使用claude code 時 他就會依照我們的架構運行」。後來參考 Paperclip 列出建議清單，他第一個選「先做 1 關卡強制」。[來源: past-discussions]

## 擋住哪些事

- 階段推進：文件不在、審查第一行不是 PASS、關卡沒放行，org.py 不讓 run 往下走。
- 權限：審查檔只有該角色能寫，實作報告只有工程師能寫，主 session 不能代寫。
- 帳本：state.json、用量、決策只能透過 org.py 改，編輯工具直接改會被擋。
- 執行鎖：同一個 run 同時只能有一個 session 推進。
- token 預算：用滿就停止派工。[來源: readme]

## 擋不住的

每一節都寫明做不到的事：例如主持人如果刻意用 Bash 寫檔、或替負責人填答案，這裡擋不住；這套機制防的是忘記和走捷徑，不是蓄意造假。[來源: readme]

關卡也只檢查文件在不在、審查是不是 PASS，擋不住「文件寫得好不好、審查者有沒有真的看」。[來源: design-doc]

## 相關頁面

- [主持人](orchestrator.md)
- [關卡與決策信](gates.md)
- [設計演進](design-evolution.md)
"""
pages["concepts/auditor.md"] = """# 組織監察人

組織監察人不屬於任何專案，也不在任何 run 裡，專門看「這個組織本身運作得好不好」，只能提建議，不能改任何東西。[來源: readme, design-doc]

## 由來

使用者提出：「我需要多一個組織負責人（類似股東） 獨立於整個專案 專門看整個組織架構有無問題的 你先設計給我看 我確認沒問題才加入」。[來源: past-discussions]

## 建議要過三道關

1. 提出時：至少引用一個指標，數字要和指標檔一致，至少根據 5 個 run 或事件。
2. 負責人決定時：每個建議一封不會逾時的決策信。
3. 改完之後：接下來兩次監察比較指標，往預期方向走才保留，否則下一次第一個建議必須是改回來。[來源: readme]

## 底線

監察人的建議不能削弱幾條底線，例如合併前一定經過關卡 C、安全否決不能被抵銷、寫的人不審自己的東西。[來源: readme]

## 相關頁面

- [規則由程式執行](enforcement.md)
- [角色與模型](roles.md)
"""
pages["concepts/case-clawd-heatmap.md"] = """# 實例：用 agent-org 做 Clawd 每日用量熱力圖

這是 agent-org 第一次完整跑完的 run（L 級），需求是使用者的原話：「我需要一個 熱力圖之類的東西 就是我有辦法看到我每天的用量」。[來源: clawd-run, past-discussions]

## 時間線

| 時間 | 階段 | 結果 |
|---|---|---|
| 11-10 21:58 | 分級 | L：新增每日用量保存（資料結構變更），專案第一個 run |
| 22:30 | 關卡 A | 做 |
| 22:43 | 設計 | 三個待選決定 |
| 22:52 | 設計審查 | 退回 1 次 |
| 11-11 02:23 | 設計重審 | 三位都 PASS |
| 02:27 | 關卡 B | 選定方案 |
| 02:46 | 拆任務 | ADR 0001 與 4 個 task |
| 04:02 | 實作 | 四個 task 完成，check.sh 86 項通過 |
| 04:20 | Code Review | Reviewer、安全都 PASS |
| 04:48 | 測試 | QA PASS |
| 06:46 | 關卡 C | 合併 |
| 13:39 | 回顧 | 3 條教訓升到通用層 |

[來源: clawd-run]

## 負責人在關卡的回覆

使用者在 PRD 釐清時選了「token 數」「一年」「另開一個視窗」「從上線那天起累積」；三個關卡都選了建議選項。[來源: past-discussions, clawd-run]

## 學到什麼

- 唯一的退回來自維護者：拆工有循環依賴、帳本格式沒有演進規則。
- 回顧寫成三條架構師教訓，經負責人同意升到通用層。
- 回顧也指出記錄缺口：審查第一行是 PASS、逐項表裡卻有 BLOCK 的情況，不會被自動記成事件。[來源: clawd-run]

## 相關頁面

- [開發流程](dev-flow.md)
- [審查與退回](review-and-bounce.md)
- [組織記憶](org-memory.md)
"""
pages["concepts/design-evolution.md"] = """# 設計演進

agent-org 在 11/05 設計、做成 plugin 後，持續把規則從說明改成程式強制，到 11/17 發出 v0.1.28。[來源: design-doc]

## 主要階段

- 11/05：從 court skill 轉向「正常公司的開發流程」，定下分工、關卡、持久化記憶。[來源: past-discussions]
- 之後：參考 Paperclip，把關卡、token 預算、跨機器執行鎖、教訓回歸案例、卡住的 run、專案目標改成程式強制，並新增組織監察人。[來源: design-doc]
- 11/10～11：第一次完整 run（Clawd 熱力圖），之後的審查找出 16 個高風險缺口並修補。[來源: design-doc]
- 11/16：盲點搜查找出的項目，在 0.1.28（11/17）補上。[來源: design-doc]

## 設計和實作的落差

11-17 的計畫檔承認，有兩條使用者同意過的設計在實作時被漏做或改掉：「等待時先做別的事」與「教訓的固定門檻」，計畫要照原設計做回來。[來源: review-plan-1117]

使用者對這類落差的態度很一致：「全部都要做 因為那是原先設計目標」。[來源: past-discussions]

## 相關頁面

- [規則由程式執行](enforcement.md)
- [組織記憶](org-memory.md)
"""
pages["index.md"] = """# Wiki 目錄：agent-org

主題：使用者自己做的 Claude Code plugin「agent-org」。先讀「agent-org 是什麼」，再依需要往下讀。

## 概念頁

| 頁面 | 一句話 |
|---|---|
| [concepts/overview.md](concepts/overview.md) | agent-org 是什麼、為什麼做 |
| [concepts/roles.md](concepts/roles.md) | 13 個角色與模型分配 |
| [concepts/orchestrator.md](concepts/orchestrator.md) | 主持人：分級、派工、記帳，不寫程式 |
| [concepts/dev-flow.md](concepts/dev-flow.md) | 九個階段與文件交接 |
| [concepts/tiers.md](concepts/tiers.md) | S／M／L 分級 |
| [concepts/gates.md](concepts/gates.md) | 關卡 A／B／C 與決策信 |
| [concepts/review-and-bounce.md](concepts/review-and-bounce.md) | 審查、退回、第三次升級 |
| [concepts/org-memory.md](concepts/org-memory.md) | 組織記憶與教訓 |
| [concepts/enforcement.md](concepts/enforcement.md) | 規則由程式執行，以及擋不住的 |
| [concepts/auditor.md](concepts/auditor.md) | 組織監察人 |
| [concepts/case-clawd-heatmap.md](concepts/case-clawd-heatmap.md) | 實例：Clawd 熱力圖 run |
| [concepts/design-evolution.md](concepts/design-evolution.md) | 設計演進與落差 |

## 來源頁

| 頁面 | 原文 |
|---|---|
| [sources/readme.md](sources/readme.md) | agent-org README |
| [sources/design-doc.md](sources/design-doc.md) | 設計文件 |
| [sources/ship-skill.md](sources/ship-skill.md) | 主持人流程 |
| [sources/roles.md](sources/roles.md) | 13 個角色定義與 models.yml |
| [sources/review-plan-1117.md](sources/review-plan-1117.md) | 11-17 審查計畫 |
| [sources/clawd-run.md](sources/clawd-run.md) | Clawd 熱力圖 run 紀錄 |
| [sources/past-discussions.md](sources/past-discussions.md) | 使用者過去的討論紀錄 |

## 其他

- [log.md](log.md)：討論提案、使用者回饋、寫入與檢查紀錄
"""
for rel, text in pages.items():
    p = W / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(text, encoding="utf-8")
print(len(pages), "頁寫入")
