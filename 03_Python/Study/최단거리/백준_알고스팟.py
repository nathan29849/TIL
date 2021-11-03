# 백준 1261번 알고스팟
from sys import stdin
from collections import deque
from heapq import heappop, heappush, heapify
input = stdin.readline

n, m = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append(input().rstrip())

visited= [[False]*n for _ in range(m)]
# print(matrix)

# q = deque([(0,0,0)]) #(r, c, crash)
q = [(0, 0, 0)] # (crash, r, c)
heapify(q)
visited[0][0] = True
# 동, 남, 서, 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
while q:
    crash, r, c = heappop(q)
    if r == n-1 and c == m-1:
        print(crash)
        break
    for i in range(4):
        new_r = r + dx[i]
        new_c = c + dy[i]
        if 0 <= new_r < n and 0 <= new_c < m:   # 범위 확인
            if visited[new_c][new_r] == False:  # 방문 여부 확인
                visited[new_c][new_r] = True
                if matrix[new_c][new_r] == "0":
                    heappush(q, (crash, new_r, new_c))
                else:
                    heappush(q, (crash+1, new_r, new_c))
    
        
