# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.
# 입력
# 89, 90, 100
# 출력
# 국어, 영어, 수학의 총점: 279


class Student:
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    @property
    def kor(self):
        return self.__kor

    @property
    def eng(self):
        return self.__eng

    @property
    def math(self):
        return self.__math

    def scores(self):
        return f"국어, 영어, 수학의 총점: {self.kor + self.eng + self.math}"


students = list(map(int, input().split(", ")))
students_list = Student(students[0], students[1], students[2])
print(students_list.scores())
