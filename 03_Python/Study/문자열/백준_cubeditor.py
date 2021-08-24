# 백준 1701번 Cubeditor (문자열)
from sys import stdin
input = stdin.readline

string = input().rstrip()

def solution(string):
    n = len(string)
    final = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if string[i] == string[j]:
                LCS = 1
                for k in range(1, n-j):
                    if string[i+k] == string[j+k]:
                        LCS += 1
                    else:
                        break
                if final < LCS:
                    final = LCS
    return final

print(solution(string))

# O(N^2)