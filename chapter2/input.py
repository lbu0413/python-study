# input은 무조건 문자열로 받는다

# ex)
# name = input("Enter your name: ")
# grade = input("Enter your grade: ")
# company = input("Enter your company: ")

# print(name, grade, company)

# ex2)
# number = input("Enter number: ")10

# print("type of number: ", type(number))
# print("type of name: ", type(name))


# ex3)
# first_number = int(input("Enter number1: "))
# second_number = int(input("Enter number2: "))

# total = first_number + second_number
# print(total)

# ex4)
# float_num = float(input("Enter a float number: "))
# print(float_num, type(float_num))

# ex5)
print(
    "firstName - {0}, lastName - {1}".format(
        input("Enter first name: "), input("Enter last name: ")
    )
)
