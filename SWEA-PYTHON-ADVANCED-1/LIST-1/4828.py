# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

# [입력]
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

test_length = int(input())

for i in range(1, test_length + 1):
    first_test_length = int(input())
    first_test = list(map(int, input().split()))
    print(f"#{i} {max(first_test) - min(first_test)}")
    i += 1
    second_test_length = int(input())
    second_test = list(map(int, input().split()))
    print(f"#{i} {max(second_test) - min(second_test)}")
    i += 1
    third_test_length = int(input())
    third_test = list(map(int, input().split()))
    print(f"#{i} {max(third_test) - min(third_test)}")
    if i == test_length:
        break
