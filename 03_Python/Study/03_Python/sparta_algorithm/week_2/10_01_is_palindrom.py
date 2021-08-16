input = "abcba"


def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] == string[len(string)-i-1]:
            continue
        else:
            return False
    return True

# 재귀함수를 이용하여 풀어보기 (feat. 문자열 슬라이싱을 이용)


print(is_palindrome(input))