input = "abcba"


# 재귀함수를 이용하여 풀어보기 (feat. 문자열 슬라이싱을 이용)
def is_palindrome(string):
    n = len(string)
    if n <= 1:
        return True
    if string[0] == string[-1]:
        string = string[1:n-1]
        # string = string[1:-1] 이렇게 해도 되네!
        
        return is_palindrome(string)
    else:
        return False

 

print(is_palindrome(input))