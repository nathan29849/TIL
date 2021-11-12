# 백준 6497번 전력난
from sys import stdin
from heapq import heappush, heappop, heapify
input = stdin.readline

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

def solution(edges, sum_number, parents):
    result = 0
    while edges:
        dist, start, dest = heappop(edges)
        if find(start, parents) != find(dest, parents):
        # if parents[start] != parents[dest]:   
        # # 이게 안되는 이유는 union할 때마다 parents 노드 전체가 다 update가 되는 것이 아니기 때문
            union(start, dest, parents)
            result += dist

    print(sum_number-result)

while True:
    edges = []
    sum_number = 0
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    else:
        for i in range(n):
            start, dest, dist = list(map(int, input().split()))
            sum_number += dist
            heappush(edges, (dist, start, dest))
        parents = [0] * m
        for i in range(m):  # parents 초기화
            parents[i] = i            
        solution(edges, sum_number, parents)       