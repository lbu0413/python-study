# 리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 짝수를 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.
# 출력
# [5, 77, 45]
n = [5, 6, 77, 45, 22, 12, 24]
ans = [i for i in n if i % 2 != 0]
print(ans)
