# Print

print("hello world")
print("""Python""")
print()  # 공백
print("""hi""")

# seperator
print("P", "Y", "T", "H", "O", "N", sep="")
print("010", "7777", "1234", sep="-")
print("python", "google.com", sep="@")

# end
print("Welcome to", end=" ")
print("IT News", end=" ")
print("Web Site")

# file
# stdout = console을 의미
import sys

print("Learn Python", file=sys.stdout)


# format (d, s, f)
# d는 digit, s는 string, f는 float
print("%s %s" % ("one", "two"))
print("{} {}".format("one", "two"))
print("{1} {0}".format("one", "two"))


# %s
print("%10s" % ("nice"))
print("{:>10}".format("nice"))  # 총 10자리를 공백과 함께 확보/ 공백이 왼쪽으로 먼저 온다

print("%-10s" % ("nice"))
print("{:10}".format("nice"))  # 총 10자리를 공백과 함께 확보/ 공백이 오른쪽으로 나중에 온다

print("{:_>10}".format("nice"))  # 10자리를 _표시와 함께 확보
print("{:^10}".format("nice"))  # 10자리를 확보하고 nice를 중앙으로 포맷

print("%.5s" % ("nice"))
print("%.5s" % ("pythonstudy"))  # .을 붙이면 5자리를 확보하고 나머지는 자른다.
print("{:10.5}".format("pythonstudy"))


# %d
print("%d %d" % (1, 2))
print("{} {}".format(1, 2))

print("%4d" % (422))
print("{:4d}".format(422))


# %f
print("%1.4f" % (3.14123123123))
print("{:1.4f}".format(3.15151515))

print("%06.2f" % (3.14159244334535213123123123))
print("{:06.2f}".format(3.14159244334535213123123123))
