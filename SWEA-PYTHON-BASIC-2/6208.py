# 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
# 메서드를 호출하는 코드를 작성해봅시다.


class Korean:
    @staticmethod
    def printNationality():
        return "대한민국"


print(Korean.printNationality())
