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


def bfs(n, matrix, start, level):
    queue = []
    visited = [([False]*n) for _ in range(n)]
    dist = 0
    feed = 0
    answer = 0
    heapq.heappush(queue, (dist, start[0], start[1])) # 거리, 행, 열 순
    matrix[start[0]][start[1]] = 0
    
            # 상 좌 우 하
    dx = [-1, 0, 0, +1] 
    dy = [0, -1, +1, 0]
    while queue:
        dist, row, col = heapq.heappop(queue)   
        # visited[row][col] = True                                 
        if 0 < matrix[row][col] < level:     # 먹을 수 있는 길인지 확인
            # 초기화
            queue = []
            matrix[row][col] = 0
            visited = [([False]*n) for _ in range(n)]
            answer += dist
            dist = 0

            feed += 1
            if feed == level:
                level += 1
                feed = 0
        # else:
        #     visited[row][col] = True          여기에 이 코드를 넣으면 시간초과가 뜹니다.      
                
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]

            if 0<= x < n and 0<= y < n:
                if visited[x][y] == False:
                    if matrix[x][y] <= level:
                        visited[x][y] = True
                        heapq.heappush(queue, (dist+1, x, y))
    
    return answer



print(solution(n, matrix))

# 20
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 9
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
