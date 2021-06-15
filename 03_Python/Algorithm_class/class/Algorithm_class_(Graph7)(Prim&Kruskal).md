# 7. Graph

오늘 배울 내용

> Prim 알고리즘(욕심쟁이 알고리즘)
> Kruskal 알고리즘(욕심쟁이 알고리즘)
> 상호 배타적 집합의 처리

## 🏄‍ (1) Prim 알고리즘

- 프림 알고리즘은 아래의 순서대로 작동한다:
  - 그래프에서 하나의 꼭짓점을 선택하여 트리를 만든다.
  - 그래프의 모든 변이 들어 있는 집합을 만든다.
  - 트리와 연결된 변 가운데 트리 속의 두 꼭짓점을 연결하지 않는 가장 가중치가 작은 변을 트리에 추가한다.

### 🚗 용어 설명

- G = (V, E) : 에지에 가중치가 있는 연결된 그래프
- n : |V|, m : |E|
- T : 최소비용 신장트리

**Pseudo code**

```pseudo
// 임의의 정점 s를 선택한다(s로부터 트리를 키워나갈 것 - 에지를 T에 하나씩 추가)
S = {s} // 초기의 트리 T의 정점들의 집합
A = ø   // 초기의 트리 T의 에지들의 집합
parents[s] = -1 // 초기화

while (A의 에지수 ≠ n-1)
   S와 V-S 사이의 최소 가중치의 에지 e = (u, v)를 선택한다.
   S = S U {u}
   parent[v] = u
   A = A U {e} // 트리 T에 e를 추가한다.
```

### 🚗 Prim 알고리즘 예시

<img src="https://images.velog.io/images/nathan29849/post/fb6ac2de-9bd1-4943-8262-0824ba949761/IMG_188E89E4DFB8-1.jpeg" width="">
<img src="https://images.velog.io/images/nathan29849/post/bdca215e-7f72-4d41-82b3-b5e3ae7b1dc4/IMG_A0859D0FCCAD-1.jpeg" width="">
<img src="https://images.velog.io/images/nathan29849/post/4a876c9a-2c74-491e-8698-1bff6bfdeb03/IMG_DC8751D6B5C0-1.jpeg" width="">
<img src="https://images.velog.io/images/nathan29849/post/1625d99e-d38e-4389-896b-160f01bc8ff6/IMG_260C09CDABE6-1.jpeg" width="">

### 🚗 Prim 알고리즘 구현

#### (1) 리스트(배열)를 이용한 구현

- V-S에 속하는 정점 v에 대하여,
  minWeight\[v] : v와 S의 정점들 사이의 에지들의 최소 가중치

- 수행시간 : `O(N^2)`

```pseudo
// V의 각 정점 u에 대하여,
minWeight[u] = ∞
parent[u] = -1

// 임의의 정점 s를 선택한다.
S = {s} // 트리 T의 정점들의 집합
A = ø // 트리 T의 에지들의 집합

// s와 인접한 각 정점 v에 대하여,
minWeight[v] = 에지 (s, v)의 가중치
parent[v] = s

while (A의 에지 수 ≠ n-1)
// S와 V-S 사이의 최소 가중치의 에지 e = (u, v)를 선택한다.
// -> V-S의 정점들의 minWeight[]가 최소인 정점을 선택 (S에 이미 있는 정점은 제외)
   S = S U {u}
   Parent[v] = u
   A = A U {e} // T에 e를 추가한다.
   // V-S의 정점들의 minWeight[]를 update
   node = adjList[v]
   while node is not None:
   // v와 인접한 V-S의 정점 w에 대하여,
       w = node.vertex
      if (weight(v, w) < minWeight([w])
         minWeight[w] = weight(v, w)
         parent[w] = v
      node = node.link
```

#### (2) 최소힙을 이용한 구현

- V-S에 속하는 정점 v에 대하여,
  minWeight\[v] : v와 S의 정점들 사이의 에지들의 최소 가중치

- V-S의 모든 정점들의 minWeight\[] 값을 최소힙 H로 관리

- 수행시간 : `O(M * log N)`
  - 오히려 m이 n^2에 가까워지면(에지 수가 늘어나면) 시간 복잡도가 증가
  - ex. 완전 그래프의 경우

