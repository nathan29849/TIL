# 이코테 실전문제 2번 미래도시(최단거리) - 플로이드 워셜로 풀기 (범위가 100이내)
from sys import stdin
import heapq
input = stdin.readline


# n : 회사 개수, m : 경로 개수
n, m = map(int, input().split())
INF = int(1e9)
matrix = [[INF]*(n+1)for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

dest, k = map(int, input().split())

# 자기 자신으로 가는 길 : 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            matrix[a][b] = 0

# 경유해서 가는 길 matrix에 적용하기
for l in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            matrix[a][b] = min(matrix[a][b], matrix[a][l]+matrix[l][b])

# 1 -> k -> dest
result = matrix[1][k] + matrix[k][dest]
if result >= INF:
    print("-1")
else:
    print(result)

# 5 7             
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
