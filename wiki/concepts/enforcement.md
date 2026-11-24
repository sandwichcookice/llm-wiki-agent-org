# 規則由程式執行

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

每一節都寫明做不到的事：例如主持人如果刻意用 Bash 寫檔、或替負責人填答案，這裡擋不住；這套機制防的是忘記和走捷徑，不是蓄意造假。[來源: readme, design-doc]

關卡也只檢查文件在不在、審查是不是 PASS，擋不住「文件寫得好不好、審查者有沒有真的看」。[來源: design-doc]

## 相關頁面

- [主持人](orchestrator.md)
- [關卡與決策信](gates.md)
- [設計演進](design-evolution.md)
