# 백준 1956번 운동
# 사이클 찾기(최소비용)
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

v, e = map(int, input().split())
matrix = [{} for _ in range(v)]
# matrix = [[] for _ in range(v)]

for i in range(e):
    a, b, c = map(int, input().split())
    # dictionary add key가 list append 보다 시간이 덜 걸리는 듯 
    matrix[a-1][b-1] = c      
    # matrix[a-1].append((b-1, c))

result = int(1e9)
for start in range(v):
    distance = [int(1e9)]*v
    q = []
    for next, dist in matrix[start].items():
    # for next, dist in matrix[start]:
        distance[next] = dist
        heappush(q, (distance[next], next))
    while q:
        dist, now = heappop(q) 
        if now == start:    # 목적지 도달시 while 탈출
            break

        if distance[now] < dist: # 이미 거리 계산이 되어있는 것이 짧으면 더이상 계산할 필요 없음
            continue

        for next, next_dist in matrix[now].items():
        # for next, next_dist in matrix[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                heappush(q, (cost, next))
    result = min(distance[start], result)
        
print(result if result != int(1e9) else -1)
