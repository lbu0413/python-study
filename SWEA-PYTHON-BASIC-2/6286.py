# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.
# 입력없음
# 출력
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# arr = []
# a, b = 1, 1
# for i in range(1, 11):
#     arr.append(a)
#     a, b = b, a + b
# print(arr)
a = [1, 1]
b = [a.append(a[i - 1] + a[i]) for i in range(1, 9)]
print(a)
