# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.

# 입력
# hello world! 123

# 출력
# LETTERS 10
# DIGITS 3

n = input()

letters = 0
digits = 0
for i in n:
    if i.isalpha():
        letters += 1
    if i.isnumeric():
        digits += 1
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
