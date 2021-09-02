"""
Class Inheritance(상속)

1. 부모 클래스가 갖는 모든 메소드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메소드나 속성을 추가할 수 있다.
3. 메소드 오버라이딩
4. super()
5. Python의 모든 클래스는 object 클래스를 상속한다. -> 모든 것은 객체이다.
"""


class Robot:
    """
    [Robot Class]
    Author: 이병욱
    Role: ???
    """

    population = 0

    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Robot.population += 1  # 로봇 인스턴스가 만들어질때마다 증가

    def say_hi(self):
        print(f"Greetings, my master. call me {self.name}")

    def cal_add(self, a, b):
        return a + b

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

    @staticmethod  # 인스턴스로도 접근 가능.
    def this_is_robot_class():
        print("yess")

    def __str__(self):
        return f"{self.name} robot!"

    def __call__(self):
        # 함수도 객체이다. 모든 함수는 호출되기 때문에
        # __call__ 매직 메소드를 가지고 있다.
        print("called")
        return f"{self.name} calls!"


# inheritance
class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f"{cls}")


siri = Siri("iphoneX")

print(siri.call_me())
print(siri.cal_mul(1, 8))
print(Siri.hello_apple())
print(siri.a)
