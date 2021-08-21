a, b = map(str, input().split(", "))


def str_length(a, b):
    if len(a) > len(b):
        return a
    else:
        return b


print(str_length(a, b))
