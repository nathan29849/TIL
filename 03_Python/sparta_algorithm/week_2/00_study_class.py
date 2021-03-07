class Person:
    # constructor를 설정하기 위해선 __init__함수를 만들어야 함.
    def __init__(self, param_name):  
        # self의 의미 : python의 경우 constructor를 생성하거나, class 내부에 함수를 만들 때, 인자에 자기 자신을 넘겨주게 됨.
        # 따라서 self를 따로 넘겨주지 않아도 python class가 알아서 자기 자신을 넘겨준다고 생각하면 됨
        print("I am created!", self)
        self.name = param_name
        
    # 항상 함수(메소드)를 만들 때, self가 인자로 들어가 있어야 한다.
    def talk(self):
        print("안녕하세요, 제 이름은", self.name+"입니다.")




# 소괄호 () 의 의미 : 생성자(constructor)
# 객체를 생성할 때 쓰는 함수를 의미함.
# 소괄호 열고 닫고가 생성자이므로, 이 Person이 호출된 순간에
# 내부의 함수가 호출된 거라 print문이 출력된 것임.
person_1 = Person("유재석") 
print(person_1)
print(person_1.name)
person_1.talk()
person_2 = Person("박명수")
print(person_2)
print(person_2.name)
person_2.talk()

# class를 이용하면 유사한 행동, 유사한 데이터를 쌓을 수 있게 만들 수 있음
# 연관성 있는 데이터들을 내부에서 관리하면서 다양한 객체를 쉽게 생성하기 위해서는 클래스를 활용해야 한다.