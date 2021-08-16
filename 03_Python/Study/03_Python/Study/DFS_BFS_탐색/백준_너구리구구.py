# 백준 18126번
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
f = stdin.readline

class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self, size):
        self.size = size
        self.adjList = [None] * (size+1)    # 1부터 시작하므로
        self.visited = [False] * (size+1)
        self.dist = [0] * (size+1)

    def insertEdge(self, v1, v2, w):
        newNode = Node(v2, w)
        newNode.next = self.adjList[v1]
        self.adjList[v1] = newNode

        newNode = Node(v1, w)
        newNode.next = self.adjList[v2]
        self.adjList[v2] = newNode


    def dfs(self, start):   # start = 1
        self.visited[start] == True
        node = self.adjList[start]
        while node is not None:
            v = node.vertex
            weight = node.weight
            if self.visited[v] == False:
                if self.dist[start] + weight > self.dist[v]:
                     self.dist[v] = self.dist[start] + weight
                self.dfs(v)
            node = node.next
            print(self.dist)


n = int(f())
g = Graph(n)
for i in range(n-1):
    v1, v2, w = map(int, f().split())
    g.insertEdge(v1, v2, w)

# g.dfs(1)

# print(g.dist)