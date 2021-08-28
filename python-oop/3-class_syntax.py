class Cal:
    # __init__ 생성자, constructor
    # 클래스로 인스턴스를 만들었을 때 즉시 실행이 되는 함수.
    # self는 클래스로 인스턴스를 만들었을 때, 인스턴스를 지칭하는 것.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


calculator1 = Cal(1, 2)  # 인스턴스 생성, 메모리에 올라감
calculator2 = Cal(3, 4)
print(calculator1.a)
print(calculator1.b)
print(calculator1.add())

print(calculator2.a)
print(calculator2.b)
print(calculator2.add())


calculator1.a = 7  # 외부에서 namespace 변경
print(calculator1.a)
print(calculator1.b)
print(calculator1.add())
