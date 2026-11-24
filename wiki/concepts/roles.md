# 角色與模型

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
