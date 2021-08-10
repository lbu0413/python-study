# tuple
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X, 삭제X) immutable

# 선언
a = ()
b = (1, 2)
c = (1,)  # 원소가 하나 일때는 ,를 찍어줘야 튜플로 인식한다.
d = (11, 12, 13, 14)
e = (100, 1000, "Ace", "Base", "Captain")
f = (100, 1000, ("Ace", "Base", "Captain"))
print((type(a)), type(b), type(c), type(d), type(e), type(f))

# 인덱싱
print("e - ", e[1])
print("e - ", e[0] + e[1] + e[1])
print("e - ", f[-1])
print("e - ", f[-1][1])
print("e - ", list(f[-1][1]))

# 수정X
# e[0] = 1500

# 슬라이싱
print("e - ", e[0:3])
print("e - ", e[2:])
print("f - ", f[2][1:3])


# 튜플 연산
print("d + e", d + e)
print("d * 3", d * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print("a - ", a)
print("a - ", a.index(3))
print("a - ", a.count(2))

# 팩킹 & 언팩킹

# 팩킹
t = ("foo", "bar", "baz", "qux")
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)


# 팩킹 & 언팩킹
t2 = (1, 2, 3)
t3 = (4,)
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
