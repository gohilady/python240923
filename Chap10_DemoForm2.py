#Chap10_DemoForm2.py 
#Chap10_DemoForm2.ui(화면을 XML문서 저장) + Chap10_DemoForm2.py(로직 코딩) 
import sys 
#Qt패키지를 임포트 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹사이트에 페이지 실행을 요청
import urllib.request
from bs4 import BeautifulSoup
#웹서버에 페이지 실행 요청
import requests

#디자인 문서를 로딩
form_class = uic.loadUiType("c:\\work\\Chap10_DemoForm2.ui")[0]
#윈도우 클래스 정의(좀 더 기능이 많은 창 QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        url = 'https://www.daangn.com/fleamarket/'
        #웹서버에 페이지 실행 요청
        response = requests.get(url)
        #페이지 소스코드 추출
        soup = BeautifulSoup(response.text, 'html.parser')
        #찾은 결과를 루프
        f = open('daangn.txt', 'wt', encoding='utf-8')
        posts = soup.find_all('div', class_='card-desc')    
        for post in posts:
            titleElem = post.find('h2', class_='card-title')
            priceElem = post.find('div', class_='card-price')
            regionElem = post.find('div', class_='card-region-name')
            title = titleElem.text.strip()  
            price = priceElem.text.strip()
            region = regionElem.text.strip()
            print(f"{title}, {price}, {region}")
            f.write(f"{title}, {price}, {region}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼")
    def thirdClick(self):
        self.label.setText("세번째 버튼~~")

#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
