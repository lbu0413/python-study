# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다
# 입력 c
# 출력 c(ASCII: 99) => C(ASCII: 67)

n = input()
up = n.upper()
low = n.lower()

if n == low:
    print(f"{low} (ASCII: {ord(low)}) => {up}(ASCII: {ord(up)})")
elif n == up:
    print(f"{up} (ASCII: {ord(up)}) => {low}(ASCII: {ord(low)})")
else:
    print(n)
