# 名詞解釋

這頁只收原文用得到、初學者可能看不懂的詞，解釋都限定在 agent-org 裡的意思。[來源: design-doc, readme]

## 角色與組織

- **子代理**：每個職位是一個子代理；每次被叫起來都是全新的上下文，看不到負責人的對話。[來源: design-doc, roles]
- **主 session、主持人**：使用者自己開的那個 Claude Code 對話就是主持人，負責分級、派工、把關卡送到負責人面前。[來源: design-doc]
- **負責人**：設計文件稱為「你」，是產品負責人，只在關卡簽核。[來源: design-doc]
- **plugin**：角色和主持人做成 plugin，裝在使用者層級，所以任何專案都叫得起這個組織。[來源: design-doc]

## 文件

- **brief**：主持人派工時給子代理的文件，內容是角色指令、專案目標、角色常駐清單、這次的任務，再加上相關的教訓和範例。[來源: design-doc]
- **PRD**：PM 把負責人的需求寫成的文件，內容是問題、使用者、驗收條件。[來源: roles]
- **決策信**：主持人在關卡寫給負責人的信，負責人回覆後 org.py 才放行；一封只能回一次。[來源: readme, ship-skill]
- **教訓**：知識管理員把被擋下的原因整理成的規則，下次派工時放進 brief。[來源: design-doc]
- **episodes（事件）**：被擋、漏抓、負責人要求修改、退回升級、一次就通過，由 org.py 自動寫下的紀錄。[來源: design-doc]

## 程式與機制

- **run**：交給組織的一件任務，從分級（triage）開始，到完成（done）結束。[來源: ship-skill]
- **org.py**：記帳工具，負責認專案、組 brief、記事件、檢查階段推進、計算退回次數、處理決策信。[來源: readme]
- **hook**：plugin 掛在 Claude Code 上的自動檢查，例如每次使用工具前（PreToolUse）檢查權限與派工，子代理結束時（SubagentStop）記 token。[來源: readme]
- **worktree**：主持人用 git worktree 替每個工程師開的獨立資料夾，各自一個分支，互不干擾。[來源: ship-skill]
- **PASS／BLOCK／VETO**：審查檔第一行的結論；BLOCK 是阻擋，VETO 是安全審查的否決，只有負責人書面推翻才放行。[來源: readme, ship-skill]

## 模型

- **Fable、Opus、Sonnet、Haiku**：角色使用的四種 Claude 模型。依 models.yml 記的 API 定價，Fable 最貴、Opus 次之、Sonnet 再次、Haiku 最便宜，這份價目只拿來比相對成本。[來源: roles]

## 相關頁面

- [agent-org 是什麼](overview.md)
- [角色與模型](roles.md)
