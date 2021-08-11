# 백준 1916번 최소 비용 구하기
from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start, end = map(int, input().split())
distance = [INF] * (n+1)

def solution(n, graph, distance, start, end):
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for x in graph[node]:
            cost = dist + x[1]
            if distance[x[0]] > cost:
                distance[x[0]] = cost
                heapq.heappush(queue, (cost, x[0]))
    return distance[end]

print(solution(n, graph, distance, start, end))