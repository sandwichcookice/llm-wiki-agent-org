# 審查、退回與升級

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
