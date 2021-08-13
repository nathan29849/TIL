# 이코테 실전2번 팀결성 (그래프 이론 - 서로소 집합)
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
n, m = map(int, input().split())
parent = [0] * (n+1)
for k in range(n+1):
    parent[k] = k
answer = []
for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union_parent(parent, a, b)
    else:   # cal == 2
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            answer.append("YES")
        else:
            answer.append("NO")

for x in answer:
    print(x)

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1