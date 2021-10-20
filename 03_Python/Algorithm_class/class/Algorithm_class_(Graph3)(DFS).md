# 4. Graph 운행(Travels)

> **(1) 깊이 우선 탐색 (Depth First Search)**
> (2) 너비 우선 탐색 (Breadth First Search)

- 그래프나 유향 그래프에서 많은 문제들은, 해를 구하기 위해 모든 정점이나 에지에 대한 검사나 처리가 필요하다.
- 그래프의 운행 : 정점들을 한 번씩 방문 (방문 목적은 문제에 따라 결정된다.)
- 각 정점이나 에지를 한 번씩 방문하는 효율적인 탐색 전략
  - **깊이 우선 탐색 (DFS)**
  - 너비 우선 탐색 (BFS)

## (1) 깊이 우선 탐색(DFS)

### 깊이 우선 탐색에 대한 설명

- 그래프의 모든 정점을 한 번만 방문하는 알고리즘
- 트리에서의 Preorder Traversal(전위 순회)의 일반화
- 시작정점 v : 문제에서 정해지기도 하고, 임의로 정할수도 있음(일단 존재는 해야함)

```
1) 시작 정점부터 방문

2) 현재 방문하고 있는 정점 v와 인접한 정점을 하나씩 검사하면서
아직 방문되지 않은 (v와 인접한) 정점 w가 있으면 이 정점 w를 방문한다.

3) 이 과정을 반복하면서 더 이상 갈 곳이 없는 정점(인접한 정점들이 모두 방문된 경우)에
도달하면 마지막에 따라왔던 간선을 따라 뒤로 돌아가서(backtrack),
인접한 정점을 방문하는 탐색을 반복한다.
```

<img src="https://images.velog.io/images/nathan29849/post/4a8e4cdd-698d-4755-8565-32c67c8332d4/image.png" width="400px;">

### 깊이 우선 탐색의 아웃라인

- 깊이 우선 탐색 골격을 살펴보자
- 기본적으로 recursive version. (재귀 사용)
- 골격

```pseudo
Algorithm dfs(graph g, int v) // 시작정점이 v인 깊이 우선 탐색
   0) graph g의 모든 정점을 "미방문" 상태로 초기화

   1) v를 방문하고 이를 "방문 되었다"라고 표시 // v를 방문할 때 필요한 작업 수행

   2) v와 인접한 각 정점 w에 대하여 만약 w가 방문되지 않았다면 dfs(g, w) // w로 부터 backtrack할 때 필요한 작업 수행

   3) v가 "종료되었다."라고 표시 // v에서 시작하는 DFS를 마친 후 필요한 작업 수행
```

<img src="https://images.velog.io/images/nathan29849/post/94ba7cf0-183a-43d9-81e5-447bc10ecaa1/image.png" width="50%;">

- 정점 v의 상태 (3가지)

  - (1) v를 아직 방문하지 않음(미방문 상태)
  - (2) v를 처음으로 방문
  - (3) v와 인접한 정점을 모두 방문 (v에서 시작하는 DFS를 종료한 상태)
    위 3가지 상태 중 (1),(2)만 필요한 경우도 있고, (3)까지 다 필요한 경우도 있다.

- 깊이 우선 탐색의 예 (무방향 그래프)
  <img src="https://images.velog.io/images/nathan29849/post/6865a6ed-bf2a-4d7f-947d-7234cf04fd8f/image.png" width="70%;">
  깊이 우선 탐색 시, 각 정점 u에 대하여 u와 인접한 미방문 정점 v를 방문할 때, 에지(u, v)들로 구성된 root가 있는 트리 (v가 u의 child가 됨, root는 시작정점)

- 깊이 우선 탐색의 예 (방향 그래프)
  <img src="https://images.velog.io/images/nathan29849/post/ea24b3de-f39b-44eb-84e7-df125f3ce0ad/image.png" width="70%;">

### Python Code (DFS 응용)

- 정점 0에서 출발하는 DFS시 방문되는 정점들을 순서대로 출력

#### ➀ 인접 행렬

