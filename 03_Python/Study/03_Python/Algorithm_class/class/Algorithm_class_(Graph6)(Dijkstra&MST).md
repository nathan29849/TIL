# Graph

오늘 배울 내용

> (1) 최단경로(shortest path) 문제
> (2) 최소 스패닝트리(minimum spanning tree)

---

## 🍉 (1)최단 경로 문제

- 에지에 가중치가 있는 그래프 (weighted graph)에서 두 정점 u와 v에 대해, u로부터 v까지의 **최단경로** 를 구하는 문제

### 🍈 Dijkstra 알고리즘(최단경로 찾는 알고리즘)

- 에지의 가중치가 양수인 그래프에서 source s(시작정점)로부터 다른 모든 정점까지의 최단경로를 찾는 알고리즘
- s로부터의 **최단경로 길이가 증가하는 순서대로 정점들을 고려** 하여 최단경로를 찾음
- 욕심쟁이 알고리즘 (Greedy)

<img src="https://images.velog.io/images/nathan29849/post/8278816a-3eb3-424e-a8eb-06c121cf6814/image.png" width="70%">

- 그래프는 연결되어 있다고 가정 (그렇지 않은 경우, 연결요소를 구하여 수행)
- V : 정점들의 집합, E : 에지들의 집합
- n : 정점들의 수, m : 에지들의 수
- S : source s로부터 현재 최단경로를 찾은 정점들의 집합
- D\[v] : s로부터 S에 속한 정점들만을 통하여 정점 v까지 가는 최단경로의 길이

```pseudo
S = {s}
while(|S|≠n)
   V - S의 정점들 중 D[] 값이 최소인 정점 u를 찾는다.
   // 그러면 D[u]는 s로부터 u까지의 최단경로의 길이가 된다.
   S = S U {u}
   u로부터 인접한 V-S의 각 정점 w에 대하여,
      D[w] = min(D[w], D[u] + weight(u, w))
      // u를 지나지 않는경우와 u를지나는 경우를 비교하여 더 작은 값 선택
```

<img src="https://images.velog.io/images/nathan29849/post/8c9a6d7f-4f85-44f2-a416-f15e71b0b52c/image.png" width="80%">

### 🍈 다익스트라 알고리즘의 정확성

- 정리 : 에지 가중치가 양수인 연결된 그래프에서 Dijkstra 알고리즘은 모든 정점에 대하여 최단 경로를 구한다.

- 증명 : 정점 s로부터 정점 u까지 최단 경로의 길이를 δ(s, u)로 표기한다. S에 있는 모든 정점 v에 대하여, D\[v]가 δ(s, v)와 같음을 보인다. 이는 S에 포함되는 정점 개수에 대한 수학적 귀납법으로 증명한다.

- 수학적 귀납법

> S에 포함되는 정점 개수가 1개일 경우, 자명하다.
> S에 포함되는 정점 개수가 k-1개일 때, S의 모든 정점 v에 대하여, D\[v]가 δ(s, v)라 하자. S에 포함되는 정점들의 수가 k일 때를 보자.
> V - S의 정점들 중 D\[] 값이 최소인 정점을 u라고 하자.
> D\[u] = δ(s, u), 즉 D\[u]가 a로부터 u까지 가는 최단경로 길이와 같음을 보인다.

- 만약 D\[u] ≠ δ(s, u)라 가정하자. (그렇지 않다고 가정하고, 모순됨을 보인다.)
  - s로부터 u까지 최단경로를 P라 하면, 가정에 의하여 P의 길이는 D\[u]보다 작다. P는 V - S에 있는 u가 아닌 어떤 정점을 지난다.
  - 경로 P에서 S에 포함되지 않는 정점 중 처음으로 지나는 정점을 u'라고 하자.

<img src="https://images.velog.io/images/nathan29849/post/96e82202-a0bf-4ebd-808c-8c1f41391607/image.png" width="70%">

