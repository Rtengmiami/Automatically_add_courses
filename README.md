# Python script for dynamically scraping course selection numbers and automatically adding courses with Line Notify notification
This Python file is designed to allow enthusiastic students to automatically add courses without being limited by luck and having to wait until the next academic year to take the course.
## How to Use
Using this program is very simple. First, make sure you have installed Python and Selenium. Then open this program and enter your personal information as prompted.

## The limitations of this program are:  
1.Only one course can be tracked at a time.  
2.The course does not conflict with your identity and can be added by yourself.

This program currently uses the National Taiwan University of Science and Technology's course inquiry and selection system as an example. It searches for courses based on course codes and filters them based on the current number of students enrolled and the maximum number of students allowed. When there is a vacancy in the course, it will notify you via Line. If you successfully add the course, you will also be notified via Line Notify.

## Other Notes
When using this program, please make sure that your behavior complies with relevant laws and regulations and does not cause excessive burden or interfere with the normal operation of the target website.  
*Ps. The version of Selenium used here is 4.8.0.*  
If you encounter any problems while using this program or have any suggestions for improvement, please feel free to contact the author of this program, Auston.

# Python 動態爬取選課人數及自動加選並以Line Notify通知
這個 Python 檔案是為了讓熱心學習的學生可以自動加簽課程，不必受限於運氣，而需要等待下一學年才可修習。
## 如何使用
此程式的使用方式非常簡單，只需要先確認已經安裝好 Python 環境及Selenium後，開啟此程式並依照使用者提示依序輸入個人資料。
該程式使用限制及為：  
1.一次限追蹤一門課程  
2.該課程與身份不衝突，可自行加簽

本程式目前以臺灣科技大學課程查詢及選課系統為範例，透過課程代碼，將課程搜尋結果固定，並根據目前選課人數及課程上限人數作為篩選條件，當有選課餘額時便以Line進行通知，若成功選到該課程，也會以Line Notify進行通知。

## 其他注意事項
在使用此程式時，請務必確認自己的使用行為符合相關法規，並且不要對目標網站造成過度負擔或干擾其正常運作。  
**Ps. 這裡使用的 Selenium 版本是 4.8.0。**  
如果你在使用此程式過程中遇到任何問題，或者有任何改進建議，歡迎隨時聯絡本程式的作者：Auston。
