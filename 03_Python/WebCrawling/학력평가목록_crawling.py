# 서울특별시 교육청 학력평가 자료 목록 크롤링 후 엑셀 파일 저장

# 1. 패키지 install
# pip install requests
# pip install beutifulsoup4
# pip install openpyxl
import requests
from bs4 import BeautifulSoup
import openpyxl

# 2. 내가 작업할 Workbook 생성하기 
wb = openpyxl.Workbook()

# 3. 작업할 Workbook 내 Sheet 활성화
sheet = wb.active

# 4. 데이터 프레임 내 header(변수명) 생성
sheet.append(["번호", "학교", "학년", "연도", "월", "구분"])

# 데이터 크롤링 과정
for p in range(1, 111, 1):
    if p != 1:
        p = int(str(p-1) + "1")  # 1 11 21 31 ... 1091 이렇게 증가함
    raw = requests.get(f"https://www.sen.go.kr/web/services/bbs/bbsList.action?bbsBean.bbsCd=105&searchBean.searchKey=&appYn=&searchBean.searchVal=&searchBean.startDt=&startDt=&searchBean.endDt=&endDt=&ctgCd=&sex=&school=&grade=&year=&month=&schoolDiv=&establDiv=&hopearea=&searchBean.deptCd=&searchBean.currentPage={p}")
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("table.boardListSkin1 tbody tr")

    for c in container:
        temp = c.find_all("td")
        arr = []
        for t in temp:
            arr.append(t.text)
        sheet.append(arr)

    

# 작업 마친 후 파일 저장(파일명 저장시 확장자 - .xlsx 필수!)
wb.save("new_test.xlsx")