```python
def dfs1(adjMatrix, n, v, visited):
   visited[v] = True # 방문 표시 # color[v] = 'gray'
   print(v, end = ' ')
   for w in range(n): # (방문하지 않은) 인접한 정점 찾기
      if visited[w] == False and adjMatrix[v][w] == 1:
         dfs(adjMatrix, n, w, visited)
   # visited[v] = black

n, m = map(int, input().split())
adjMatrix = [[0 for i in range(n)] for j in range(n)]
visited = [False for k in range(n)]  # 'white'

for i in range(m):
   u, v = map(int, input().split())

   # adjacency matrix
   adjMatrix[u][v] = 1
   adjMatrix[v][u] = 1

print("dfs at 0 using adjacency matrix")
dfs1(adjMatrix, n, 0, visited) # 정점 0 부터 시작
```

- dfs1의 시간 복잡도 : `O(N^2)` (N : vertex 개수)

#### ➁ 인접 리스트 - 1 (연결리스트)

1. 그래프를 클래스로 정의하지 않고 표현

```python
class Node:
   def __init__(self, v):
      self.vertex = vertex
      self.next = None

def dfs2(adjList1, n, v, visited):
   visited[v] = True # color[v] = 'gray'
   print(v, end=' ')
   node = adjList1[v]
   while node is not None:
      w = node.vertex
      if visited[w] == False:
         dfs2(adjList1, n, w, visited)
      node = node.next
      # visited[v] = 'black'

n, m = map(int, input().split())
adjList1 = [None for i in range(n)]
visited = [False for k in range(n)]  # 'white'

for i in range(m):
   u, v = map(int, input().split())

   # adjacency list1 (linked list)
   node = Node(v)
   node.next = adjList1[u]
   adjList1[u] = node

   node = Node(u)
   node.next = adjList1[v]
   adjList1[v] = node

print("dfs at 0 using adjacency list1")
for i in range(n)
   visited[i] = False # visited[i] = 'white'

dfs2(adjList1, n, 0, visited)
```

2. 그래프를 클래스로 정의하여 표현

```python
class Node:
   def __init__(self, vertex):
      self.vertex = vertex
      self.link = None

class Graph:
   def __init__(self, size):
      self.adjList = [None] * size	# [None, None, ..., None]
      self.color = [white] * size
      self.size = size

   def add_edge(self, v1, v2):
      new_node = Node(v2)
      new_node.link = self.adjList[v1]
      self.adjList[v1] = new_node

      # in case of undirected graph
      new_node = Node(v1)
      new_node.link = self.adjList[v2]
      self.adjList[v2] = new_node

   def dfs(self, v):  # 정점 v부터 시작!
      self.color[v] = 'gray' # v를 방문
      print(v, end=' ')
      node = self.adjList[v]
      while node != None:
         w = node.vertex
         if self.color[w] == 'white':
            self.dfs(w)
         node = node.link
      self.color[v] = 'black'

    def printGraph(self):
       for v in range(self.size):
          print(v, end=': ')
          current = self.adjList[v]
          while current is not None:
             print(current.vertex, end=' ')
             current = current.link
          print()

n, m = map(int, input().split())
g = Graph(n)
for i in range(m):
   v1, v2 = map(int, input().split())
   g.add_edge(v1, v2)

g.printGraph()
g.dfs(0)
```

- dfs2의 시간 복잡도 : `O(N*M)` (N : vertex 개수, M : edge 개수)

#### ➂ 인접 리스트 - 2 (list of lists)

```python
def dfs3(adjList2, n, v, visited):
   visited[v] = True # color[v] = 'gray'
   print(v, end=' ')

   for i in range(len(adjList2[v])):
      w = adjList2[v][i]
      if visited[w] == False:
         dfs3(adjList2, n, w, visited)
   # visited[v] = 'black'

n, m = map(int, input().split())
adjList2 = [[] for i in range(n)]
visited = [False for k in range(n)]  # 'white'

for i in range(m):
   u, v = map(int, input().split())

   # adjacency list2
   adjList2[u].append(v)
   adjList2[v].append(u)

print("dfs at 0 using adjacency list2")
for i in range(n):
   visited[i] = False # visited[i] = 'white'
dfs3(adjList2, n, 0, visited)
```

- dfs3의 시간 복잡도 : `O(N*M)` (N : vertex 개수, M : edge 개수)

---

- 입력 예시

```python
9 9
0 1
0 3
0 4
2 4
2 3
5 6
5 8
6 8
6 7
```

- 출력 예시

