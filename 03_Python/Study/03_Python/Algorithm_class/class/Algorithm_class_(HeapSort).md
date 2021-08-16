# 1. 힙(Heap)

## (1) 성질

### a. 구조적 성질

- 완전이진트리의 구조를 가지고 있다.
  - 마지막 레벨을 제외하고 모든 레벨에서 노드들이 꽉 차있으며, 마지막 level에서는 노드들이 왼쪽부터 오른쪽으로 꽉 채워져 있다.

### b. Heap Order property

- 모든 노드의 값이 자식 노드보다 같거나 커야 한다. (최대힙)
  - 가장 큰 노드의 값이 루트 노드에 있어야 한다.
- 모든 노드의 값이 자식 노드보다 같거나 작아야 한다. (최소힙)
  - 가장 작은 노드의 값이 루트 노드에 있어야 한다.

heap sort, priority queue 등에서 활용된다.

### c. height & number of leaves

- n개의 노드를 가진 **힙의 높이** : (logN)을 반내림한다.(소숫값 버림)
- n개의 노드를 가진 완전 이진 트리의 **리프 노드 개수** : (n/2)를 반올림한다.

- level은 0부터 시작한다.
- node X의 level은 X의 parent의 `level + 1`이다.
- node X가 root 노드라면, X의 level은 0이다.
  <img src="https://images.velog.io/images/nathan29849/post/5fd4c25b-cdf8-4682-b75f-821c2da002f0/image.png" width="60%">

### d. 배열로 힙 구현하기

- 부모 자식간의 관계가 중요하다.
- 부모 노드의 index를 i라고 한다면,
  - 왼쪽 자식의 index는 `2*i + 1`이다.(if 2\*i + 1 < n)
  - 오른쪽 자식의 index는 `2*i + 2`이다.(if 2\*2 + 2 < n)
- 자식 노드의 index를 j라고 한다면,
  - 부모 노드의 index는 `(j-1)/2`를 내림한 값이다. (if j != 0)

<img src="https://images.velog.io/images/nathan29849/post/883eeb9a-e4c9-4344-bb25-0441c6f809c1/image.png" width="70%">

## (2) Rebuild Heap

> 힙 정렬에서 유용한 연산
> 루트의 왼쪽 부트리와 오른쪽 부트리가 최대힙(또는 최소힙)일 경우, 루트를 포함한 전체 트리를 힙으로 만듦

<img src="https://images.velog.io/images/nathan29849/post/a01653a6-13fe-4317-b672-0e8fd1ccee40/image.png" width="60%">

### Rebuild Heap에서의 핵심은 힙 성질을 유지하는 것이다.

rebuild heap python code

```python
def rebuildHeap(A, r, n): # A : 리스트, r : 루트노드, n : 전체 노드 개수
# r은 left subtree와 right subtree가 최대 힙일 때, 루트가 r인 최대 힙을 만듦
# r은 리스트에서 root의 위치임
    current = r
    value = A[r]    # 루트의 값을 value가 참조(value에 저장)
    while (2*current + 1 < n):
        leftChild = 2*current + 1
        rightChild = leftChild + 1
        # 두 자식 노드 중 큰 값의 노드를 largerChild로 이동

        if rightChild < n and A[rightChild] > A[leftChild]:
            largerChild = rightChild
        else:
            largerChild = leftChild

        if value < A[largerChild]: # largerChild의 값이 크면
            A[current] = A[largerChild]
            current = largerChild   # current를 largerChild로 내림
        else:
            break
    A[current] = value
    # while문 바깥에 있는 이유 : current로 비교한 후 일단 value보다 큰 값을 다 바꿔주고 마지막에 current자리
    # 즉 마지막에 바뀐 largerChild자리에 원래의 value값을 넣어주면 된다. (매번 할 필요가 없음)
```

- 기본연산 : 원소비교(loop 1번 돌 때마다 자식들과 비교)
  - 비교를 두 번씩 한다.(자식들끼리 한 번, 추가된 노드와 한 번)
  - 사실상 level 1씩 증가할 때마다 비교를 두 번씩 한다고 보면 됨
