# https://www.daleseo.com/python-int-bases/
# 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.
# 입력
# 9
# 출력
# 1001
n = input()
# print(bin(int(n)).replace("0b", ""))
print(format(int(n), "b"))