```pseudo
// V의 각 정점 v에 대하여,
minWeight[u] = ∞
parent[u] = -1

// 임의의 정점 s를 선택한다.
S = {s} // 트리 T의 정점들의 집합
A = ø // 트리 T의 에지들의 집합

// s와 인접한 각 정점 v에 대하여,
minWeight[v] = 에지 (s, v)의 가중치
parent[v] = s

// V-S의 모든 정점들과 그 minWeight 값을 힙 H에 삽입
while (A의 에지 수 ≠ n-1)
   u = deleteMin(H)  // 최소힙 H에서 minWeight가 최소인 정점 삭제
   S = S U {u}
   Parent[v] = u
   A = A U {e} // T에 e를 추가한다.
   // V-S의 정점들의 minWeight[]를 update
   // u와 인접한 V-S의 정점 w에 대하여,
      if (weight(u, v) < minWeight([v])
         minWeight[v] = weight(u, v)
         최소힙 H를 update
         parent[v] = u
```

---

## 🏄‍ (2) Kruskal 알고리즘

MST(최소 비용 신장 트리) 가

- 1. 최소 비용의 간선으로 구성됨
- 2. 사이클을 포함하지 않음

의 조건에 근거하여 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택 한다

- 전체 에지 집합에서 가중치가 최소인 에지를 하나씩 제거(또는 뽑아내기)하여 그 에지가 구성한 포리스트에서 사이클을 만들지 않으면 구성한 포리스트에 포함시키는 알고리즘

### 🚗 용어 설명

Kruskal’s algorithm은 최소 비용 신장 부분 트리를 찾는 알고리즘이다. 변의 개수를 E, 꼭짓점의 개수를 V라고 하면 이 알고리즘은 O(E\*logE)의 시간복잡도를 가진다.

- 입력 : 에지에 가중치가 있는 그래프 G = (V, E)
- R = E (R은 남아있는 에지들의 집합)
- F = ø (현재까지 구성한 포리스트 에지들의 집합)

```
while (|F| != n-1)
   R에서 최소 가중치의 에지(v, w)를 제거한다.
   if ((v, w)를 F에 추가할 때, 사이클을 만들지 않으면),
      (v, w)를 F에 추가한다.
```

- `if (v, w)를 F에 추가할 때, 사이클을 만들지 않으면` 에 대한 판별은 어떻게?
  - set union & find를 활용한다.

**크루스칼 알고리즘**

> 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
> 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
> 즉, 가장 낮은 가중치를 먼저 선택한다.
> 사이클을 형성하는 간선을 제외한다.
> 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.

### 🚗 Kruskal 알고리즘 예시

#### Kruskal 알고리즘을 이용하여 MST(최소 비용 신장 트리)를 만드는 과정

- 간선 선택을 기반 으로 하는 알고리즘
- 이전 단계에서 만들어진 신장 트리와는 상관없이 무조건 최소 간선만을 선택하는 방법

<img src="https://images.velog.io/images/nathan29849/post/b89b4a54-58f5-4255-92a6-5815a3f36087/image.png">

### 🚗 Kruskal 알고리즘 시간 복잡도

- union-find 알고리즘을 이용하면 Kruskal 알고리즘의 시간 복잡도는 간선들을 정렬하는 시간에 좌우된다.
- 즉, 간선 e개를 퀵 정렬과 같은 효율적인 알고리즘으로 정렬한다면,
  - Kruskal 알고리즘의 시간 복잡도는 `O(E*logE)`가 된다.
- Prim 알고리즘의 시간 복잡도는 `O(N^2)`이므로,
  - 그래프 내에 적은 숫자의 간선만을 가지는 희소그래프(Sparse Graph)의 경우에는 Kruskal이 적합하다.
  - 그래프 간선이 많이 존재하는 밀집그래프(Dense Graph)의 경우 Prim 알고리즘이 적합하다.

---

## 🏄‍ (3) 상호 배타적 집합의 처리

### 🚗 집합의 처리

- disjoint set(배타적 집합)만을 대상으로 한다.
  - 성질 : 교집합이 공집합
- 연산
  - Make-Set(x) : 원소 x로만 이루어진 집합을 생성
  - Find-Set(x) : 원로 x를 가지고 있는 집합을 알아낸다.
  - Union(x, y) : 원소 x를 가진 집합과 원소 y를 가진 집합의 합집합

<img src="https://images.velog.io/images/nathan29849/post/8af7c074-a57f-4c95-9e2c-be8ba886e272/image.png">

