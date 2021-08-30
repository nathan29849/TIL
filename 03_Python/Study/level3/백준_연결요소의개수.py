# 백준 11724번 연결 요소의 개수
from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        q = deque()
        q.append(i)
        visited[i] = True
        while q:
            now = q.popleft()
            for x in graph[now]:
                if visited[x] == False:
                    visited[x] = True
                    q.append(x)
        count += 1

print(count)