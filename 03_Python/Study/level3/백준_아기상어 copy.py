# 백준 16236번 아기상어 (그래프 탐색(BFS), 구현)
from sys import stdin
import heapq
input = stdin.readline

n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

def solution(n, matrix):
    level = 2               # 아기 상어의 크기
    start = (0, 0)          # 시작점(9)의 위치
    for i in range(n):      # 상어 위치 찾기
        for j in range(n):
            if matrix[i][j] == 9:
                start = (i, j)
    

    result = bfs(n, matrix, start, level) 

    return result



INF = int(1e9)

def bfs(n, matrix, start, level):
    queue = []
    visited = [([False]*n)for _ in range(n)]
    start_x, start_y = start
    dist = 0
    feed = 0
    answer = 0
    heapq.heappush(queue, (dist, start_x, start_y)) # 거리, 행, 열 순
    matrix[start_x][start_y] = 0
    
            # 상 좌 우 하
    dx = [-1, 0, 0, +1] 
    dy = [0, -1, +1, 0]

    # 우선순위 : 거리 > 위(행) > 왼쪽(열)
    while queue:
        # print(queue)
        now = heapq.heappop(queue)  # (거리, 행, 열)
        visited[now[1]][now[2]] = True
        for i in range(4):
            row = now[1]+dx[i]
            col = now[2]+dy[i]
            # 행렬 범위 내에 있는지 우선 확인
            if 0 <= row < n and 0<= col < n: 
                if matrix[row][col] <= level and visited[row][col] == False:   # 지나갈 수 있는 곳
                    if matrix[row][col] < level and matrix[row][col] != 0:  # 먹을 수 있는 곳
                        queue = []
                        matrix[row][col] = 0
                        feed += 1
                        print(row, col)
                        if feed == level:       # level up
                            level += 1
                            feed = 0            # 초기화
                        answer += now[0] + 1
                        dist = 0
                        visited = [([False]*n)for _ in range(n)]
                    else:
                        dist = now[0] + 1
                        visited[row][col] = True
                    heapq.heappush(queue, (dist, row, col))
    return answer


print(solution(n, matrix))