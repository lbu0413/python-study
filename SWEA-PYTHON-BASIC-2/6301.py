# 항목 값으로는 0을 갖는 2*3*4 형태의 3차원 배열을 생성하는
# 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

# array = [[[0 for k in range(4)] for j in range(3)] for i in range(2)]
# print(array)
array = []
for i in range(2):
    i = 0
    first_array = []
    for j in range(3):
        j = 0
        second_array = []
        first_array.append(second_array)
        for k in range(4):
            k = 0
            second_array.append(j * k)
    array.append(first_array)

print(array)
