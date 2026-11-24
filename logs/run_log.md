# 執行與檢查紀錄

格式：時間｜Graph｜節點｜第幾次｜結果｜說明

| 時間 | Graph | 節點 | 次 | 結果 | 說明 |
|---|---|---|---|---|---|
| 13:28 | A | 取得資料 | 1 | 通過 | 9 個網址 HTTP 200；Demo07a 從 GitHub 抓 notebook |
| 13:30 | A | 取得資料 | 1 | 失敗 | react-paper 摘要選擇器抓不到內容（arXiv 頁面結構），raw 檔只剩專案頁 |
| 13:31 | A | 取得資料 | 2 | 失敗 | 改用 arXiv API 回傳空白 |
| 13:32 | A | 取得資料 | 3 | 通過 | 改讀 arXiv 頁面的 citation_abstract meta，補上摘要 |
| 13:40 | A | 討論 | 1 | 等待 | 5 篇提案已送出，等使用者回饋 |
| 13:30 | A | 主題變更 | — | — | 使用者改主題為 agent-org；外部 5 篇移到 raw_old_ai_agents/，改收本機 6 份資料 |
| 13:33 | A | 取得資料 | 1 | 通過 | 6 份：README、設計文件 artifact、ship skill、13 角色定義＋models.yml、11-17 審查計畫、Clawd 實際 run 紀錄 |
| 13:40 | A | 討論 | 1 | 等待 | 6 份提案已送出，等使用者回饋 |
| 13:41 | A | 討論 | 1 | 通過 | 使用者指示討論已在過去對話完成；子代理摘錄 48 則原話（raw/past-discussions.md），寫進 log.md 回饋表 |
| 13:46 | A | 寫入 | 1 | 完成 | 7 個來源頁、12 個概念頁、index.md |
| 13:46 | A | 檢查（lint） | 1 | 失敗 | 4 個錯誤，全是「表格段落沒有來源標記」：roles、dev-flow、tiers、case-clawd-heatmap |
| 13:48 | A | 修正 | 1 | — | 判斷是規則沒考慮表格：表格格子外無法加標記，來源寫在下一段。改 lint：表格可由緊接的下一段標來源；CLAUDE.md 同步寫明 |
| 13:48 | A | 檢查（lint） | 2 | 通過 | 19 頁、7 篇原文，0 錯誤 |
| 13:50 | B | 規劃大綱 | 1 | 完成 | 只讀 index.md，排 13 張（slides/build/outline_v1.md） |
| 13:48 | A | 檢查（獨立子代理核對內容） | 1 | 進行中 | 只讀 raw 與 concepts，逐段核對事實 → logs/check_wiki_v1.md |
| 13:48 | B | 查詢 Wiki ＋ 撰寫投影片 | 1 | 完成 | 每張只讀大綱指定的 concept 頁，13 張（slides/build/slides_v1.py） |
| 13:48 | B | 檢查（check_slides.py） | 1 | 通過 | 13 張、每張有來源、連結檔案都存在 |
| 13:49 | B | 檢查（獨立子代理核對陳述） | 1 | 進行中 | 只讀 src 指定的 wiki 頁 → logs/check_slides_v1.md |
| 13:49 | A | 檢查（獨立子代理核對內容） | 1 | 通過 | 67 段、0 段不被支持；3 項備註（來源標不全、一句轉述加了引號），見 logs/check_wiki_v1.md |
| 13:49 | B | 檢查（獨立子代理核對陳述） | 1 | 失敗 | 88 條陳述中 5 條有問題，3 條 BLOCK；另有約 17 個術語沒解釋，見 logs/check_slides_v1.md |
| 13:53 | A | 寫入（回補） | 2 | 完成 | 依 B 的失敗回頭改 Wiki：新增 concepts/glossary.md；review-and-bounce 與 case-clawd 對同一次 BLOCK 的說法統一；處理 A 的 3 項備註 |
| 13:53 | A | 檢查（lint） | 3 | 通過 | 20 頁、0 錯誤 |
| 13:52 | B | 規劃大綱＋查詢 Wiki（v2：改成論點清單） | 2 | 完成 | 14 張（新增第 2 張名詞小辭典）、58 個論點，每個論點附 Wiki 頁與原文錨點（slides/build/slides_v2.py） |
| 13:52 | B | 檢查（check_claims.py，v2 新增，移到撰寫之前） | 1 | 通過 | 58 個錨點都在指定頁、每張 src 等於論點用到的頁、術語都在名詞解釋之後才出現 |
| 13:53 | B | 撰寫投影片 | 2 | 完成 | 內容直接由論點清單產生（v1 備份在 slides/build/index_v1.html） |
| 13:53 | B | 檢查（check_slides.py） | 2 | 通過 | 14 張、0 錯誤 |
| 13:54 | B | 檢查（獨立子代理核對陳述） | 2 | 失敗 | 73 條陳述中 1 條有問題（第 13 張寫「回顧結束」，Wiki 只寫「13:39 回顧」）；術語問題 9 個，見 logs/check_slides_v2.md |
| 13:56 | B | 查詢 Wiki＋撰寫（v3 修正） | 3 | 完成 | 第 13 張照 Wiki 原文改寫；名詞小辭典補關卡、分級、模型、PM。diff、PR、回滾等一般軟體詞 Wiki 沒有定義，不補（記為限制） |
| 13:56 | B | 檢查（check_claims.py ＋ check_slides.py） | 2 | 通過 | 14 張、61 個論點、0 錯誤 |
| 13:57 | B | 檢查（獨立子代理複核改過的第 2、13 張） | 3 | 通過 | 15 條陳述、0 條有問題，見 logs/check_slides_v3.md |
| 13:58 | B | 發布 | 1 | 完成 | 重建 docs/，推上 GitHub Pages |
