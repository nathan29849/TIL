# 백준 4386번 별자리 만들기
from sys import stdin
import math
from heapq import heappush, heappop, heapify
input = stdin.readline
INF = int(1e9)
result = 0
n = int(input())
coo = []
parents = [i for i in range(n)]
for i in range(n):
    coo.append(tuple(map(float, input().split())))
indegree = []     # 진입분지수 
results = []
for i in range(n):
    for j in range(i+1, n):
        dist = round(math.sqrt((coo[i][0] - coo[j][0])**2 + (coo[i][1] - coo[j][1])**2), 2)
        heappush(indegree, (dist, i, j))   # (거리, 온 노드의 번호)


def find(a, parents):
    if parents[a] != a:
        parents[a] = find(parents[a], parents)
    return parents[a]

def union(a, b, parents):    
    a = find(a, parents)
    b = find(b, parents)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

while indegree:
    dist, a, b = heappop(indegree)
    if find(a, parents) != find(b, parents):
        union(a, b, parents)
        result += dist

print(round(result, 2))
