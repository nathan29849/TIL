# 백준 3020번 개똥벌레
from sys import stdin
from collections import deque
n, h = map(int, input().split())
mite = [] # 석순
tite = [] # 종유석

heights = [0 for _ in range(h+1)]
for i in range(n):
    temp = int(input())
    if i % 2 == 0:
        # 석순
        mite.append(temp) 
    else:
        # 종유석
        tite.append(temp)

mite.sort()   # 석순 오름차순 정렬
tite.sort()   # 종유석 오름차순 정렬

for i in range(1, h+1):
    count = 0
    for j in range(n//2):
        now = mite[j]
        if i > now:
            count += 1
        else:
            heights[i] = n//2 - count
            break

for i in range(h, 0, -1):
    count = 0
    for j in range(n//2):
        now = tite[j]
        # h - i + 1 : 전체 높이에서 현재 높이를 뺀 후 +1
        if h-i+1 > now: 
            count += 1
        else:
            heights[i] += n//2 - count
            break

min_num = min(heights[1:])
result = 0
for i in range(1, h+1):
    if min_num == heights[i]:
        result += 1

print(min_num, result)


