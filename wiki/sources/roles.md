# 來源：13 個角色定義與 models.yml

agents/*.md 是每個子代理的指令，models.yml 決定每個角色用哪個模型。[來源: roles]

## 摘要

- 每個角色檔都寫明：看不到負責人的對話，只讀 brief 和它指定的文件；只能寫到 brief 指定的路徑。[來源: roles]
- 模型分配：PM、架構師、Code Reviewer、安全、知識管理員、監察人用 Opus 5.5；工程師、效能、維護者、QA 用 Sonnet 5.5；Release 用 Haiku 5.5；L 級架構師與升級處理用 Fable 5.2。[來源: roles]
- models.yml 註解寫明：換模型是組織的修改，要負責人同意；審查者和工程師要用不同模型。[來源: roles]

## 用在哪些頁

[角色與模型](../concepts/roles.md)。[來源: roles]
