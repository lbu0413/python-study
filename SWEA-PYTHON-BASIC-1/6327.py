# 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면


# 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.
a, b = map(int, input().split(", "))


def math(a, b):
    print(f"square({a}) => {a**2}")
    print(f"square({b}) => {b**2}")


print(math(a, b))
