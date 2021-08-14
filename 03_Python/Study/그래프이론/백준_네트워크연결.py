# 백준 1922번 네트워크 연결 (Kruskal)
from sys import stdin

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


input = stdin.readline

n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

arr = []
result = 0
for i in range(m):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))
arr.sort() # sort를 꼭 해줘야 한다 - 그래야 최소 값부터 find & union을 하니까
for x in arr:
    c, a, b = x
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
print(result)