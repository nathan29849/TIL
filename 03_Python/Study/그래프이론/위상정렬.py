# 위상정렬 소스코드
from  collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    print(indegree)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        
    if len(result) == v:
        for i in result:
            print(i, end=" ")
        return True
    else:
        return False

print(topology_sort())

# 7 7
# 1 2
# 1 5
# 2 3
# 3 4
# 4 7
# 6 4
# 7 6