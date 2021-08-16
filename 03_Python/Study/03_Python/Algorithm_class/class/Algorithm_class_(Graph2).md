# Graph

## 3. Graph 표현

그래프의 표현 방법으로는 크게 두 가지가 있다.

> 1.  인접 행렬
> 2.  인접 리스트

- n : |V| (그래프의 정점 수)
- m : |E| (그래프의 에지 수)
- 그래프의 정점 집합 : V = {v0, v1, ..., vn-1}
- 그래프 G의 n개의 정점들을 0부터 n-1의 정수로 대응시킨다.
  (정점 vi를 정수 i에 대응 시킨다고 가정)

---

### 1) 인접 행렬 (Adjacency Matrix) 표현

#### (1) 그래프 G의 인접 행렬 A = (aij) 표현

- aij = 1 ((vi, vj)가 E에 속하는 경우 - 인접하는 경우)
- aij = 0 ((vi, vj)가 E에 속하지 않는 경우 - 인접하지 않는 경우)
- 무향 그래프에 대한 인접 행렬은 `대칭적`이다.

무향 그래프 인접 행렬 표현 예시
<img src="https://images.velog.io/images/nathan29849/post/58d107ce-2e82-4ad6-985b-e138e686f872/image.png" width="60%;">

- 단, 에지가 없는 것(인접하지 않는것)도 0이라는 하나의 값으로 표현하고 있기 때문에 낭비적이라고 볼 수 있다. (공간적 낭비)

- 그래프의 입력
  ex.

```python
9 9 	# n m
0 1	# a b
0 3	# a d
0 4   # a e
2 4	# c e
2 3	# c d
5 6	# f g
5 8	# f i
6 8	# g i
6 7	# g h
```

<img src="https://images.velog.io/images/nathan29849/post/be60cfc3-4d9c-4bc1-a440-73984d7fd0ed/image.png" width="60%;">

- Python Code

```python
class Graph:
   def __init__(self, size):
      self.adjMatrix = [[0 for j in range(size)] for i in range(size)]
      self.size = size

   def insertEdge(self, v1, v2):
      self.adjMatrix[v1][v2] = 1
      self.adjMatrix[v2][v1] = 1 # in case of undirected graph

   def printGraph(self):
      for i in range(self.size):
         for j in self.adjMatrix[i]
             print(j, end = ' ')
         print()

def main():
   n, m = input().split()
   n, m = int(n), int(m)
   g = Graph(n)
   for i in range(m):
      v1, v2 = input().split()
      v1, v2 = int(v1), int(v2)
      g.insertEdge(v1, v2)
   g.printGraph()

if __name__ = "__main__":
   main()
```

#### (2) 가중치 그래프 G = (V, E, W)의 인접 행렬 A = (aij) 표현

- aij = weight(i, j) ((vi, vj)가 E에 속하는 경우 - 인접하는 경우)
  (weight(i, j)는 에지(vi, vj)의 가중치)
- aij = c ((vi, vj)가 E에 속하지 않는 경우 - 인접하지 않는 경우)
  (c는 문제에 따라 0 혹은 ∞)

- (에지에) 가중치가 있는 그래프의 입력
  > n : vertex 수
  > m : edge 수
  > i0, j0 : wt0 (에지 (i0, j0)의 가중치)
  > i1, j1 : wt1 (에지 (i1, j1)의 가중치)
  > ...
  > in-1, jn-1 : wtn-1 (에지 (in-1, jn-1)의 가중치)

### 2) 인접 리스트 (Adjacency List) 표현

#### (1) 연결 리스트(Linked List)로 표현

- 각 정점에 대하여, 이 정점과 인접한 모든 정점들을 연결리스트로 만듦
- 리스트 i번째의 원소 : vi와 인접한 정점들의 연결리스트를 참조함
- 인접하지 않은 것의 정보는 갖고 있지 않다.(인접 행렬과의 차이점 - 공간 효율 ↑)

<img src="https://images.velog.io/images/nathan29849/post/029d62f7-afff-4f93-b5db-128181754637/image.png" width="700px;">

- Python Code

```python
class Node:
   def __init__(self, vertex):
      self.vertex = vertex
      self.link = None

class Graph:
   def __init__(self, size):
      self.adjList = [None] * size
      self.size = size

   def insertEdge(self, v1, v2):
      newNode = Node(v2)
      newNode.link = self.adjList[v1]
      self.adjList[v1] = newNode

      # in case of undirected graph
      newNode = Node(v1)
      newNode.link = self.adjList[v2]
      self.adjList[v2] = newNode

   def printGraph(self):
      for v in range(self.size):
         print(v, end = ': ')
         current = self.adjList[v]
         while current is not None:
            print(current.vertex, end =' ')
            current = current.link
         print()

   def main():
      n, m = input().split()
      n, m = int(n), int(m)
      g = Graph(n)
      for i in range(m):
         v1, v2 = input().split()
         v1, v2 = int(v1), int(v2)
         g.insertEdge(v1, v2)
      g.printGraph()

   if __name__ == "__main__":
      main()
```

<img src="https://images.velog.io/images/nathan29849/post/1a5566f4-3800-4690-b29e-393db7b4e94b/image.png" width="700px;">

#### (2) List of lists 로 표현

- Node로 따로 표현하지 않고, 리스트 속에 리스트를 넣어 인접한 정점들을 관리한다.

- Python Code

```python
class Graph:
   def __init__(self, size):
      self.adjList = [[] for i in range(size)]
      self.size = size

   def insertEdge(self, v1, v2):
      self.adjList[v1].append(v2)	# 인접 정점들을 리스트의 마지막에 집어 넣음
      # in case of undirected graph
      self.adjList[v2].append(v1) 	# 인접 정점들을 리스트의 마지막에 집어 넣음

   def printGraph(self):
      for v in range(self.size):
         print(v, end = ': ')
         for x in self.adjList[v]:
            print(x, end = ' ')
         print()

n, m = [int(x) for x in input().split()]	# 이렇게도 표현할 수 있구나.. map(int, input().split()) 이거랑 같음
g = Graph(n)
for i in range(m):
   v1, v2 = [int(x) for x in input().split()]
   g.insertEdge(v1, v2)
g.printGraph()
```

- append : 동적으로 배열 크기가 할당된다. (amortized : 기본적인 크기가 먼저 주어지고, 점점 커짐, 줄기도 함)
