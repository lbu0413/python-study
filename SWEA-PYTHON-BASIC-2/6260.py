# 다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.
# 입력
# Hello World! 123
# 출력
# UPPER CASE 2
# LOWER CASE 8
n = input().strip()
upper = 0
lower = 0
for i in n:
    if i >= "a" and i <= "z":
        lower += 1
    elif i >= "A" and i <= "Z":
        upper += 1

print(f"UPPER CASE {upper}")
print(f"LOWER CASE {lower}")