- 힙의 높이가 `h`라고 했을 때, 최악의 경우에 비교를 2h만큼 하게 된다.

  - 최악의 경우에는 최대 level까지 내려가야 하기 때문이다. (상수는 무시)

- 총 n개의 노드가 있을 때, 높이 `h`인 힙은 `logn의 내림`으로 표현 가능하다.

- 따라서 rebuildHeap은 `O(h)`만큼의 시간 복잡도를 갖는다. 즉 `O(logN)`

# 2. 힙정렬(Heap Sort)

## (1) 설명(최대힙을 이용한 정렬)

- 단계 1: 최대 힙을 만듦(rebuild heap 이용)
  - 마지막 노드의 부모노드부터 시작하는 rebuild heap
- for root = n/2 - 1 to 0 by -1
  - transform a semiheap with the given root into a heap rebuildHeap(A, root, n)

```python
n = len(heap)
for i in range(n//2 - 1, -1, -1):
   rebuildHeap(A, i, n) # 각 i에 대해서 rebuild하면 된다!
```

## (2) 단계 1 : Rebuild Heap 이용하기

### 조건 : left와 right의 subtree들이 모두 힙이어야 성립 가능하다.

<img src="https://images.velog.io/images/nathan29849/post/bcd8d283-2dff-4bd5-b180-66ab3f76159e/image.png" width="60%">
<img src="https://images.velog.io/images/nathan29849/post/c77f6fb4-c56d-4ebf-a427-6110807f461e/image.png" width="60%">
<img src="https://images.velog.io/images/nathan29849/post/cca903a9-27be-446e-84e7-5f58211e99c5/image.png" width="60%">
<img src="https://images.velog.io/images/nathan29849/post/c0f18cf1-7f61-406c-be94-6b485dac665d/image.png" width="60%">
<img src="https://images.velog.io/images/nathan29849/post/59f72b43-60b8-4ee9-9500-d64bcba472c7/image.png" width="60%">

## (3) 단계 2 : 최대힙을 정렬된 리스트(배열)로 만들기

- 단계 1에서 만든 최대힙(배열)으로부터 다음 과정을 반복하여 정렬(n : 원소개수)
- last : 힙의 마지막 노드의 위치로서 초기 값은 `n-1`이다.
- 초기에 힙은 A\[0 .. last]에 있다.

> 1.  힙의 루트에 있는 원소 A\[0](즉, 최대 원소)와 마지막 원소 A\[last]를 교환한다.
> 2.  힙의 크기를 1 줄인다. 루트가 A\[0]인 semiheap에 대하여 `rebuildHeap`을 호출하여 힙으로 만든다.
> 3.  `last = 0` 이 될 때까지 위의 단계 1-2를 반복한다.

쉽게 말하면 첫 번째 원소와 마지막 원소를 바꾼 후 마지막 원소 제외 후 다시 정렬

```python
heap_size = n
for last in range(n-1, 0, -1):
   A[0], A[last] = A[last], A[0]
   heap_size -= 1
   rebuildHeap(A, 0, heap_size)
```

## (4) Heap Sort 수행시간 분석

### Heap Sort Code by Python

```python
def heapsort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):   # step 1
        rebuildHeap(A, i, n)

    heap_size = n
    for last in range(n-1, 0, -1):      # step 2
        A[0], A[last] = A[last], A[0]
        heap_size -= 1
        rebuildHeap(A, 0, heap_size)
```

### 단계 1의 수행시간

- RebuildHeap은 `O(h)`만큼의 시간 복잡도를 갖는다.
  (루트노드부터 내려오고, 최악의 경우엔 리프노드까지 내려가므로)

- 힙 높이 h는 `logn의 내림` 값과 같다. 따라서 RebuildHeap은 `O(logN)`
  의 시간 복잡도를 갖는다.

- Heap Sort는 대략 n/2만큼 rebuildHeap을 수행하기 때문에, n/2\*logn의 시간이 걸리게 되므로, `O(nlogn)`의 시간 복잡도를 갖는다고 할 수 있다.

