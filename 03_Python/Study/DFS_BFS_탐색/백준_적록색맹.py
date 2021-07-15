# 백준 10026번
from sys import stdin
from collections import deque

def solution(n, matrix, visited):
    queue = deque()
    count = 0
    rgb_count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                queue.append((i, j))
                visited[i][j] = True
                bfs(queue, matrix, visited)
                count += 1
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                queue.append((i, j))
                rgb(queue, matrix, visited)
                rgb_count += 1
    
    print(count, end=" ")
    return rgb_count




def bfs(queue, matrix, visited):
    dx = [0, -1, 0, +1]
    dy = [+1, 0, -1, 0]
    while queue:
        col, row = queue.popleft()
        cur = matrix[col][row]
        if cur == 'G':
            matrix[col][row] = 'R'
        for i in range(4):
            temp_col = col+dx[i]
            temp_row = row+dy[i]
            if 0 <= temp_col < n and 0 <= temp_row < n:
                if matrix[temp_col][temp_row] == cur and visited[temp_col][temp_row] == False:
                    visited[temp_col][temp_row] = True
                    queue.append((temp_col, temp_row))
    return 

def rgb(queue, matrix, visited):
    dx = [0, -1, 0, +1]
    dy = [+1, 0, -1, 0]
    while queue:
        col, row = queue.popleft()
        cur = matrix[col][row]
        for i in range(4):
            temp_col = col+dx[i]
            temp_row = row+dy[i]
            if 0 <= temp_col < n and 0 <= temp_row < n:
                if matrix[temp_col][temp_row] == cur and visited[temp_col][temp_row] == True:
                    visited[temp_col][temp_row] = False
                    queue.append((temp_col, temp_row))
    return 







n = int(stdin.readline())
matrix = []
visited = []
for i in range(n):
    matrix.append(list(stdin.readline()))
    visited.append([False for _ in range(n)])

print(solution(n, matrix, visited))