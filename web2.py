#web2.py
#웹서버에 페이지 실행 요청
import requests
#크롤링 라이브러리
from bs4 import BeautifulSoup

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
    #f-string 포맷팅(포멧스트링)
    print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")

f.close()













    # <div class="card-desc">
    #   <h2 class="card-title">아이폰 14 128GB</h2>
    #   <div class="card-price ">
    #     600,000원
    #   </div>
    #   <div class="card-region-name">
    #     전남 순천시 용당동
    #   </div>