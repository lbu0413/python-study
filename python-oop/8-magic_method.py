class Robot:
    """
    [Robot Class]
    Author: 이병욱
    Role: ???
    """

    population = 0

    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
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


siri = Robot("siri", 2103898223)
jarvis = Robot("jarvis", 124948933)
bixby = Robot("bixby", 891923222)
droid1 = Robot("R2-D2", 1241243)
Robot.how_many()

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)

print(Robot.say_hi(siri) == siri.say_hi())

print(dir(siri))
print(dir(Robot))

print(Robot.__doc__)
print(siri.__class__)

# __magic__ 이렇게 언더스코어로 이루어진 함수들을
# 통칭 magic method라고 부른다.
print(droid1)  # <__main__.Robot object at 0x10594fcd0> -> R2-D2 robot!
