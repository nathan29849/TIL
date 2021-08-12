# 백준 11404번 플로이드 (최단 경로)
from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    if graph[a][b] > w:
        graph[a][b] = w

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=" ")
    print()
