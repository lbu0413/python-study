"""
abstraction
불필요한 정보는 숨기고 중요한 혹은 필요한 정보만을 표현함으로써
공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.
"""


class Robot:
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수 / constructor
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1  # 로봇 인스턴스가 만들어질때마다 증가

    # 인스턴스 메소드
    def say_hi(self):
        print(f"Greetings, my master. call me {self.name}")

    # 인스턴스 메소드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메소드
    def dead(self):
        print(f"{self.name} is dead")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last robot")
        else:
            print(f"we have {Robot.population} robots left")

    @classmethod  # decorator
    def how_many(cls):  # cls는 클래스를 받는다.
        print(f"we have {cls.population} robots")


siri = Robot("siri", 2103898223)
jarvis = Robot("jarvis", 124948933)
bixby = Robot("bixby", 891923222)
Robot.how_many()
