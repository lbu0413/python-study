# self의 이해
# self는 인스턴스 객체이다
# 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다.
# 즉, self는 인스턴스 그 자체이다.


class SelfTest:
    # 클래스 변수
    name = "wook"

    def __init__(self, x):
        self.x = x

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메소드
    def func2(self):
        print(f"self: {self}")
        print("class안의 self 주소: ", id(self))
        print("func2")


test_obj = SelfTest(17)
test_obj.func2()
SelfTest.func1()
print("인스턴스의 주소: ", id(test_obj))

"""
self: <__main__.SelfTest object at 0x1078f8d60>
class안의 self 주소:  4421815648
func2
cls: <class '__main__.SelfTest'>
func1
인스턴스의 주소:  4421815648
"""

# func1은 클래스 메소드이고 name도 마찬가지로 클래스의 변수이지만
# 인스턴스 네임스페이스에서 실행시켜도 작동한다.
test_obj.func1()
print(test_obj.name)

# 하지만 반대로
# 클래스 네임스페이스에서 인스턴스 메소드를 실행시키지 못한다.
# 모든 인스턴스는 독립적이기 때문.
SelfTest.func2()  # 에러
print(SelfTest.x)  # 에러
