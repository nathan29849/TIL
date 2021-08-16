# 백준 1922번 네트워크 연결 (Prim)
from sys import stdin
import heapq

input = stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a)) # 양방향 연결이므로 양쪽 노드 다 해줘야 함!

def prim(graph, start):
    edge_cnt = -1
    visited = [False] * (n+1)
    queue = []
    heapq.heappush(queue, (0, start))
    total_weight = 0

    while edge_cnt < n-1:
        if not queue:
            return False
        weight, node = heapq.heappop(queue)
        if visited[node] != True:
            edge_cnt += 1
            visited[node] = True
            total_weight += weight
            for x in graph[node]:
                heapq.heappush(queue, (x[0], x[1]))
            # print(weight, queue)
    return total_weight

print(prim(graph, 1))       
# min_weight = int(1e9)     # greedy 알고리즘... 모든 노드에서 동일하게 값(최적해)이 나온다.
# for i in range(1, n+1):
#     w = prim(graph, i)
#     print(w)
#     if min_weight > w:
#         min_weight = w
# print(min_weight)

