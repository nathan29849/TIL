# 백준 1520번 내리막 길
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
m, n = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))

count = 0

# 동 남 서 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
dp = [[-1]*n for _ in range(m)]
dp[0][0] = 1
def dfs(x, y):
    global count
    global matrix
    global dp
    now = matrix[x][y]
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:      # 핵심 dp 초기값을 0으로 두고 시작해버리면 겹치는 부분이 많아짐 
        dp[x][y] += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                temp = matrix[nx][ny]
                if temp > now:    # 더 낮은 계단칸
                    dp[x][y] += dfs(nx, ny)
    # 이미 방문이 되었다면, dp값을 그대로 return
    return dp[x][y]


result = dfs(m-1, n-1)
# print(dp)
print(result)
            

# 4 4
# 20 16 12 7
# 13 12 11 7
# 10 11 7 6
# 5 8 7 5

# [[1,  1, 1, -1],
#  [1,  2, 3,  3],
#  [-1, 2, 5,  8],
#  [-1, 2, 2, 10]]

# [[1, 6, 10, 0],
# [4, 21, 47, 47],
# [0, 8, 24, 71],
# [0, 2, 2, 73]] 