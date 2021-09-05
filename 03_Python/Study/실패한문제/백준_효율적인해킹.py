# 백준 1325번 효율적인 해킹
from sys import stdin
from collections import deque
input = stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    v, w = map(int, input().split())
    graph[w].append(v)
final = [0] * (n+1)
for j in range(1, n+1):
    if len(graph[j]) > 0:
        count = 0
        visited = [False]*(n+1)
        visited[j] = True
        arr = deque([j])
        while arr:
            now = arr.popleft()
            for x in graph[now]:
                if visited[x] == False:
                    visited[x] = True
                    count += 1
                    arr.append(x)
        
        final[j] = count
result = 0
result_arr = []
for k in range(1, n+1):
    if result < final[k]:
        result = final[k]
        result_arr = [k]
    elif result == final[k]:
        result_arr.append(k)
    else:
        pass

print(" ".join(map(str, result_arr)))



