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

# 가능성 있는 벽 추려내기 ( 상하좌우를 살펴서 부수는게 의미가 있을 벽들 골라내기 )
for ox, oy in one:
    null_ctx = 0
    wall_ctx = 0
    for i in range(4):
        nx = ox + dx[i]
        ny = oy + dy[i]
        if 0<= nx < n and 0<= ny < m:
            if matrix[nx][ny] == 1:
                wall_ctx += 1
        else:
            null_ctx += 1
    if wall_ctx >= 3 or (wall_ctx == 2 and null_ctx >= 1) or (wall_ctx == 1 and null_ctx == 2):
        continue
    else:
        final_one.append((ox, oy))



start = (0, 0, 1)   # 0,0에서 출발
answer = int(1e9)

def bfs(start, matrix):
    q = deque([start])
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            x += dx[i]
            y += dy[i]
            if 0<= x < n and 0<= y < m:
                if matrix[x][y] == 0:
                    if x == n-1 and y == m-1:   # 목적지 도착시                                                
                        return True
                    else:
                        q.append((x, y, d+1))
                        matrix[x][y] = 2
            x -= dx[i]
            y -= dy[i]
    return False

# 그냥 벽을 안 없앨 때
result = bfs(start, copy.deepcopy(matrix))
if result:
    answer = result

# print(final_one)
# 벽 하나 제외시키는 경우
flag = False
for ox, oy in final_one:
    temp_matrix = copy.deepcopy(matrix)
    temp_matrix[ox][oy] = 0
    result = bfs(start, temp_matrix)
    if result:
        flag = True

if flag:
    print(answer)
else:
    print(-1)


