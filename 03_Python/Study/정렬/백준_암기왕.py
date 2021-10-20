# 백준 2776번 암기왕
from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    cards = set(map(int, input().split()))
    m = int(input())
    check = list(map(int, input().split()))
    check_check = [0 for i in range(m)]
    dic = {}

    for j in range(m):
        if check[j] in cards:
            check_check[j] = 1

    for k in range(m):
        print(check_check[k])
