# lambda
# 가독성 향상, 메모리 절약, 코드 간결
# 하지만 람다식을 부정하는 의견도 많다
# 일반적인 함수 - 객체 생성 -> 리소스 (메모리) 할당
# 램다는 즉시 실행 함수 (Heap 초기화) -> 메모리 초기화
# 너무 남발 시, 가독성이 오히려 감소


def mul_func(x, y):
    return x * y


a = lambda x, y: x * y
a(5, 6)

# 람다 예제
def func_final(x, y, func):
    print(x * y * func(100, 100))


func_final(10, 20, lambda x, y: x * y)
