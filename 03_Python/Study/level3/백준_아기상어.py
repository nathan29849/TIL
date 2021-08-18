# 백준 16236번 아기상어 (그래프 탐색(BFS), 구현)
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

def solution(n, matrix):
    level = 2               # 아기 상어의 크기
    start = (0, 0)          # 시작점(9)의 위치
    time = 0                # 걸리는 시간
    feed = 0                # 먹은 물고기(레벨업시 초기화됨)
    q = deque()             # 아기상어가 먹을 수 있는 상어의 위치
    for i in range(n):      # 상어 위치 찾기
        for j in range(n):
            if matrix[i][j] == 9:
                start = (i, j)
    q.append(start)       

    while q:
        now_start = q.popleft()
        result = bfs(n, matrix, now_start, level, feed) 
        if result != False:
            row, col, dist, feed, level = result
            q.append((row, col))
            time += dist
        else:
            break

    return time



INF = int(1e9)

def bfs(n, matrix, start, level, feed):
    queue =deque()
    distance = [([0]*n)for _ in range(n)]
    visited = [([False]*n)for _ in range(n)]
    queue.append(start)
    visited[start[0]][start[1]] = True
    matrix[start[0]][start[1]] = 0
    result = []
    dist = 0
            # 상 좌 하 우
    dx = [-1, 0, 0, +1] 
    dy = [0, -1, +1, 0]
    while queue:
        now = queue.popleft()
        # dist += 1
        for i in range(4):
            row = now[0]+dx[i]
            col = now[1]+dy[i]
            # 행렬 범위 내에 있는지 우선 확인
            if 0 <= row < n and 0<= col < n: 
                if matrix[row][col] <= level and visited[row][col] == False:   # 지나갈 수 있는 곳
                    if matrix[row][col] < level and matrix[row][col] != 0:  # 먹을 수 있는 곳
                        feed += 1
                        if feed == level:       # level up
                            level += 1
                            feed = 0            # 초기화
                        dist = distance[now[0]][now[1]] + 1
                        return (row, col, dist, feed, level)
                    else:                       # 지나갈 수는 있으나 먹을 수는 없는 곳
                        queue.append((row, col))
                        visited[row][col] = True
                        distance[row][col] = distance[now[0]][now[1]] + 1

                else:                           # 지나갈 수 없는 곳
                    pass
    return False


print(solution(n, matrix))