#전역변수
strName = "Not Class Member"

#클래스 정의
class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #약간의 버그 - 전역변수 잘못 호출 / 수정완료
        print(self.strName)

#인스턴스 생성
d = DemoString()
#메서드 호출
d.set("First Message")
d.print()
