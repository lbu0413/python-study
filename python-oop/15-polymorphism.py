"""
polymorphism
- 여러 형태를 가질 수 있도록 하는 것.
- 객체를 부품화할 수 있다.

"""


class Robot:
    """
    [Robot Class]
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid age")
        else:
            self.__age = new_age

    def __say_hi(self):
        print(f"Greetings, my master. call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f"we have {cls.population} robots")


# 같은 형태의 코드가 다른 의미를 가지는 것 -> polymorphism


class Siri(Robot):
    def say_apple(self):
        print("Hello my apple")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요 from Siri")


class Bixby(Robot):
    def say_samsung(self):
        print("안녕하세요 from bixby")
