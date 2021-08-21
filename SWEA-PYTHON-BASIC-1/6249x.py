# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
# 입력
# 11
# 출력
# 0 1 2 3 4 5 6 7 8 9
# 0 2 0 0 0 0 0 0 0 0

n = input()
arr1 = [0 for i in range(10)]

for i in n:
    arr1[int(i)] += 1
for i in range(0, 10):
    print(i, end=" ")
print()
ans = " ".join([str(elem) for elem in arr1])
print(ans)
