# 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
# [입력]
# 두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.
# [출력]
# 첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.
# 예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.
# 단, 비긴 경우는 Result : Draw 라고 출력한다.

n = input()
m = input()

if n == "가위" and m == "보":
    print("Result : Man1 Win!")
elif n == "바위" and m == "가위":
    print("Result : Man1 Win!")
elif n == "보" and m == "바위":
    print("Result : Man1 Win!")
elif n == m:
    print("Result : Draw")
else:
    print("Result: Man2 Win!")
