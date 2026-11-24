# 來源：agent-org README（v0.1.28）

agent-org plugin 的使用說明，是對外的第一份文件。[來源: readme]

## 摘要

- 定位：把公司式的軟體開發流程搬進 Claude Code；PM、架構師、工程師、審查委員會、QA、Release 各是一個子代理，角色之間只靠文件交接，負責人只在三個關卡簽核，被擋下的地方累積成跨專案的組織記憶。[來源: readme]
- 指令有六個：`/agent-org:ship`（交任務給組織）、`status`、`audit`、`direct`、`setup`、`help`。[來源: readme]
- 大部分篇幅在說「規則怎麼由程式強制」：org.py 帳本、hook、決策信、執行鎖、token 預算、卡住的 run、教訓的回歸案例。[來源: readme]
- 每一節都寫明「做不到的」，例如這套機制防的是忘記和走捷徑，不是蓄意造假。[來源: readme]

## 用在哪些頁

[agent-org 是什麼](../concepts/overview.md)、[規則由程式執行](../concepts/enforcement.md)、[組織監察人](../concepts/auditor.md)。[來源: readme]
