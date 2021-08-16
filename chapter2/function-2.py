# 중요
# *args, **kwargs
# unpacking
def args_func(*args):
    for i, v in enumerate(args):
        print("Result: {}".format(i), v)
    print("-----")


args_func("Lee")
args_func("Lee", "Park")
args_func("Lee", "Park", "Kim")

# ** kwargs unpacking
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("-----")


kwargs_func(name1="Lee")
kwargs_func(name1="Lee", name2="Park")
kwargs_func(name1="Lee", name2="Park", name3="Kim")

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)


example(10, 20, "Lee", "Kim", "Park", age1=20, age2=30, age3=40)

# 중첩함수


def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)


nested_func(100)
