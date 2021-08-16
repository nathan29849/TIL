# 백준 2252번 줄 세우기
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int ,input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1    # 진입분지수 추가

def topology_sort():
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for x in graph[now]:
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)
    
    for i in range(n):
        print(result[i], end=" ")
    
topology_sort()