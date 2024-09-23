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
