import time
import csv
import random


name = input("Please enter your name: ")

print(f"Hi, {name}. It's time to play the game!")
print()

time.sleep(1)
print("Start loading..")
print()
time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 csv 파일 로드
with open("./resource/word_list.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)
# 리스트 섞기
random.shuffle(words)
q = random.choice(words)


# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ""

# 기회
turns = 10

# 핵심 while loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=" ")
        else:
            # 틀린 경우
            print("_", end=" ")
            failed += 1
    if failed == 0:  # 정답
        print()
        print()
        print("Congratulations! you guessed the word!")
        break
    print()
    # 추측 단어 문자 단위 입력
    print()
    print("Hint: {}".format(q[1].strip()))
    guess = input("Guess a character in the word! ")
    guesses += guess

    # 정답 단어에 추측한 문자가 포험되어 있지 않을 경우
    if guess not in word:
        turns -= 1
        # 오류 메세지
        print("sorry your guess is not in the word")
        print(f"You have {turns} guesses remaining")

        if turns == 0:
            print("You failed to guess the word :( ")