```python
# dfs1
0 1 3 2 4

# dfs2
0 4 2 3 1

adjList =
0: 4 3 1
1: 0
2: 3 4
3: 2 0
4: 2 0
5: 8 6
6: 7 8 5
7: 6
8: 6 5
0 4 2 3 1

# dfs3
0 1 3 2 4

adjList2 =
[[1, 3, 4],
[0],
[4, 3],
[0, 2],
[0, 2],
[6, 8],
[5, 8, 7],
[6],
[5, 6]]
```

---

### 미로 문제

- 0은 통로의 일부, 1은 벽의 일부를 표현
- 출발지에서 목적지지 가는 경로가 있는가?
- 출발지에서 목적지까지 최단 경로를 구하라.

- m : 행의 개수, n: 열의 개수
  <img src="https://images.velog.io/images/nathan29849/post/bd9cdf37-3ca4-4d8c-a166-e13c41863a4f/image.png" width="70%">

#### Pseudo Code

```
// map : 미로 정보를 저장하는 2차원 배열
// m, n : 미로의 행과 열의 크기
// start, dest : 출발지와 목적지
// visited : 미로의 행과 열의 각 위치가 방문되었는지 아닌지를 위한 2차원 배열

// start에서 dest까지 가는 경로가 있는지를 판별하는 알고리즘
Algorithm findPath(map, m, n, start, dest, visited)
   visited[start.row][start.col] = true
   print("(", start.now, ",", start.col, ")")
   if (start.row == dest.row and start.col == dest.col) // 목적지 도달
      return true
   if (start.col < n-1){ // 오른쪽
      if (map[start.row][start.col+1] == 0 and not visited[start.row][start.col+1]) {
      next.row = start.row
      next.col = start.col + 1
      if(findPath(map, m, n, next, dest, visited))
         return true
          }
      }
   if (start.row < m-1){ // 아래쪽
      if (map[start.row+1][start.col] == 0 and not visited[start.row+1][start.col]) {
      next.row = start.row + 1
      next.col = start.col
      if(findPath(map, m, n, next, dest, visited))
         return true
         }
      }
   if (start.col > 0){ // 왼쪽
      if (map[start.row][start.col-1] == 0 and not visited[start.row][start.col-1]) {
      next.row = start.row
      next.col = start.col - 1
      if(findPath(map, m, n, next, dest, visited))
         return true
         }
      }
    if (start.row > 0){ // 위쪽
      if (map[start.row-1][start.col] == 0 and not visited[start.row-1][start.col]) {
      next.row = start.row - 1
      next.col = start.col
      if(findPath(map, m, n, next, dest, visited))
         return true
         }
      }

    return false
```

#### Python Code

```python
class Location:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col


def findPath(maze, m, n, start, dest, visited):
    next = Location()
    if maze[start.row][start.col] == "0":
        visited[start.row][start.col] = True
    else:
        return False

    if start.row == dest.row and start.col == dest.col:
        return True

    if (start.col < n-1):
        if maze[start.row][start.col+1] == "0" and visited[start.row][start.col+1] == False:
            next.row = start.row
            next.col = start.col+1
            if findPath(maze, m, n, next, dest, visited):
                return True
    if (start.row < m-1):
        if maze[start.row+1][start.col] == "0" and visited[start.row+1][start.col] == False:
            next.row = start.row+1
            next.col = start.col
            if findPath(maze, m, n, next, dest, visited):
                return True
    if (start.col > 0):
        if maze[start.row][start.col-1] == "0" and visited[start.row][start.col-1] == False:
            next.row = start.row
            next.col = start.col-1
            if findPath(maze, m, n, next, dest, visited):
                return True
    if (start.col > 0):
        if maze[start.row-1][start.col] == "0" and visited[start.row-1][start.col] == False:
            next.row = start.row-1
            next.col = start.col
            if findPath(maze, m, n, next, dest, visited):
                return True

    return False

start = Location(1, 0)
dest = Location(5, 11)

m, n = 7, 12

maze = []
for i in range(m):
    maze.append(input())

visited = [list(False for i in range(n))for j in range(m)]
result = findPath(maze, m, n, start, dest, visited)
print(result)

# 111111111111
# 000100100001
# 101101101101
# 100000100101
# 111101111101
# 100000000000
# 111111111111
```
