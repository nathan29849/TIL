# 이코테 실전문제 3번 전보(최단거리) - 다익스트라로 풀기
from sys import stdin
import heapq

def solution(n, m, c, graph):
    INF = int(1e9)
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, c))
    distance = [INF] * (n+1)

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        else:
            for x in graph[node]:
                cost = dist + x[1]
                if cost < distance[x[0]]:
                    distance[x[0]] = cost
                    heapq.heappush(queue, (cost, x[0]))
    
    count = 0
    maxNum = 0
    for i in range(1, n+1):
        if distance[i] == INF:
            continue
        else:
            count += 1
            if distance[i] > maxNum:
                maxNum = distance[i]
    
    return count, maxNum
        

input = stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    # x -> y (시간 : z)
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

result1, result2 = solution(n, m, c, graph)
print(result1, result2)

