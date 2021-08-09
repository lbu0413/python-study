# 파이썬에서 지원하는 자료형
# int: 정수
# float: 실수
# complex: 복소수
# bool: boolean
# str: 문자열 (sequence)
# list : 배열 (sequence)
# tuple: 튜플 (sequence)
# set: 집합
# dictionary: 사전

# 데이터 타입
str1 = "Python"
bool = False
str2 = "Anaconda"
float_v = 10.0  # 10 == 10.0는 다르다
int_v = 7
list = [str1, str2]
dict = {"name": "machine Learning", "version": 2.0}
tuple = (7, 8, 9)  # 괄호없이 ,로 나열해도 tuple로 인식됨.
set = {7, 8, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))


# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) == x ** y 
"""

# 정수 선언
i = 77
i2 = -14
big_int = 88889898989898989822392893829389283928398293

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)


# 연산 실습
i1 = 39
i2 = 939
big_int1 = 1248981294812940184920148012498210498491048
big_int2 = 4921849124801249849545453512312045645645645
f1 = 1.234
f2 = 3.939

# +
print(">>>>>>>>>+")
print("i1 + i2: ", i1 + i2)
print("f1 + f2: ", f1 + f2)
print("big_int1 + big_int2: ", big_int1 + big_int2)


# *
print(">>>>>>>>>*")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)


# 형 변환 실습
a = 3.0
b = 6
c = 0.7
d = 12.7

# 출력
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))  # True: 1, False: 0
print(int(False))
print(float(False))
print(complex(3))
print(int("3"))
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)  # 나누기 몫과 나머지
print([x, y])
print(pow(5, 3), 5 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1))
print(math.pi)