- 하지만 이는 tight bound하지 않다. 엄밀하게 분석하자면, `O(nlogn)`보다는 더 작다. 오히려 `O(n)`이라고 볼 수 있다. (허나 이는 최종 수행시간에 영향을 미치지는 않는다.), (자식 하나만 제대로 비교하고 남은 자식은 break로 탈출하기 때문)

### 단계 2의 수행시간

- rebuildHeap(A, 0, heap_size)의 수행시간은 `O(logn)`이다.
- rebuildHeap(A, 0, heap_size)는 총 **n-1**번 수행된다.
- 따라서 단계 2의 수행시간은 총 `O(nlogn)`이다.

### 총 수행시간

단계 1 + 단계 2의 수행시간을 모두 더하면 총 수행시간은 `O(nlogn)`이다.

# 3. 우선순위 큐 (Priority Queues)

## (1) 설명

우선순위 큐는 중요한 힙의 응용(application of heaps)이다.
키와 관련이 있는 집합의 요소들을 동적으로 유지하게끔 해준다.

- insert(S, x) : inserts the element x into the set S
- find(S) : returns the element of S with the largest key
- deleteMax(S) : removes and returns the element of S with the largest key

## (2) Insertion Operation

- 리스트의 맨 마지막에 원소를 삽입한다.
- 만약 부모 노드보다 크다면 바꾸고, 이 과정을 반복한다.

수도코드

```
Algorigthm insert(A, key)
   n <- n+1
   i <- n-1 // 마지막 원소의 인덱스를 i로 놓기
   while i > 0 and A[Parent(i)] < key
      L[i] <- L[Parent(i)]
      i <- Parent(i)
   L[i] <- key
```

### 시간 복잡도

최악의 경우 루트 노드까지 새로 추가한 노드가 올라가므로 높이만큼의 시간 복잡도가 걸린다.
따라서 `O(h)` 즉 `O(logN)`이다.

## (3) DeleteMax Operation

- 루트 노드를 삭제한다.
- 그리고 그 루트 노드 자리에 힙의 맨 마지막 노드를 넣는다.
- 남은 노드들로 rebuildHeap을 실행하여 heap을 재구성한다.

수도코드

```
Algorithm deleteMax(A)
   if n < 1
      then error "heap underflow"
   maximum <- A[0]
   A[0] <- A[n-1]
   n <- n-1
   rebuildHeap(A, 0, n)	// 업데이트 된 n이다.
   return maximum
```

### 시간 복잡도

주요 연산은 rebuildHeap이고, 최악의 경우 루트 노드가 리프 노드까지 내려가는 경우이므로 `O(logN)`이다.

## (4) Python "heapq" library

- 파이썬은 우선순위 큐를 위한 heapq 라이브러리를 제공한다.
- 연산 종류 : insert, deleteMin ...
- import heapq를 코드로 적어 사용한다.
- heapq에 선언된 메소드
  > heapq.heappush(heap, item) // insert()와 동일
  > heapq.heappop(heap) // deleteMin()과 동일
  > heapq.heappushpop(heap, item) // item 삽입 후 deleteMin() 수행
  > heapq.heapify(h) // 리스트 h를 힙으로 만듦

++ 참고 : 여러 개의 원소를 넣을 때는 튜플을 이용하자(튜플인 경우 맨 앞 요소가 기준이다.)

# 4. 정렬 알고리즘들의 비교

## (1) 비교 분석 표

<img src="https://images.velog.io/images/nathan29849/post/9f9344fb-c2f3-4cc4-8efa-66eab10d9c55/image.png" width="70%">

## (2) 정렬 알고리즘의 하한계(lower bound)

- 정리 : n개의 자료(원소)를 키 비교에 의하여 정렬하는 알고리즘은 최악의 경우 적어도 `log(n!)의 내림`만큼 키를 비교한다. (≈`(nlogn - 1.443n)의 내림`과 비슷함)

- 키 비교에 의한 정렬 알고리즘의 최악의 경우 시간 복잡도는 `Ω(nlogn)`이다.
  - 키 비교에 의한 정렬 알고리즘으로 Merge Sort나 Heap Sort는 **최악의 경우 최적인 알고리즘**이다.
