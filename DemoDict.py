#DemoDict.py

colors = {'apple':'red', 'banana':'yellow'}
print(len(colors))
#검색
print(colors['apple'])
#입력
colors['kiwi']='green'
print(colors)
#삭제
del colors['apple']
print(colors)

#반복문
for item in colors.items():
    print(item)

for k,v in colors.items():
    print(k,v)
