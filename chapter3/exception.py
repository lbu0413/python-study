# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError

# 1. 예외는 반드시 처리.
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError: 문법 오류

# NameError: 참조 없음
# a = 10
# b = 20
# print(c)

# AttributeError: 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# TypeError: 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2]
# y = (1, 2)
# z = "test"
# print(x + y)


# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러이름1:
# else: try block에 에러가 없을 경우 실행
# finally: 항상 실행

name = ["Lee", "Kim", "Park"]

# ex)
# try:
#     z = "Kim"
#     x = name.index(z)
#     print("{} Found in name, {}".format(z, x + 1))
# except ValueError:
#     print("Not Found it - Occurred ValueError")
# else:
#     print("Ok! else.")
# print()


# ex2)
# try:
#     z = "Cho"
#     x = name.index(z)
#     print("{} Found in name, {}".format(z, x + 1))
# except Exception: # 그냥 except만 써도 가능.
#     print("Error")
# else:
#     print("Ok! else.")
# print()

# ex3)
# try:
#     z = "Cho"
#     x = name.index(z)
#     print("{} Found in name, {}".format(z, x + 1))
# except Exception as e:
#     print(e)
#     print("Error")
# else:
#     print("Ok! else.")
# print()


# ex4)
# 예외 발생: raise

try:
    a = "Park"
    if a == "Kim":
        print("Ok! pass")
    else:
        raise ValueError
except ValueError:
    print("ValueError Occurred")
