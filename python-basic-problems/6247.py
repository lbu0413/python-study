# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# *******
#  *****
#   ***
#    *

# ljust, rjust, center, zfill
i = 7
while i > 0:
    print(("*" * i).center(7))
    i -= 2
