n = input()


def palindrome(n):
    ans = n[::-1]
    if n == ans:
        print(ans)
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print("입력하신 단어는 회문이 아닙니다.")


palindrome(n)
