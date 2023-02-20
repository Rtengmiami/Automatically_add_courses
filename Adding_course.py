from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
#個人資訊填寫
Upper_limit= str(40) #Fill in the maximum number of participants. ex:40
code_in_school= "" #Fill in the course code ex:BA1234567
token = '' #個人須自行到網站複製 Individuals need to copy from the website themselves (https://notify-bot.line.me/my/)
account = "" #Account 
password = "."#Password 
message = ""
#webdriver新版本設定，視窗最大化以關閉個人列表  Set up the new version of WebDriver to maximize the window and close the personal list
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.set_page_load_timeout(86400)
search = 'https://querycourse.ntust.edu.tw/querycourse/#/'

#網站刷新 Refresh the website.
def web_refresh():
    try:
        driver.get(search)
        #代碼輸入 Code input
        course_code =driver.find_element(By.XPATH,'//*[@id="app"]/div[12]/main/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/input')
        course_code.click()
        course_code.send_keys(code_in_school)
        #搜尋按鈕 Search button
        search_buttom = driver.find_element(By.XPATH,'//button[@class="v-btn v-btn--block v-btn--round theme--light"]')
        search_buttom.click()
        #等待搜尋結果 Wait for search results
        condition = WebDriverWait(driver, 1,0.5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/div[13]/main/div/div/div/div/div[5]/div[1]/table/tbody/tr/td[8]/span[1]'))
            )
        condition =  (condition.text[0]+condition.text[1])
        driver.set_window_size(1300,100) #縮小視窗 Minimize the window.
        return(condition)
    except:
        driver.refresh()
        return(Upper_limit)

def notify_line():
    url_notify = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + token    # 設定權杖 Set up token
    }
    data = {
        'message':message     # 設定要發送的訊息 Set the message to be sent.
    }
    data = requests.post(url_notify, headers=headers, data=data) 

    
cond1= web_refresh()
#迴圈確認有無同學退選 Loop to check for any classmates who have dropped the course.
while cond1 ==Upper_limit:
    print("無法加選") 
    cond1= web_refresh()
    if cond1 <Upper_limit:
        break   

message= f"可以加簽囉，正在為您加選{code_in_school}" #通知加簽訊息 Notify the message for adding the course.
notify_line()

url_add = 'https://courseselection.ntust.edu.tw/'
driver.get(url_add)

driver.find_element(By.NAME,"UserName").send_keys(account)
driver.find_element(By.NAME,"Password").send_keys(password)
driver.find_element(By.ID,"btnLogIn").click()
WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/nav/div/div[2]/ul[1]/li[2]'))
        )

driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div[2]/ul[1]/li[2]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div[2]/ul[1]/li[2]/ul/li[1]/a").click()

driver.find_element(By.NAME,"CourseText").send_keys(code_in_school)
driver.find_element(By.ID,"SingleAdd").click()
time.sleep(1)
target = driver.find_elements(By.CLASS_NAME,"data")

#處理選到課程 Data of Course processing
target_list=[]
for t in target:
    target_list.append(t.text)
code_in_system = [i.split(" ",2)[0] for i in target_list]
name_in_system = [i.split(" ",2)[1] for i in target_list]

if code_in_school in  code_in_system:
    position = code_in_system.index(code_in_school)
    message = (f'{name_in_system[position]}Got')
    notify_line()
else:
    message = "QQ"
    notify_line()


time.sleep(2)
driver.quit()
