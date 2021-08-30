"""
namespace: 개체를 구분할 수 있는 범위
__dict__: 네임스페이스를 확인할 수 있다
dir(): 네임스페이스의 key 값을 확인할 수 있다
__doc__: class의 주석을 확인한다
__class__: 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다
"""


class Robot:
    """
    [Robot Class]
    Author: 이병욱
    Role: ???
    """

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

    @staticmethod
    def this_is_robot_class():
        print("yess")


siri = Robot("siri", 2103898223)
jarvis = Robot("jarvis", 124948933)
bixby = Robot("bixby", 891923222)
Robot.how_many()

# 메모리 효율을 위해 클래스 namespace 안에 인스턴스의 정보가 다 들어가있다.
print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)

# say_hi는 인스턴스 메소드
print(Robot.say_hi(siri) == siri.say_hi())

# dir은 접근 가능한 모든 메소드들(key값)을 보여준다
print(dir(siri))
print(dir(Robot))


# doc 메소드는 클래스 안에 주석을 확인할 수 있는 메소드
# 클래스 설계는 보통 추상적이기 때문에 주석만 확인해서 클래스의 용도를 파악하는 경우를 위해.
print(Robot.__doc__)


# __class__ 어떤 인스턴스가 속해있는 클래스를 확인하고 싶을때 사용.
print(siri.__class__)
