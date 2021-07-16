# 이코테 - 음료수 얼려먹기 (DFS, BFS 탐색)
from sys import stdin
from collections import deque

# BFS로 했음
def solution(n, m, matrix, visited):
    answer = 0
    queue = deque()
    dx = [0, -1, 0, +1]
    dy = [+1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "0" and visited[i][j] == False:
                answer += 1  
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for z in range(4):
                        if 0 <= x+dx[z] < n and 0 <= y+dy[z] < m:
                            if matrix[x+dx[z]][y+dy[z]] == "0" and visited[x+dx[z]][y+dy[z]] == False:
                                visited[x+dx[z]][y+dy[z]] = True
                                queue.append((x+dx[z], y+dy[z]))
    return answer


n, m = map(int, stdin.readline().split())
matrix = []
visited = []
for i in range(n):
    matrix.append(input())
    visited.append(list(False for i in range(m)))
# print(matrix)
print(solution(n, m, matrix, visited))

# 4 5
# 00110
# 00011
# 11111
# 00000


# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# 4 5
# 01010
# 10101
# 01010
# 10101