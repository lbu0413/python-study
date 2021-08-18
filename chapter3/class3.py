# ex4)
class Dog:  # object 상속
    # 클래스 속성
    species = "firstdog"

    # 초기화 / 인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} speaks {}!".format(self.name, sound)


# 인스턴스 생성
# self의 id 값과 c의 id 값은 같다
d = Dog("Mary", 10)
c = Dog("July", 4)
print(c.info())
print(c.speak("wal wal"))
print(d.speak("mung mung"))
