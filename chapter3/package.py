# 패키지는 모듈을 모아놓은 폴더이다.
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성
# 상대경로: ..(parent directory), .(current directory)

# __init__.py: python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천

# ex)
import sub.sub1.module1
import sub.sub2.module2

# 사용
print(sub.sub1.module1.mod1_test1())
print(sub.sub1.module1.mod1_test2())

print(sub.sub2.module2.mod2_test1())
print(sub.sub2.module2.mod2_test2())

print()
print()
print()

# ex2)
from sub.sub1 import module1
from sub.sub2 import module2 as m2  # alias

module1.mod1_test1()
m2.mod2_test1()

print()
print()
print()

# ex3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()

# ex4)
import module as m

print(m.add(2, 4))
print(m.multiply(2, 4))

# # ex 5)
from sub.sub1 import module1 as mm1

print(mm1.mod1_test2())
