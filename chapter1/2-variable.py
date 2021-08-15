# 기본 선언
n = 700

print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언
var = 75
# 재선언
var = "Change Value"
# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex 1)
print(300)  # 내부적으로 int object을 만듬
print(int(300))

# ex 2)
n = 777  # 내부적으로 int object을 만듬
print(n, type(n))

m = n
print(m, n)
print(type(m), type(n))

m = 400
print(m, n)
print(type(m), type(n))

# id

# 같은 오브젝트를 참조.
m = 800
n = 655

print(id(m))  # object의 고유 값
print(id(n))
print(id(m) == id(n))  # false

m = 800
n = 800
print(id(m) == id(n))  # true


# 다양한 변수 선언 방법
# camelCase: numberOfCollegeGraduates -> Method
# PascalCase: NumberOfCollegeGraduates -> Class
# snake_case: number_of_college_graduates
