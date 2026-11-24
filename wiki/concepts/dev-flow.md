# 開發流程

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
