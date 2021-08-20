# 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한

# 팩토리얼 값을 구하는 프로그램을 작성하십시오.
# 입력
# 5
# 출력
# 120
n = int(input())

sum = 1
for i in range(1, n + 1):
    sum *= i

print(sum)
