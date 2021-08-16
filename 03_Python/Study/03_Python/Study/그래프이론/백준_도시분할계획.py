# 백준 1647번 도시 분할 계획
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
 
edges = []
result = 0
count = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if count == n-2:    # 두 도시로 분할하면 되므로, 간선의 개수가 n-2개가 될 때 멈춘다.ㄴ
        print(result)
        break
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        count += 1
        result += cost

    