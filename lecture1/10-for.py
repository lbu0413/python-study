# for 반복문

# for in <collection>
#   <Loop body>

for v1 in range(10):
    print("v1: ", v1)

for v2 in range(1, 11):
    print("v2: ", v2)

for v3 in range(1, 11, 2):
    print("v3: ", v3)

# 1 ~ 1000 합
sum1 = 0
for v in range(1, 1001):
    sum1 += v
print(sum1)
print("1~1000", sum(range(1, 1001)))
print("1~1000 4의 배수의 합: ", sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# ex1)
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]
for name in names:
    print("You are: ", name)

# ex2)
lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print("current number: ", n)

# ex3)
word = "Beatufiul"
for s in word:
    print("word: ", s)

# ex4)
my_info = {"name": "Wook", "age": 28, "city": "Seoul"}
for k in my_info:
    print("key: ", my_info)

for v in my_info.values():
    print("value: ", v)

for z in my_info.keys():
    print("value: ", z)

# ex5)
name = "PineAppLE"
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

print(name.upper())


# break
numbers = [14, 3, 4, 7, 19, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 34:
        print("Found: 34")
        break
    else:
        print("Not Found: ", num)


# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print("current type: ", v, type(v))


# for-else
numbers = [14, 3, 4, 7, 19, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("found: 24")
        break
else:
    print("Not found: 24")

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print("{:4d}".format(i * j), end="")

# 변환 예제
name2 = "Aceman"

print("reversed", reversed(name2))
print("list", list(reversed(name2)))
print("tuple", tuple(reversed(name2)))
print("set", set(reversed(name2)))
