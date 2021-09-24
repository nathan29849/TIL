# 백준 14502번 연구소
from sys import stdin
from itertools import combinations
from collections import deque
import copy
input = stdin.readline

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(start, c, n, m, temp_matrix, answer):
    global dx
    global dy
    count = c
    q = copy.deepcopy(start)
    # visited = [i for i in start] 이걸 할 필요가 없었음 (애초에 0인 곳만 가니까) - 시간초과의 원인
    while q:
        now = q.popleft()
        for i in range(4):
            next_x = now[0]+dx[i]
            next_y = now[1]+dy[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                # if (next_x, next_y) not in visited: # 미방문
                if temp_matrix[next_x][next_y] == 0: # 바이러스 퍼질 수 있는 곳
                    temp_matrix[next_x][next_y] = 2
                    # visited.append((next_x, next_y))
                    q.append((next_x, next_y))
                    count += 1
                    if count >= answer:
                        return False
    return count
        
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
box = []
two = deque()
one = 3 # 결과적으로 벽을 세 개 세우게 되므로 
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            two.append((i, j))
        elif matrix[i][j] == 1:
            one += 1
        else:
            box.append((i, j))
        
c = len(two)   # 2가 속한 영역
comb = list(combinations(box, 3))
answer = int(1e9)
for test in comb:
    temp = copy.deepcopy(matrix)
    for t in test:
        temp[t[0]][t[1]] = 1
    result = bfs(two, c, n, m, temp, answer)
    if result:
        answer = min(answer, result)

answer = n*m - one - answer
print(answer)