- D\[u'] < P의 길이 < D\[u] 이다.

- 그런데 Dijkstra 알고리즘에서, V - S에 있는 모든 정점들 중 D\[u]가 최소이다. 이는 모순이다. 따라서 S에 포함되는 정점들의 수가 k일 때도, S의 모든 정점 v에 대하여 D\[v] = δ(s, v)이다.

### 🍈 Dijkstra 알고리즘 구현 - 인접행렬 표현

- The weoghted graph is represented as an adjacency matrix A
- 최단 경로를 찾기 위하여, 배열 parent를 이용
  - (parent : v 바로 직전에 지나가는 정점)
  - 최종적으로 parent를 다 구하면 역순으로 추적하여 최단경로를 찾아낼 수 있음 (stack으로 구현하면 순서대로 출력이 가능)
- S : 최단 경로를 찾은 vertex들의 집합

```pseudo
S = {s}
for i = 0 to n
   D[i] = adjMatrix[s][i]  // 지나는 에지 없으면 ∞로 초기화
   parent[i] = s // s로 우선 초기화

while(|S|≠n)
   V - S의 vertex들 중 D[] 값이 최소인 정점을 u라고 하자.
   S = S U {u}
   u로부터 인접한 모든 정점 w에 대하여
      if(D[w] > (D[u] + adjMatrix[u][w])
         D[w] = D[u] + adjMatrix[u][w]
         parent[w] = u // parent 값 update
```

- 수행시간 분석
  - n : 정점 수, m : 간선 수
  - 그래프를 인접행렬로 표현할 경우 : `O(n^2)`
  - 그래프를 인접리스트로 표현할 경우
    - D\[]를 단순 배열(리스트)로 관리할 경우 : `O(n^2)`
    - D\[]를 최소힙으로 관리할 경우 : `O(m * log n)`
      (최소힙의 경우, 에지수가 늘어남에 따라 시간복잡도가 증가.)
      (만약 에지수가 n^2에 가까워지면 사실상 `O(n^2 * log n)` 시간소요)

<img src="https://images.velog.io/images/nathan29849/post/721fe440-2aa0-4a5d-8a3e-1b370f61db96/image.png">

<img src="https://images.velog.io/images/nathan29849/post/fba42859-5a1b-4145-a85b-2e68863607a6/image.png">

### 🍈 다익스트라 알고리즘의 예

<img src="https://images.velog.io/images/nathan29849/post/9ee57ff7-3f4d-4661-97d4-dc8b3423e316/image.png">

<img src="https://images.velog.io/images/nathan29849/post/07d78589-e137-4dc5-bfa5-b892b594666d/image.png">

<img src="https://images.velog.io/images/nathan29849/post/1d823783-f297-4932-a2fa-8194b6ab88e6/image.png">

<img src="https://images.velog.io/images/nathan29849/post/b1d92065-d08c-4031-807b-1b2d59d47b3b/image.png">

**NOTE**

- 만약 가중치가 음인 에지가 있을 경우, Dijkstra 알고리즘은 최단경로를 찾지 못할 수도 있다.

- 다음 예에서, source 0으로부터 1까지 가는 최단 경로를 구할 때, Dijkstra 알고리즘은 최단경로로 길이 2인 경로 (0,1)을 구한다.
- 허나 실제 최단경로는 길이 1인 (0, 2, 1)이다.

<img src="https://images.velog.io/images/nathan29849/post/5bcc4859-5404-46ee-bec4-e53af68a7087/image.png">

---

## 🍉 (2) 최소비용 스패닝(신장) 트리

- 트리 : 사이클이 없는 연결된 그래프이다. (자료구조의 트리와 달리 root가 없음)

- 스패닝 트리(spanning tree)란?
  - 그래프 G의 스패닝 트리는 G의 부그래프(sub Graph)
  - 그래프 내의 모든 정점을 포함하는 트리
  - 그래프의 최소 연결 부분 그래프이다.
  - 최소 연결 : 간선의 수가 가장 적음
  - n 개의 정점을 가지는 그래프의 최소 간선의 수는 n-1, n-1개의 간선으로 모든 정점이 연결되어 있으면 필연적으로 트리 형태가 되고, 이것이 바로 spanning tree가 된다.

### 🍈 설명

- 그래프 에지 하나를 스패닝 트리에 추가하면 반드시 사이클이 생긴다.

<img src="https://images.velog.io/images/nathan29849/post/5a2fab31-db60-4660-bd2e-2d509a79d14d/image.png">

- 최소비용 스패닝 트리의 정의 : 에지에 가중치가 있는 그래프 G의 최소비용 스패닝트리는 전체 가중치(가중치의 합)가 최소인 G의 스패닝트리이다.
  (가중치를 비용으로 생각할 수도 있음.)
  (어떻게 연결해야 최소비용으로 연결할 수 있을까?가 관건이다.)

<img src="https://images.velog.io/images/nathan29849/post/b583b826-e39f-4fa2-b47b-7f4448ee7de6/image.png">

### 🍈 성질

- 보조 정리 1
  - 트리 T에 대하여, T에 있지 않는 에지 e를 T에 추가하면, 사이클이 생긴다.

<img src="https://images.velog.io/images/nathan29849/post/67b87bdc-cc1c-4c77-966c-f8304e839596/image.png">

- 보조 정리 2

  - 연결된 가중치 그래프 G = (V, E, W)에 대하여, S를 V의 임의의 부분집합이라 하자. S와 V-S 사이의 에지들 중 가중치가 가장 작은 에지 e = (u, v)
    를 포함하는 최소비용 신장트리(MST)가 존재한다.

- 보조 정리 2에 대한 증명
  - e는 가중치가 가장 작은 에지이다.
  - T를 임의의 최소비용 스패닝트리(MST)라 하자.
  - T가 e를 포함하지 않는다고 하자.
  - T에 e를 추가하면 사이클 C가 만들어진다.
  - 이 사이클 C는 S와 V-S 사이의 어떤 에지 e' = (x, y)를 포함한다.
  - T' = (T - {e'} U {e})는 스패닝 트리이다.
  - W(T) : T의 에지 가중치의 합
  - W(T') : T'의 에지 가중치의 합
  - weight(e) : 에지 e의 가중치
  - weight(e') : 에지 e'의 가중치
  - weight(e) ≤ weight(e')이므로 W(T') ≤ W(T)이다.
  - 따라서 에지 e를 포함하는 최소비용 신장트리가 존재한다.

<img src="https://images.velog.io/images/nathan29849/post/7246ec2a-c827-4e8c-bf7b-9aff313d540f/image.png">
