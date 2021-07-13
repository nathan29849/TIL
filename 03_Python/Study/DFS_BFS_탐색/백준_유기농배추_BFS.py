# 백준 1012번 (BFS)
import sys
from collections import deque

def solution(n, m, maze):
    result = 0
    queue = deque()
    # queue.append((0,0))

    dx = [0, -1, 0, +1]
    dy = [+1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: # 1이면 ~
                queue.append((i, j))
                maze[i][j] = 0  # 방문
                result += 1
                while queue:
                    col, row = queue.popleft()
                    for k in range(4):
                        temp = (col+dx[k], row+dy[k])
                        if 0 <= temp[0] < n and 0 <= temp[1] < m:
                            if maze[temp[0]][temp[1]] == 1:
                                queue.append(temp)
                                maze[temp[0]][temp[1]] = 0

    return result

t = int(sys.stdin.readline())
answer = []
for i in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    maze = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        col, row = map(int, sys.stdin.readline().split())
        maze[col][row] = 1
    answer.append(solution(n, m, maze))

for i in range(len(answer)):
    print(answer[i])