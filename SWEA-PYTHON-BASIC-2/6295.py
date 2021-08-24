# 다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
# 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.
# 입력
# 3, 5
# 출력
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

n = list(map(int, input().split(", ")))

# for문으로 만들기
# result = []
# for i in range(n[0]):
#     three_lists = []
#     for j in range(n[1]):
#         three_lists.append(i * j)
#     result.append(three_lists)
# print(result)


# list comprehension
result = [[i * j for i in range(int(n[1]))] for j in range(int(n[0]))]
print(result)
