# 백준 1976번 여행가자 
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
n = int(input())    # 도시 수
m = int(input())    # 여행이 계획된 도시 수
parent = [0] * (n+1)
for k in range(1, n+1):
    parent[k] = k


matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

travel = list(map(int, input().split()))

# union
for i in range(n):
    for j in range(n):  
        # 처음 범위를 for j in range(i)라고 했을 때 안됐던 이유
        # A->B의 연결은 표시됐으나, B->A 연결이 표시되지 않는 경우가 있는 것으로 판단.
        if matrix[i][j] == 1:
            union_parent(parent, i+1, j+1)

root = parent[travel[0]]
# print(parent)
# print(travel)
flag = True
for t in travel:
    if parent[t] != root:
        flag = False
        break
    
print("YES") if flag else print("NO")

# 5
# 3
# 0 1 0 1 0
# 1 0 0 0 0
# 0 0 0 0 0
# 1 0 0 0 0
# 0 0 0 0 0
# 1 4 2