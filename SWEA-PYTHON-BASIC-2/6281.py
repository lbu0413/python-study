# 다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해
# 약수 리스트를 출력하는 코드를 작성하십시오.
# 입력
# 32
# 출력
# [1, 2, 4, 8, 16, 32]
n = int(input())
arr = []
for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)

print(arr)
