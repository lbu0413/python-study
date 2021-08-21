from datetime import datetime

a = input()
b = int(input())

today = str(datetime.today()).split()
year = int(today[0].split("-")[0])
ageDiff = 100 - b

print(f"{a}(은)는 {year + ageDiff}년에 100세가 될 것 입니다.")
