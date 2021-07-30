# 백준 1939번
from sys import stdin
import sys
from collections import deque
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self, size):
        self.adjList = [None] * (size+1) # 0은 없으므로
        self.adjList2 = [[] for _ in range(size+1)]
        self.size = size+1

    def insertEdge(self, v1, v2, w):    # linked list
        newNode = Node(v2, w)
        newNode.next = self.adjList[v1]
        self.adjList[v1] = newNode

        newNode = Node(v1, w)
        newNode.next = self.adjList[v2]
        self.adjList[v2] = newNode

    def bfs(self, start, dest, box_weight):
        visited = [False] * (self.size+1)
        queue = deque([start])
        visited[start] = True

        while queue:
            w = queue.popleft()
            if w == dest:
                return True
            node = self.adjList[w]
            while node is not None:
                if visited[node.vertex] == False and node.weight >= box_weight:
                    visited[node.vertex] == True
                    queue.append(node.vertex)
                node = node.next
        return False

    def insertEdge2(self, v1, v2, w):   # list of lists
        self.adjList2[v1].append((v2, w))
        self.adjList2[v2].append((v1, w))

    def bfs2(self, start, dest, box_weight):
        visited = [False] * (self.size+1)
        queue = deque([start])
        visited[start] = True
        while queue:
            w = queue.popleft()
            if w == dest:
                return True
            for vertex, weight in self.adjList2[w]:
                if visited[vertex] == False and weight >= box_weight:
                    visited[vertex] = True
                    queue.append(vertex)
        return False


    def findFactory(self, start, dest, max_weight):
        left = 1
        right = max_weight
        answer = 0
        while left <= right:
            mid = (left+right)//2
            if self.bfs2(start, dest, mid) == True:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer


n, m = map(int, stdin.readline().split())
g = Graph(n)
max_weight = 0
for _ in range(m):
    v1, v2, w = map(int, stdin.readline().split())
    if max_weight < w:      # 중량 최댓값 구하기
        max_weight = w
    g.insertEdge2(v1, v2, w)

f1, f2 = map(int, stdin.readline().split())
result = g.findFactory(f1, f2, max_weight)
print(result)