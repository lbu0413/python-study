# Module
# Module: 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일로 재사용이 가능하고 타인이 가져다 쓸 수 있다.


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


# print("-" * 15)
# print("called inner!")
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(5, 5))
# print(divide(10, 2))
# print(power(5, 3))
# print("-" * 15)

# __name__ 사용
if __name__ == "__main__":
    print("-" * 15)
    print("called main!")
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(10, 2))
    print(power(5, 3))
    print("-" * 15)
