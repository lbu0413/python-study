# abs
print(abs(-3))

# all: iterable 요소 검사(참, 거짓)
# 모든 요소를 검사해 전부 True가 나오면 True를 리턴
# 한 개의 요소라도 거짓이라면 False 리턴
print(all([1, 2, 3]))


# any: iterable 요소 검사 (참, 거짓)
# 한 개의 요소라도 True라면 True를 리턴
print(any([1, 2, 3, 0]))

# chr: ascii -> chracter
# ord: character -> ascii
print(chr(67))
print(ord("C"))

# enumerate: index + interable 객체 생성
for i, name in enumerate(["abc", "bcd", "efg"]):
    print(i, name)

# filter: iterable로부터 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, -2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, -2, 0, -5, 6])))

# id: 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# len: 요소의 길이

# max, min: 최대값, 최소값, iterable을 넣으면 됨

# map: iterable에 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))

# pow: 제곱값 반환
print(pow(2, 10))

# range: 반복가능한 객체 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round: 반올림
print(round(6.5781, 2))
print(round(8.6))
print(round(8.2))

# sorted: iterable 객체를 정렬한 후 반환
print(sorted([6, 7, 4, 3, 1, 2]))
print(sorted(["p", "y", "t", "h", "o", "n"]))

# sum: iterable 객체 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 101)))

# zip: iterable 객체의 요소를 묶어서 반환
# 짝이 안맞으면, 짝이 맞는 요소들만 반환
print(list(zip([10, 20, 30], [40, 50, 60])))
print(list(zip([10, 20, 30], [40, 50])))
print(type(list(zip([10, 20, 30], [40, 50, 777]))[0]))
