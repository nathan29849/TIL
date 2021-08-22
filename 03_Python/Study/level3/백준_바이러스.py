# 백준 2606번 바이러스
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
edges = int(input())
graph = [[] for _ in range(n+1)]
for i in range(edges):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)


def solution(n, graph):
    visited = [False] * (n+1)
    start = 1
    queue =deque([start])
    count = 0
    visited[start] = True
    while queue:
        now = queue.popleft()
        for x in graph[now]:
            if visited[x] == False:
                queue.append(x)
                visited[x] = True
                count += 1
    return count

print(solution(n, graph))
