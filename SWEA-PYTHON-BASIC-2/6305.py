# 리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해
# [12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.
# 출력
# [12, 24, 35, 88, 120, 155]


# 1
# a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# b = []
# a_list = [b.append(i) for i in a if i not in b]
# print(b)


# 2
# b = []
# def no_dup(a):
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b


# print(no_dup(a))

# 3
a = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
b = []
c = [i for i in sorted(list(set(a)))]
print(c)
