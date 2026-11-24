# agent-org 是什麼

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