### 🚗 Tree를 이용한 처리

- 같은 집합의 원소들은 하나의 tree로 관리한다.
  - child가 Parent를 가리킴
- tree의 root를 집합의 대표 원소로 삼는다.
  <img src="https://images.velog.io/images/nathan29849/post/52a4b66b-7228-483c-8d65-03949f8e599d/image.png">
  <img src="https://images.velog.io/images/nathan29849/post/549de687-26d9-4e2e-93fb-5d06fd391e73/image.png">
  <img src="https://images.velog.io/images/nathan29849/post/25004044-3d3b-4138-9ac6-62de7de316a5/image.png">

#### 트리를 이용한 집합 처리 알고리즘

- Make-Set(x)

```pseudo
{
	p[x] <- x  // 노드 x를 유일한 원소로하는 집합 생성
}
```

- Union(x, y)

```pseudo
{
	p[Find-Set(y)] <- Find-Set(x)
    // 노드 x가 속한 집합과 노드 y가 속한 집합을 각각 알아낸 후 합친다.
}
```

- Find-Set(x)

```pseudo
{
	if (x = p[x]) 			// 노드 x가 속한 집합을 알아낸다.
       then return x			// 노드 x가 속한 트리의 루트노드를 반환한다.
       else return Find-Set(p[x])
}
```

### 🚗 연산의 효율을 높이는 방법

- Rank를 이용한 Union
  - 각 노드는 자신을 루트로 하는 subtree의 높이를 랭크(Rank)라는 이름으로 저장한다.
  - 두 집합을 합칠 때 Rank가 낮은 집합을 Rank가 높은 집합에 붙인다.
- Path compression
  - Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꾸어 준다.

#### Rank를 이용한 Union의 예

<img src="https://images.velog.io/images/nathan29849/post/a6a263e6-d29c-49d7-aaed-ee46672b35c1/image.png">

#### Rank를 이용한 Union에서 랭크가 증가하는 예

<img src="https://images.velog.io/images/nathan29849/post/4448343e-464f-4cc3-8bf2-a1f2c29407fa/image.png">

#### Path compression의 예

<img src="https://images.velog.io/images/nathan29849/post/2017c822-ca96-474d-9755-7ef6357cc2d5/image.png">

#### Rank를 이용한 Union과 Make-Set

```
Algorithm Make-Set(x)
   p[x] <- x
   rank[x] <- 0

Algorithm Union(x, y)
   x' <- Find-Set(x)
   y' <- Find-Set(y)
   if (rank[x'] > rank[y'])
      then p[y'] <- x'
      else
         p[x'] <- y'
         if (rank[x'] = rank[y']) then rank[y'] <- rank[y'] + 1 (rank + 1)
```

#### Path Compression을 이용한 Find-Set

```
Algorithm Find-Set(x)
   if (p[x] ≠ x) then p[x] <- Find-Set(p[x])
   return p[x]
```

#### 수행시간

- Tree를 이용해 표현되는 Disjoint set에서 랭크를 이용한 Union과 경로압축을 이용한 Find-Set을 동시에 사용하면, m번의 Make-Set, Union, Find-Set 중 n번이 Make-Set일 때, 이들의 수행시간은 `O(M٭log*N)`이다.
  - 사실상 linear time이다.
  - log\*N = min{k : loglog ... logn ≤ 1}

### 🚗 Set Union/Find 응용

**Kruskal 알고리즘**

- set 초기화
  - 모든 정점 u에 대하여 Make-Set(x)
- (v, w)를 F에 추가할 때 사이클이 만들어지는 검사
  - x = Find-Set(v)
  - y = Find-Set(w)
  - if (x != y) // 사이클이 만들어지지 않으면 (v, w)를 F에 추가
  - v가 속해있는 트리와 w가 속해있는 트리를 연결하여 하나의 트리로 만듦
  - Union(x, y)
- 수행시간
  - m : 에지수
  - 에지들을 정렬하는데 걸리는 시간 `O(m*logm)` (ex 퀵정렬)
  - while loop : 거의 `O(m)`
  - 전체 수행시간은 `O(m*logm)`

<img src="https://images.velog.io/images/nathan29849/post/0644c722-e816-443a-abba-565dc8ac7863/image.png">

---

### References

[gmlwjd9405.github.io](https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html)
