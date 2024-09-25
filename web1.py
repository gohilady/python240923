#web1.py
#크롤링 선언

from bs4 import BeautifulSoup

#html 파일 읽기
html = open('Chap09_test.html', 'r', encoding='utf-8')

#html 파일 객체를 파싱
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

# 문서에 있는 모든 <p> 태그를 찾아서 출력
#print(soup.find_all('p'))

# 첫번째 <p> 태그를 찾아서 출력
#print(soup.find('p'))

# 조건에 맞는 <p> 태그를 찾아서 출력
#<p class='outer-text'> 태그를 찾아서 출력

#print(soup.find_all('p', class_='outer-text'))
#최근에는 attrs속성을 사용하여 찾음
#print(soup.find_all('p', attrs={'class':'outer-text'}))

#<p>에서 id가 'first'인 태그를 찾아서 출력
print(soup.find(id='first'))

#찾은 결과를 루프
for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace('\n', '')
    title = title.replace('\t', '')
    title = title.replace('\r', '')
    title = title.replace('\f', '')
    print(title)


#<p>에서 class가 'outer-text'인 태그를 찾아서 출력
#print(soup.find_all(class_='outer-text'))

#<p>에서 id가 'first'인 태그를 찾아서 출력
#print(soup.find(id='first'))


