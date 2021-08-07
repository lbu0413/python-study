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
