# 백준 1010번 다리 놓기
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())


def bridge(n, m):
    if n >= m:
        return 1
    else:
        