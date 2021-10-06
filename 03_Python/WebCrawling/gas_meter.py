# 가스 미터 현황 크롤링 후 엑셀 파일 저장

# 1. 패키지 install
# pip install requests
# pip install beutifulsoup4
# pip install openpyxl
# pip install selenium
import requests
from bs4 import BeautifulSoup
import openpyxl
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# 2. 내가 작업할 Workbook 생성하기 
wb = openpyxl.Workbook()

# 3. 작업할 Workbook 내 Sheet 활성화
sheet = wb.active

# 4. 데이터 프레임 내 header(변수명) 생성
sheet.append(["NO", "구분", "계량기종류", "형식승인번호", "상호명", "수량", "기물번호", "완료일", "규격"])

# 데이터 크롤링 과정
# for p in range(1, 1086, 1):
for p in range(1, 2):
    URL = f"http://metrology.ktc.re.kr/Ipt/InfoList?MrnrSeCode=AB001006&AthrzEndDe_Start=2011-01-01&AthrzEndDe_End=2020-12-31&InsttSn=undefined&EntrpsNm=undefined&page={p}"
    raw = requests.get(URL)
    html = BeautifulSoup(raw.text, "html.parser")

    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    
    driver.get(url=URL)

    container = html.select("table.list tbody tr")

    

    for c in container:
        # driver.implicitly_wait(5)
        temp = c.find_all("td")
        # a_tag.click()
        arr = []
        count = 0
        for t in temp:
            count += 1
            if count == 3:

            arr.append(t.text)
        sheet.append(arr)
    

# 작업 마친 후 파일 저장(파일명 저장시 확장자 - .xlsx 필수!)
wb.save("gas_meter_update.xlsx")