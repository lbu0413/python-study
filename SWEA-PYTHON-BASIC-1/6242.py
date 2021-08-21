# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

students = ["A", "A", "A", "O", "B", "B", "O", "AB", "AB", "O"]
bloodtype = {}

for i in students:
    if i in bloodtype:
        bloodtype[i] += 1
    else:
        bloodtype[i] = 1

print(bloodtype)
