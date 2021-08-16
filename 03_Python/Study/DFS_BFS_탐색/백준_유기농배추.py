# 백준 1012번 (DFS)
import sys
sys.setrecursionlimit(10**6)

def solution(n, m, maze):
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m, maze) == True:
                result += 1
    return result


def dfs(x, y, n, m, maze):
    if 0 <= x < n and 0 <= y < m:
        if maze[x][y] == 1:
            maze[x][y] = 0

            dfs(x-1, y, n, m, maze)
            dfs(x, y-1, n, m, maze)
            dfs(x+1, y, n, m, maze)
            dfs(x, y+1, n, m, maze)
            return True
        else:
            return False
    else:
        return False


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