# 主持人

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
