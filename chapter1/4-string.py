# 파이썬 문자형
# 문자형은 매우 중요

str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = """Thank you"""

print(len(str1))

# 빈 문자열
str1_t1 = ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# escape 문자
print("I'm a boy")
print("I'm a boy")
print("I\\'m a boy")
print("a\tb")
print("a\nb")

escape_str1 = 'Do you have "retro games"?'
print(escape_str1)
escape_str2 = "What's going on?"
print(escape_str2)

# \t \n
t_s1 = "Click \t start!"
print(t_s1)
t_s2 = "New Line \n Check!"
print(t_s2)

# Raw String
raw_s1 = r"D:\python\test"
print(raw_s1)
hello = r"hello\world :)"
print(hello)

# Multi-Line input
multi_str = """
string
multi line
test
"""
print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "how are you doing"
str_o4 = "seoul daejeon busan jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print("y" in str_o1)
print("n" in str_o1)
print("z" in str_o1)
print("P" not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

print(divmod(100, 3))


# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha....)
print("capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("e"))
print("replace: ", str_o1.replace("thon", "Good"))
print("sorted: ", sorted(str_o1))  # 리스트 형태로 반환
print("split: ", str_o4.split())

# 반복 (시퀀스)
im_str = "Good Boy!"
# print(dir(im_str))  # __iter__

# 출력
# for i in im_str:
#     print(i)

# 슬라이싱 연습
str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3])
print(str_s1[1:2])
print(str_s1[5:])
print(str_s1[5 : len(str_s1)])
print(str_s1[1:4:2])  # index 1부터 4까지 가져오는데 2칸씩 띄움
print(str_s1[1:9:2])
print(str_s1[:-1])  # 처음부터 -1 인덱스까지.
print(str_s1[1:-2])
print(str_s1[::2])  # 처음부터 끝까지 2칸씩 띄우면서 가져옴
print(str_s1[::-1])  # reverse


# ascii code
a = "z"

print(ord(a))  # ascii code
print(chr(122))  # ascii code를 집어넣으면 캐릭터를 리턴
