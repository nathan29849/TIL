# 백준 2206번 벽 부수고 이동하기
from sys import stdin
from collections import deque
import copy
input = stdin.readline

# n, m, matrix 입력받기
n, m = map(int, input().split())
matrix = []
one = []
final_one = []
for i in range(n):
    string = input().rstrip()
    temp = []
    for j in range(len(string)):
        s = int(string[j])
        temp.append(s)
        if s == 1:
            one.append((i, j))
    matrix.append(temp)

# 동 남 서 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
start = (0, 0, 0)   # x = 0, y = 0, d = 1, crash = 0
def bfs(start):
    answer = int(1e9)
    global matrix
    # global visited
    visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
    print(visited)
    
    visited[0][0][0] = 1
    q = deque([start])
    while q:
        x, y, crash= q.popleft()
        if x == n-1 and y == m-1:
            answer = min(answer, visited[x][y][crash])               
            return answer
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and visited[nx][ny][crash] == 0:
                    q.append((nx, ny, crash))
                    visited[nx][ny][crash] = visited[x][y][crash] + 1
                elif matrix[nx][ny] == 1 and crash == 0: 
                    q.append((nx, ny, crash+1))
                    visited[nx][ny][crash+1] = visited[x][y][crash] + 1   
    return False

result = bfs(start)
if result:
    print(result)
else:
    print(-1)


# 8 8
# 01000100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 00010100

# 1 1
# 0