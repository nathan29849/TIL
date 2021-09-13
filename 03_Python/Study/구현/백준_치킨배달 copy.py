# 백준 15686번 치킨배달
from sys import stdin
from collections import deque
from itertools import combinations
input = stdin.readline
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            chicken.append([i, j])
        elif matrix[i][j] == 1:
            home.append([i, j])

arr = list(combinations(chicken, m))   # 최대 보유할 수 있는 치킨집의 개수(m)만큼의 조합
final = int(1e9)
while arr:
    distance = [int(1e9)] * len(home)  # 각 1(집)에대한 2(치킨집)까지의 거리 
    now = arr.pop()
    for x in now:
        for i in range(len(home)):
            absolute = abs(home[i][0] - x[0]) + abs(home[i][1] - x[1])
            if distance[i] > absolute:
                distance[i] = absolute
    if final > sum(distance):
        final = sum(distance)
print(final)