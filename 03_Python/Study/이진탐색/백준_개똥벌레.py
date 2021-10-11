# 백준 3020번 개똥벌레
from sys import stdin
from collections import deque
n, h = map(int, input().split())
# stalagmite = [] # 석순
# stalactite = [] # 종유석
cave = deque()
heights = [0 for _ in range(h+1)]
for i in range(n):
    temp = int(input())
    if i % 2 == 0:
        # 석순
        cave.append([0, temp])
    else:
        # 종유석
        cave.append([h-temp, h])

mid = h//2
for i in range(n):
    low, high = cave.popleft()


