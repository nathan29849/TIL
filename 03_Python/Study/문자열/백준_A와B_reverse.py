# 백준 12904번 A와 B
from sys import stdin
from collections import deque
input = stdin.readline

S = input().rstrip()
T = input().rstrip()

def solution(T, S):
    while T != S:
        if T[-1] == "A":
            T = T[:-1]
        else:
            T = T[::-1][1:]
        # print(T)

        if len(T) <= len(S):
            if T == S:
                return 1
            else:
                return 0
    return 1

print(solution(T, S))