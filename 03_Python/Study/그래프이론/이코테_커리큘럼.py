# 이코테 실전 4번 커리큘럼 (그래프 이론)
from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
weight = [0] * (n+1)

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(len(temp)-1):
        if j == 0:
            weight[i] = temp[j]
        else:
            graph[temp[j]].append(i)    # 그래프에 노드 추가
            indegree[i] += 1
print("graph :", graph)
print("indegree :", indegree)
print("weight :", weight)
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                weight[i] += weight[now]
                q.append(i)
    
    if len(result) != n:
        return False
    else:
        return True

if topology_sort() == True:
    for i in range(1, n+1):
        print(weight[i])


# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1