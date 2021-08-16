from sys import stdin
import heapq
input = stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]   # 노드 번호를 그대로 인덱스로 쓰기 위함
# visited = [False] * (n+1) 굳이 필요 없음 - distance가 역할 대체
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

queue = []
heapq.heapify(queue)

def dijkstra(start, queue):
    heapq.heappush(queue, (0, start)) # (거리, 노드)
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:   # 이미 방문한 노드라면 continue
            continue
        else:
            for x in graph[node]:
                cost = dist + x[1]
                if cost < distance[x[0]]:
                    distance[x[0]] = cost
                    heapq.heappush(queue, (cost, x[0]))

    return distance

print(dijkstra(start, queue))

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2