# 다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.
# 입력
# 12
# 출력
# [1, 2, 3, 4, 6, 12]
n = int(input())
arr = []
for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)
print(arr)
