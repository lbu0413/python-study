"""
pulbic vs private

encapsulation:
    객체의 속성과 행위(methods)를 하나로 묶고, 구현된 일부를 감추어 은닉한다.
"""

# 파이썬의 모든 클래스는 Object 클래스를 상속한다. -> 모든것은 객체이다.


class Robot:  # 모든 클래스는 오프젝트를 상속한다.
    """
    [Robot Class]
    """

    population = 0

    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.__age = age  # __를 추가하면 private 변수로 만들어준다.
        Robot.population += 1  # 로봇 인스턴스가 만들어질때마다 증가

    def __say_hi(self):  # private method
        print(f"Greetings, my master. call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod  # decorator
    def how_many(cls):  # cls는 클래스를 받는다.
        print(f"we have {cls.population} robots")


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)

        self.__age = 999  # 시리 클래스 안에 새로운 private age를 만든 것.
        print(self.__age)


ss = Robot("yss", 8)
print(ss.__say_hi())  # error
sss = Siri("iphone", 9)
