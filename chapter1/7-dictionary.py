# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)

# 선언
a = {"name": "Wook", "phone": "01033337777", "dob": "940413"}
b = {0: "Hello Python"}
c = {"arr": [1, 2, 3, 4]}
d = {
    "Name": "Niceman",
    "City": "Seoul",
    "Age": 28,
    "Grade": "A",
    "Status": True,
}

e = dict([("Name", "Niceman"), ("City", "Seoul")])
f = dict(Name="Niceman", City="Seoul", Age=28, Grade="A", Status=True)
print("a -", type(a), a)
print("b -", type(b), b)
print("c -", type(c), c)
print("d -", type(d), d)
print("e -", type(e), e)
print("f -", type(f), f)


# 출력
print("a - ", a["name"])  # 키가 없을 경우 에러
print("a - ", a.get("name"))  # 키가 없을 경우 None
print("f - ", f.get("City"))
print("f - ", f.get("Age"))


# 딕셔너리 추가
a["address"] = "seoul"
print(a)
a["rank"] = [1, 2, 3]
print(a)
print("a - ", len(a))  # 키의 길이

# 딕셔너리 함수
# dict_keys, dict_values, dict_items: 반복문(__iter__)에서 사용 가능

print("a - ", a.keys())
print("b - ", b.keys())
print("c - ", c.keys())
print("d - ", d.keys())
print("e - ", e.keys())

print("a - ", a.values())
print("a - ", list(a.keys()))
print("a - ", a.items())

print("a - ", a.pop("name"))
print(a)

print("f - ", f.popitem())
print(f)


print("a - ", "birth" in a)
print("d - ", "City" in d)


# 수정
a["test"] = "test_dict"
print("a - ", a)

a["address"] = "dj"
print("a - ", a)

a.update(dob="940412")
print("a - ", a)

temp = {"address": "busan"}
a.update(temp)
print("a - ", a)
