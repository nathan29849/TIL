# 백준 1753 최단경로
from sys import stdin
import heapq

input = stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

INF = int(1e9)
distance = [INF] * (v+1)

def solution(v, k, graph, distance):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, k))
    distance[k] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for x in graph[node]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(queue, (cost, x[0]))

solution(v, k, graph, distance)

for i in range(1, v+1):
    if distance[i] >= INF:
        print("INF")
    else:
        print(distance[i])