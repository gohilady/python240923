strA = "파이썬은 강력해" 
strB = "python is very powerful"
x= 100
y = 3.14

print(dir())
print(len(strA))
print(len(strB))

strC = """다중 라인을
저장하는 경우는
이렇게 처리
"""

print(strC)

#슬라이싱
print(strA[0])
print(strA[0:3])
print(strA[:3])
print(strA[-2:])
print(strA[-3:])

#리스트 
lst = ['red', 'blue', 'green']
print(len(lst))

lst.append('white')
print(lst)

lst.insert(1,'pink')
print(lst)

lst.remove('blue')
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)


# set 형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#tuple 형식
tp=(10,20,30)
print(len(tp))
#함수정의
def calc(a,b):
    return  a+b,a*b

#함수 호출
result = calc(3,4)
print(result)

print("id:%s, name:%s" % ('kim',"김유신"))

#형식 변환(Type Casting)
a = set((10,20,30))
print(a)
print(type(a))

b = list(a)
b.append(40)
print(b)

c = tuple(b)
print(c)
print(type(c))


