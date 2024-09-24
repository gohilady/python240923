#DemoDate.py

from datetime import *

d1 = date(2024,9,24)
print(d1)
d2 = date.today()
print(d2)

d3=datetime.now()
print(d3)

d4 = timedelta(days=100)
print("주문받고 100일후:", d2+d4)

#임의의 숫자를 생성
import random
print(random.random())
print(random.random())
print(random.uniform(2.0,5.0))
#리스트 컴프리헨션(리스트 내장)
print(random.randrange(20)for i in range(10))
print(random.randrange(20)for i in range(10))
print(random.sample(range(20),10))
print(random.sample(range(20),10))

#로또번호 생성
print(random.sample(range(1,46),5))


#파일명 다루기
from os.path import *
from os import *

#절대경로
print(abspath("python.exe"))
#상대경로
print(basename("c:\\work\\python.exe"))

fName = "c:\\python310\\python.exe"
if exists(fName):
    print("파일크기:",getsize(fName))
else:
    print("파일없음")

print('운영체제명:',name)
print("환경변수 목록:",environ)

#외부 실행파일 실행
#system("notepad.exe")


#파일 목록
import glob
print(glob.glob("c:\\work\\*.py"))

