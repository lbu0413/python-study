# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다

# 함수 정의 방법
# def function_name(param):
#   code

# ex)
def first_function(w):
    print("hello, ", w)


print(first_function("Wook"))

# ex2)
def return_function(w1):
    value = "Hello, " + str(w1)
    return value


x = return_function("Wook")
print(x)

# ex3) 다중반환
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


x, y, z = func_mul(10)  # unpacking
print(x, y, z)

# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)


q = func_mul2(20)  # packing
print(type(q), q)

# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]


p = func_mul3(30)
print(type(p), p, set(p))

# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {"v1": y1, "v2": y2, "v3": y3}


d = func_mul4(30)
print(type(d), d, d.get("v2"), d.items(), d.keys())
