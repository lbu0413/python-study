# csv 파일 읽기 및 쓰기
# CSV : MEME - text/csv

import csv

# ex)
with open("./resource/test1.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Header Skip

    # 객체 확인
    print(reader)
    print(type(reader))
    # 속성 확인
    print(dir(reader))
    # 정보 가져오기
    for c in reader:
        print(" ".join(c))


# ex2)
with open("./resource/test2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")
    for c in reader:
        print(c)
print()

# ex3)
with open("./resource/test1.csv", "r") as f:
    reader = csv.DictReader(f)
    for i in reader:
        for j, k in i.items():
            print(j, k)
        print("---------")


# ex4)
w = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
]
with open("./resource/write1.csv", "w", encoding="UTF-8") as f:
    print(dir(csv))
    wt = csv.writer(f)

    # dir 확인
    print(dir(wt))

    for v in w:
        wt.writerow(v)


with open("./resource/write2.csv", "w", encoding="UTF-8") as f:
    fields = ["One", "Two", "Three"]

    # dict writer
    wt = csv.DictWriter(f, fieldnames=fields)
    # header writer
    wt.writeheader()

    for v in w:
        wt.writerow({"One": v[0], "Two": v[1], "Three": v[2]})
