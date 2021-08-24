# 백준 1701번 Cubeditor (문자열)
from sys import stdin
input = stdin.readline

string = input().rstrip()

def solution(string):
    n = len(string)
    final = 0
    temp = [0] * (n)
    dictionary = {}
    for i in range(n):
        if dictionary.get(string[i]):
            if i > 0:
                temp[i] = temp[i-1] + 1
        else:
            dictionary[string[i]] = 1

    print(temp)
    return max(temp)
print(solution(string))