#funtion1.py

#함수의 정의
def setValue(newValue):
    #지역변수
    x= newValue
    print('지역변수:', x)

#함수 호출
    retValue = setValue(10)
    print(retValue)


#함수를 정의
def swap(x,y):
    return(y,x)

#호출
print(swap(3,4))

#교집합 문자 리턴
def intersect(prelist, postlist):
    #지역변수
    result = []

    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result
    
#호출
print(intersect('HAM','SPAM'))

#기본값을 명시
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))


#지역변수와 전역변수
x=5
def func1(a):
    return a+x

#호출
print(func1(1))

def func2(a):
    #지역변수
    x=1
    return a+x

#호출
print(func2(1))

