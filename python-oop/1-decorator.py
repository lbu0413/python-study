# decorator
# 기존의 함수를 꾸며주는 역할
# 데코레이터 패턴은 함수의 객체와 함수를 변경하는 다른 객체를 wrapping 한다.


def copyright(func):
    def new_func():
        print("@wook")
        func()

    return new_func


@copyright  # smile = copyright(smile)
def smile():
    print("😀")


@copyright
def angry():
    print("😡")


@copyright
def sad():
    print("😢")


smile()
angry()
sad()
