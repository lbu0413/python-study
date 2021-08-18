# self의 이해


# self가 없는 것은
# 클래스 메소드이기 때문에 클래스가 직접 호출
# self가 있는 것은 인스턴스 메소드다.


class SelfTest:
    def func1():
        print("Func1 called")

    def func2(self):
        print(id(self))
        print("Func2 called")


# init method를 만들지 않으면
# 파이썬이 내부적으로 알아서 만들어줌
f = SelfTest()
print(id(f))
# 인스턴스 f는 self와 같다.
# f.func1() 에러발생 / 예외
f.func2()

SelfTest.func1()
SelfTest.func2(f)

# ex3)
# 클래스 변수, 인스턴스 변수
# 클래스는 모두가 공유하는,
# 인스턴스는 나만의,
# 예를 들어 클래스는 과일의 속성을 가지고 있고
# 인스턴스는 과일의 종류인 딸기나 수박의 속성을 가지고 있을 수 있다.


class Warehouse:
    # 클래스 변수
    stock_number = 0
    # 인스턴스 변수
    def __init__(self, name):  # 인스턴스 초기화
        self.name = name
        Warehouse.stock_number += 1

    def __del__(self):  # 인스턴스 삭제
        Warehouse.stock_number -= 1


user1 = Warehouse("Lee")
user2 = Warehouse("Cho")
print("stock number: ", Warehouse.stock_number)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print("before", Warehouse.__dict__)

del user1

print("after", Warehouse.__dict__)
