# 백준 1717번 집합의 표현
import sys
sys.setrecursionlimit(10**6)
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

input = sys.stdin.readline
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

answer = []
for j in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_parent(parent, a, b)
    else:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            answer.append("YES")
        else:
            answer.append("NO")


for x in answer:
    print(x)