# 백준 1238번 파티 (최단 경로)
from sys import stdin
import heapq


input = stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))


def solution(graph, n, x):
    queue = []
    maxTime = [0] * (n+1)
    INF = int(1e9)
    
    distance_x = []
    for start in range(1, n+1):
        distance = [INF] * (n+1)
        heapq.heappush(queue, (0, start))
        distance[start] = 0

        while queue:
            dist, node = heapq.heappop(queue)
            if distance[node] < dist:
                continue
            
            for c in graph[node]:
                cost = dist + c[1]
                if distance[c[0]] > cost:
                    distance[c[0]] = cost
                    heapq.heappush(queue, (cost, c[0]))


        if start != x:  # 도착지점이 출발점이 아닌 경우 ~ start에서 x까지 가는 최단 경로
            maxTime[start] = distance[x]
        else:   # start == x : 도착지점이 출발점인 경우 ~ x에서 start까지 가는 최단 경로
            distance_x = distance

    for i in range(1, n+1):
        maxTime[i] += distance_x[i]

    return max(maxTime)

print(solution(graph, n, x))