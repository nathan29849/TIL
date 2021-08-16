# 백준 2075번 정렬

from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    arr += list(map(int, stdin.readline().split()))
    arr.sort(reverse=True)
    arr = arr[:n]

print(arr[-1])