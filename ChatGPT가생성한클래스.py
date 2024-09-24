# Person 클래스 정의
class Person:
    """
    Person 클래스는 사람을 표현하는 기본 클래스입니다.
    멤버 변수:
        id: 사람의 고유 번호
        name: 사람의 이름
    메서드:
        printInfo(): 사람의 정보를 출력합니다.
    """
    def __init__(self, id, name):
        """
        Person 클래스의 생성자입니다.
        
        매개변수:
            id (int): 사람의 고유 번호
            name (str): 사람의 이름
        """
        self.id = id
        self.name = name

    def printInfo(self):
        """
        사람의 id와 name을 출력하는 메서드입니다.
        
        예시 출력: ID: 1, Name: Alice
        """
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 정의 (Person 클래스를 상속)
class Manager(Person):
    """
    Manager 클래스는 Person 클래스를 상속받아 관리자를 표현합니다.
    멤버 변수:
        id: 사람의 고유 번호 (상속받음)
        name: 사람의 이름 (상속받음)
        title: 관리자의 직책 (예: "프로젝트 관리자")
    메서드:
        printInfo(): 사람의 정보와 직책을 출력합니다.
    """
    def __init__(self, id, name, title):
        """
        Manager 클래스의 생성자입니다.
        
        매개변수:
            id (int): 사람의 고유 번호
            name (str): 사람의 이름
            title (str): 관리자의 직책
        """
        # Person 클래스의 생성자를 호출하여 id와 name을 초기화
        super().__init__(id, name)
        # title 변수 초기화
        self.title = title

    def printInfo(self):
        """
        사람의 id, name과 함께 title을 출력하는 메서드입니다.
        
        예시 출력: ID: 2, Name: Bob, Title: Project Manager
        """
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

# Employee 클래스 정의 (Person 클래스를 상속)
class Employee(Person):
    """
    Employee 클래스는 Person 클래스를 상속받아 직원을 표현합니다.
    멤버 변수:
        id: 사람의 고유 번호 (상속받음)
        name: 사람의 이름 (상속받음)
        skill: 직원의 기술 (예: "파이썬 개발자")
    메서드:
        printInfo(): 사람의 정보와 기술을 출력합니다.
    """
    def __init__(self, id, name, skill):
        """
        Employee 클래스의 생성자입니다.
        
        매개변수:
            id (int): 사람의 고유 번호
            name (str): 사람의 이름
            skill (str): 직원의 기술
        """
        # Person 클래스의 생성자를 호출하여 id와 name을 초기화
        super().__init__(id, name)
        # skill 변수 초기화
        self.skill = skill

    def printInfo(self):
        """
        사람의 id, name과 함께 skill을 출력하는 메서드입니다.
        
        예시 출력: ID: 3, Name: Charlie, Skill: Python Developer
        """
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 테스트 함수 정의
def test():
    """
    Person, Manager, Employee 클래스의 동작을 테스트하는 함수입니다.
    다양한 테스트 케이스를 통해 클래스들이 의도한 대로 동작하는지 확인합니다.
    """
    # 테스트 1: Person 객체 생성 및 출력
    p1 = Person(1, "Alice")
    p1.printInfo()  # 예상 출력: ID: 1, Name: Alice

    # 테스트 2: Manager 객체 생성 및 출력
    m1 = Manager(2, "Bob", "Project Manager")
    m1.printInfo()  # 예상 출력: ID: 2, Name: Bob, Title: Project Manager

    # 테스트 3: Employee 객체 생성 및 출력
    e1 = Employee(3, "Charlie", "Python Developer")
    e1.printInfo()  # 예상 출력: ID: 3, Name: Charlie, Skill: Python Developer

    # 테스트 4: 여러 Person 객체 생성 및 출력
    p2 = Person(4, "David")
    p3 = Person(5, "Eve")
    p2.printInfo()  # 예상 출력: ID: 4, Name: David
    p3.printInfo()  # 예상 출력: ID: 5, Name: Eve

    # 테스트 5: 여러 Manager 객체 생성 및 출력
    m2 = Manager(6, "Frank", "HR Manager")
    m3 = Manager(7, "Grace", "Sales Manager")
    m2.printInfo()  # 예상 출력: ID: 6, Name: Frank, Title: HR Manager
    m3.printInfo()  # 예상 출력: ID: 7, Name: Grace, Title: Sales Manager

    # 테스트 6: 여러 Employee 객체 생성 및 출력
    e2 = Employee(8, "Heidi", "Java Developer")
    e3 = Employee(9, "Ivan", "DevOps Engineer")
    e2.printInfo()  # 예상 출력: ID: 8, Name: Heidi, Skill: Java Developer
    e3.printInfo()  # 예상 출력: ID: 9, Name: Ivan, Skill: DevOps Engineer

    # 테스트 7: Manager 객체의 title 변경 후 출력
    m1.title = "Senior Project Manager"
    m1.printInfo()  # 예상 출력: ID: 2, Name: Bob, Title: Senior Project Manager

    # 테스트 8: Employee 객체의 skill 변경 후 출력
    e1.skill = "Data Scientist"
    e1.printInfo()  # 예상 출력: ID: 3, Name: Charlie, Skill: Data Scientist

    # 테스트 9: Person, Manager, Employee 섞어 출력
    for person in [p1, m1, e1, p2, m2, e2]:
        # Person, Manager, Employee 객체가 모두 person 변수에 담길 수 있으며,
        # 각 객체는 자신에 맞는 printInfo() 메서드를 호출합니다.
        person.printInfo()

    # 테스트 10: Manager, Employee 상속 확인
    assert isinstance(m1, Person), "Manager는 Person의 하위 클래스여야 합니다."
    assert isinstance(e1, Person), "Employee는 Person의 하위 클래스여야 합니다."

# 테스트 실행
test()
