# 백준 9935번 문자열 폭발
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

string = input().rstrip()
exp = input().rstrip()

def solution(string, exp):
    m = len(exp)
    while exp in string:
        n = len(string)
        i = 0
        temp = ""
        while n - i> 0:
            if string[i:i+m] == exp:
                i += m
            else:
                temp += string[i]
                i += 1
        string = temp
        temp = string # UnboundLocalError
    return temp if len(temp) > 0 else "FRULA"

print(solution(string, exp))