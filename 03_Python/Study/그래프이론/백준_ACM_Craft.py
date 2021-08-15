# 백준 1005번 ACM Craft 
from sys import stdin
from collections import deque

input = stdin.readline

def topology_sort(n, indegree, costs, graph, w):
    q = deque()
    result = []
    temp_costs = [0]*(n)

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
                temp = costs[j-1] + costs[now-1]
                if temp_costs[j-1] > temp:
                    costs[j-1] = temp_costs[j-1]
                else:
                    costs[j-1] += costs[now-1]
                # print("indegree :", indegree)
                # print("costs : ", costs)
            else:
                # 진입분지수가 0이 되지 않았을 때, 비용이 더 클 수 있는 점을 고려
                if temp_costs[j-1] < costs[j-1] + costs[now-1]:
                    temp_costs[j-1] = costs[j-1] + costs[now-1]
    
    return costs[w-1]

t = int(input())
answer = []
for _ in range(t):
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    graph = [[]for _ in range(n+1)]
    indegree = [0] * (n+1)
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    answer.append(topology_sort(n, indegree, costs, graph, w))


for i in range(t):
    print(answer[i])