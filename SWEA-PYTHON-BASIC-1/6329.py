# 인자로 전달된 숫자를 이용해 카운트다운하는 함수 countdown을 정의하고,
# 이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.
# 0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.
# 입력없음
# 출력
# 카운트다운을 하려면 0보다 큰 입력이 필요합니다.
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


def countdown(n):
    if n <= 0:
        return "카운트다운을 하려면 0 보다 큰 입력이 필요합니다"
    for i in range(1, n + 1):
        print(n + 1 - i)


print(countdown(0))
print(countdown(10))
