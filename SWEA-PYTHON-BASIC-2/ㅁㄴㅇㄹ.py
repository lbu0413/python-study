# # 1 - 100, 2진수로 바꾸고, 0이 하나만 포함된 숫자
# output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
# print(sum(output))

a = {"city": "atl", "name": "wook", "age": 28}

print(a.keys())
print(a.values())
print(a.items())
