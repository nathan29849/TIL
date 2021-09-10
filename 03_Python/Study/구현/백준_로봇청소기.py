# 백준 14503번 로봇 청소기
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

q = deque()
q.append([r, c, d])
# 방향       0: 북, 1: 동, 2: 남, 3: 서
# 방향의 왼쪽 0: 서, 1: 남, 2: 동, 3: 북
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

# 후진
    # 북 동 남 서
bx = [+1, 0, -1, 0]
by = [0, -1, 0, +1]
count = 1
matrix[r][c] = 2        # 로봇 청소기가 있는 칸의 상태는 항상 빈칸이다. 

def clean(R, C, D):
    global count
    global q
    for i in range(D+3, D-1, -1):
        new_D = i%4
        new_R, new_C = R+dx[new_D], C+dy[new_D]
        if matrix[new_R][new_C] == 0:
            count += 1
            matrix[new_R][new_C] = 2 # 청소 완료
            q.append([new_R, new_C, new_D])
            return False
    return new_R, new_C, new_D

while q:
    flag = True
    R, C, D = q.popleft()
    result = clean(R, C, D)
    if result != False:
        if matrix[R+bx[D]][C+by[D]] == 1:   # 후진 시 벽이 아니라면
            break    
        else:
            q.append([R+bx[D], C+by[D], D])
            # clean(R+bx[D], C+by[D], D)
print(count)
# print(matrix)