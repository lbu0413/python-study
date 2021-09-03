# 파이썬의 모든 클래스는 Object 클래스를 상속한다. -> 모든것은 객체이다.


class Robot(object):  # 모든 클래스는 오프젝트를 상속한다.
    """
    [Robot Class]
    """

    population = 0

    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Robot.population += 1  # 로봇 인스턴스가 만들어질때마다 증가

    def say_hi(self):
        print(f"Greetings, my master. call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod  # decorator
    def how_many(cls):  # cls는 클래스를 받는다.
        print(f"we have {cls.population} robots")


class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b


siri = Siri("iphoneX")

print(Siri.mro())  # mro는 상속의 관계를 보여주는 메소드.
# [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
print(Robot.mro())
# [<class '__main__.Robot'>, <class 'object'>]
print(object)
print(dir(object))
print(object.__name__)
print(int.mro())
print(float.mro())
print(list.mro())


class A:
    pass


class B:
    pass


class C:
    pass


class D(
    A,
    B,
    C,
):
    pass


print(D.mro())
