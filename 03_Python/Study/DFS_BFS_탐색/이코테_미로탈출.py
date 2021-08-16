 # 이코테 - 음료수 얼려먹기 (DFS, BFS 탐색)
from sys import stdin
from collections import deque

def solution(n, m, maze, dist):
    answer = 0
    cur = (0, 0)
    dx = [0, -1, 0, +1]
    dy = [+1, 0, -1, 0]
    visited[cur[0]][cur[1]] = True
    queue = deque([cur])
    dist[cur[0]][cur[1]] = 1
    while queue:
        v = queue.popleft()
        if v[0] == n-1 and v[1] == m-1:
            return dist[v[0]][v[1]]

        # if link > 1:
        #     answer -= link-1

        # link = 0
        for i in range(4):
            if 0 <= v[0]+dx[i] < n and 0 <= v[1]+dy[i] < m:
                temp = (v[0]+dx[i], v[1]+dy[i])
                if visited[temp[0]][temp[1]] == False and maze[temp[0]][temp[1]] == "1":
                    queue.append(temp)
                    visited[temp[0]][temp[1]] = True
                    dist[temp[0]][temp[1]] = dist[v[0]][v[1]] + 1
                    
n, m = map(int, stdin.readline().split())
maze = []
visited = []
dist = []
for i in range(n):
    maze.append(input())
    visited.append(list(False for _ in range(m)))
    dist.append(list(0 for _ in range(m)))


print(solution(n, m, maze, dist))