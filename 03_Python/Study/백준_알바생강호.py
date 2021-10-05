# 백준 1758번 알바생 강호
from sys import stdin
input = stdin.readline
n = int(input())
lines = []
for _ in range(n):
    lines.append(int(input()))
lines.sort(reverse=True)
tip = 0
for i in range(n):
    # 0 1 2 3
    temp = lines[i] - i
    if temp > 0:
        tip += temp

print(tip)