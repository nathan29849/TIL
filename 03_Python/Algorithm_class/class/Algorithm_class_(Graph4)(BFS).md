# 4. Graph 운행(Travels)

> (1) 깊이 우선 탐색(Depth First Search)
> **(2) 너비 우선 탐색(Breadth First Search)**

- 그래프나 유향 그래프에서 많은 문제들은, 해를 구하기 위해 모든 정점이나 에지에 대한 검사나 처리가 필요하다.
- 그래프의 운행 : 정점들을 한 번씩 방문 (방문 목적은 문제에 따라 결정된다.)
  각 정점이나 에지를 한 번씩 방문하는 효율적인 탐색 전략
  - 깊이 우선 탐색 (DFS)
  - **너비 우선 탐색 (BFS)**

## (2) 너비 우선 탐색(BFS)

### 너비 우선 탐색에 대한 설명

- 그래프의 모든 정점을 한 번만 방문하는 알고리즘
- 정점들이 출발 정점으로 부터 거리가 증가하는 순서대로 방문이 됨
  (거리 : 경로에 있는 에지들의 수)
- 다음은 너비 우선 탐색을 하면서 너비우선트리를 찾는 알고리즘(v: 시작정점)

```pseudo
// g: 그래프, n: 정점 수, v: 출발정점
// parent는 배열로서 parent[u]는 bfs 트리에서 u의 부모노드를 가리킴
Algorithm bfs(g, n, v, parent)
   // visited는 각 정점이 방문 되었는지를 체크하기 위한 크기 n인 배열
   for w = 0 to n-1
      visited[w] = false

   dist[0] = 0		// dist = 거리 저장하는 배열
   parent[v] = -1  // 시작 정점의 parent는 없기 때문
   visitied[v] = true // v를 방문

   // Queue : 큐
   Q.enqueue(v) // 큐에 v를 삽입

   while(!Q.isEmpty)   // 큐가 비어있지 않다면,
      u = Q.dequeue()  // 큐에서 삭제
      // u와 인접한 각 정점 w에 대하여,
         if (!visited[w])
            visited[w] = true
            Q.Enqueue(w)
            parent[w] = u // bfs 트리 에지
            dist[w] = dist[u] + 1 // 거리 계산
```

- 시간 복잡도 : O(n^2)
- 인접리스트 사용시 : O(m+n)

### 너비 우선 탐색의 예

<img src="https://images.velog.io/images/nathan29849/post/a084e551-3c7e-4b59-a66a-fdff9d051799/image.png" width="70%">

- DFS는 스택을 이용하고, BFS는 큐를 이용한다.
