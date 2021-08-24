# 단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.
# 입력
# python, hello, world, hi
# 출력
# hello, hi, python, world

# sort는 리스트 내장함수
# sorted는 이터러블 객체로부터 정렬된 리스트를 새로 생성.
# sort는 리스트만을 위한 메소드이지만 sorted()함수는 어떤 이터러블 객체도 받을 수 있다.

n = sorted(map(str, input().split(", ")))
print(", ".join(n))
