# 백준 18352번 특정거리의 도시 찾기(최단거리)
from sys import stdin
import heapq
def solution(n, m, k, x, graph):
    INF = int(1e9)
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (0, x))
    distance = [INF] * (n+1)
    distance[x] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        cost = dist + 1
        for i in graph[node]:
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(queue, (cost, i))
    
    answer = []
    for j in range(1, n+1):
        if distance[j] == k:
            answer.append(j)
            
    if len(answer) == 0:
        answer.append(-1)
    return answer


input = stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    # a -> b
    a, b = map(int, input().split())
    graph[a].append(b)    
result = solution(n, m, k, x, graph)

for i in result:
    print(i)