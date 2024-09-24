#DemoStr.py

strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(strB.capitalize())
print(strB.count("p"))
print("MBC2580".isalnum())
print("2580".isdecimal())

#문자열 가공
data  = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)

result=result.replace("spam", "spam egg")
lst = result.split()
print(lst)
print(":)".join(lst))


#정규표현식
import re

result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

#단어검색
result = re.search("apple","this is apple")
print(result.group())

result = re.search("\d{4}","올해는 2024년입니다")
print(result.group())

result = re.search("\d{5}","우리동네는 52100입니다.")
print(result.group())


