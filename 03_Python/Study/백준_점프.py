# 백준 1890번 점프(메모리 초과)
from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
start = (0, 0)
q = deque([start])
dx = [+1, 0]
dy = [0, +1]
count = 0
visited = []
while q:
    now_x, now_y = q.pop()
    if now_x == n-1 and now_y == n-1:
        count += 1
        visited = []
    else:
        if (now_x, now_y) not in visited:
            visited.append((now_x, now_y))
            now = matrix[now_x][now_y]
            for i in range(2):
                temp_x = now_x + dx[i]*now
                temp_y = now_y + dy[i]*now
                if 0 <= temp_x < n and 0 <= temp_y < n:
                    q.append((temp_x, temp_y))
print(count)