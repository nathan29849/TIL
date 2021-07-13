# 백준 1260번
from collections import deque
from sys import stdin
import heapq


class Graph:
    def __init__(self, size):
        self.size = size                                        # 주어진 노드의 개수  
        self.adjList = list([] for _ in range(size+1))            # list of lists (1부터 시작하므로)
        self.visited = [False] * (size+1)

    def insertEdge(self, v1, v2):
        # 양방향 연결
        # heapq.heapify(self.adjList[v1])
        # heapq.heappush(self.adjList[v1], v2)
        # heapq.heapify(self.adjList[v2])
        # heapq.heappush(self.adjList[v2], v1)  => 오답 나옴.. 잘 고치면 되긴 할듯?
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

    def dfs(self, start):
        for i in range(len(self.adjList)):
            self.adjList[i].sort()                              # 정렬을 꼭 해줘야 함.. 그래야 번호 낮은 순서대로 탐색 가능(이거 최소힙 써도 될듯?)

        self.visited[start] = True
        print(start, end=" ")

        for i in range(len(self.adjList[start])):
            v = self.adjList[start][i]
            if self.visited[v] == False:
                self.dfs(v)

    def bfs(self, start):
        queue = deque()
        visit = [False] * (self.size+1)
        visit[start] = True
        queue.append(start)
        
        while queue:
            v = queue.popleft()
            print(v, end=" ")

            for i in range(len(self.adjList[v])):
                w = self.adjList[v][i]
                if visit[w] == False:
                    visit[w] = True
                    queue.append(w)
        


n, m, start = map(int, stdin.readline().split())
g = Graph(n)
for i in range(m):
    v1, v2 = map(int, stdin.readline().split())
    g.insertEdge(v1, v2)

g.dfs(start)
print()
g.bfs(start)