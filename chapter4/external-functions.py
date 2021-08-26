# external functions


# ex)
import sys

print(sys.argv)

# ex2) 강제종료
# sys.exit()

# ex3) 파이썬 패키지 위치
print(sys.path)

# pickle: 객체 파일 쓰기
import pickle

# ex4) 쓰기
f = open("test.obj", "wb")
obj = {1: "python", 2: "study", 3: "basic"}
pickle.dump(obj, f)
f.close()

# ex5) 읽기
f = open("test.obj", "rb")
data = pickle.load(f)
print(data, type(data))
f.close()

# os: 운영체제, 환경변수
# mkdir, rmdir, rename

# ex6)
import os

for i in os.environ:
    print(i)

# ex7) 현재경로
print(os.getcwd())


# time: 시간 관련 처리
import time

# ex8)
print(time.time())

# ex9) 형태변환
print(time.localtime(time.time()))

# ex10)
print(time.ctime())
# Thu Aug 26 16:10:40 2021

# ex11)
print(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time())))


# ex12) 시간 간격 발생
# for i in range(5):
#     print(i)
#     time.sleep(1)


# random
import random

print(random.random())  # 0 ~ 1 실수

print(random.randint(1, 45))
print(random.randrange(1, 45))


# 섞기
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)


# 무작위 선택
c = random.choice(d)
print(c)


# webbrowser : 본인 os의 웹 브라우저 실행
import webbrowser

webbrowser.open("http://www.wook-lee.com")
webbrowser.open_new('http://www.google.com')