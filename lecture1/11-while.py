# while <expression>:
#   <statement(s)>


# ex)
n = 5
while n > 0:
    print(n)
    n = n - 1

# ex2)
a = ["foo", "bar", "baz"]
while a:
    print(a.pop())

# ex3)
# break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("Loop ended")


# ex4)
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print("Loop ended")


# nested if
# ex5)
i = 1
while i <= 10:
    print("i: ", i)
    if i == 6:
        break
    i += 1


# while else
# ex6)
n = 10
while n > 0:
    n -= 1
    print(n)
    if n == 5:
        break
else:
    print("else out")


# ex7)
a = ["foo", "bar", "baz", "qux"]
s = "qux"

i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, "not found in list.")


# ex8)
a = ["foo", "bar", "baz"]
while True:
    if not a:
        break
    print(a.pop())
