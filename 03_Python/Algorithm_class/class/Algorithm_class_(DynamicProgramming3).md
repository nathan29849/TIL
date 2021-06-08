# Dynamic Programming (동적 계획법 - 3)

> 7.  Weighted Interval Scheduling

## 7. Weighted Interval Scheduling

### (1) Interval Scheduling problem (구간 스케쥴링 문제)

> We are given a set of intervals(구간) : "I" = {(si, fi) | i = 1, ..., n}
> (si = 시작시간, fi = 끝나는 시간)
> Our goal is to find a subset "J" ⊂ "I" such that
>
> - no two intervals in "J" overlap and
> - |J| is as large as possible

- ex. 아래의 5개 구간 I1, I2, I3, I4, I5에 대하여 겹치지 않는 구간은 최대 3개(I2, I4, I5)이다.
  <img src="https://images.velog.io/images/nathan29849/post/becd4d99-0569-4038-bd13-f8377401b5dd/image.png" width="40%">

- 먼저 끝나는 구간을 선택하는 욕심장이(greedy) 방법으로 최적 해를 구한다.
  <img src="https://images.velog.io/images/nathan29849/post/24ccb029-a7ad-4153-a405-f893c060fbdc/image.png" width="40%">

- 허나 greedy의 방법은 가중치가 주어진 Interval Scaheduling 문제에 대해 비효율적이다.

```python

```

---

### (2) Weighted Interval Scheduling problem

> we are given the set of intervals (jobs) "I" along with a set of weights {Wi}
> Now, we wish to find the subset "J" ⊂ "I" such that
>
> - no two intervals in "J" overlap and
> - ∑(i∈J)Wi is as large as possible (구간의 가중치의 합이 최대치여야 한다.)

- n개의 구간들(시작 시간, 끝나는 시간, 가중치)에 대하여, 가중치의 합이 가장 큰 겹치지 않는 구간들을 구하라.

- ex. 아래의 5개 구간에 대하여, 가중치의 합이 가장 큰 겹치지 않는 구간은 (I1, I2, I4)이다.

<img src="https://images.velog.io/images/nathan29849/post/b1b00842-fb10-4d03-925f-be75bfe6425d/image.png" width="40%">

- 이 때 꼭 개별 구간의 가중치가 가장 큰 구간을 골라야 하는 것은 아니다. (아래 그림 참고)

<img src="https://images.velog.io/images/nathan29849/post/3c04e90c-e1bb-4eb3-b933-fd36af2c6484/image.png" width="40%">

- Greedy 방법은 최적인 해를 보장하지 못한다. (아래 그림 참고)
  <img src="https://images.velog.io/images/nathan29849/post/40588983-b5c1-4002-b3ef-8feeb2ad4b21/image.png" width="40%">

---

> - 주어진 n개의 구간들을 finish time에 의하여 정렬한다.
> - 이들 구간들을 I1, I2, ..., In이라 하고, 구간 Ii의 시작 시간과 끝나는 시간을 Si, Fi라고 하고, 그 weight(가중치)를 Wi라고 하자.

- **부분문제(subproblem)의 정의**
  I1, I2, ..., Ii에 대하여, 겹치지 않으면서 가중치 합이 가장 큰 구간들을 찾아라.

- **부분문제의 최적 해 값(목적 함수)**
  OPT(i) : I1, I2, ..., Ii에 대하여, 겹치지 않는 구간들의 가중치 합의 최댓값

- **주어진 문제의 최적 해 값(목적 함수)**
  OPT(n)

- **부분문제 최적 해 값(목적함수)의 재귀적 정의**
  구간 : (I1, I2, ..., Ij, ..., Ii)
  Ii를 포함하는 경우와 Ii를 포함하지 않는 경우로 나누어 생각한다.
  OPT(i) = max{OPT(i-1), OPT(j) + Wi}

  - 여기서 j는 I1, I2, ..., I(i-1) 중 Ii와 겹치지 않으면서 finish time이 가장 큰 구간의 인덱스이다.
    <img src="https://images.velog.io/images/nathan29849/post/24bb5d66-85cb-49f8-91ea-1e9b2dda136f/image.png" width="40%">

---

### (3) Weighted Interval Scheduling problem : Bottom-Up

- Bottom-up dynamic programming

> Input : n, s1,...,sn, f1,...,fn, w1,...,wn
>
> 1. 구간들을 finish time에 따라 정렬한다 (f1 ≤ f2 ≤ ... ≤ fn)
>    p(i) = largest index j < i such that interval Ij does not overlap interval Ii.
> 2. p(1), p(2), ... , p(n)을 구하고 나서 OPT를 구한다.
> 3. Algorithm Interative-Compute-Opt
>    OPT[0] = 0
>    for i = 1 to n
>    OPT[i] = max(wj + OPT[p(i)], OPT[i-1])

수행시간 : `O(nlogn)`
<img src="https://images.velog.io/images/nathan29849/post/3873e428-8d5a-4777-9218-24e954287959/image.png" width="40%">

- P를 찾을 때 팁 : 뒤에서부터 순차탐색으로 P를 찾으면 너무 오래걸린다.
  따라서 **"이진 탐색"**으로 P를 찾아낸다.
  - 우선 중간의 Interval의 finish time이 맨 마지막 Interval의 start time과 겹친다면, 그 이전의 Interval들을 탐색하고, 겹치지 않는다면, 그 이후의 Interval들을 탐색한다.

```pseudo
1. P배열 구하기 (Basecase 작성)
2-1. OPT[0] = 0
2-2. OPT[i] = max(Wj + OPT[p(i)], OPT[i-1])구하기
```

파이썬 코드로 구현하면 다음과 같다.

```python
def wis(weight_list, n, p):
    opt = [0 for i in range(n)]
    for i in range(n):
        opt[i] = max(weight_list[i]+opt[p[i]], opt[i-1])

    print(opt)

def searchP(time_list, start, end, k, p):
    # 이전의 끝나는 시간이 k의 시작 시간과 겹치지 않을 때
    if start <= end:
        mid = (start+end)//2
        if time_list[mid][1] == time_list[k][0]:
            p[k] = mid
            return p[k]
        elif time_list[mid][1] < time_list[k][0]:
            start = mid + 1
            return searchP(time_list, start, end, k, p)
        else:   # time_list[mid][1] > time_list[k][0]:
            end = mid - 1
            return searchP(time_list, start, end, k, p)
    else:
        return 0

def makeP(time_list, n, p):
    for k in range(n-1, 0, -1):
        start = 0
        end = k
        searchP(time_list, start, end, k, p)
    print(p)


# time_list [[시작시간, 끝나는 시간]]
time_list = [
    [0, 0],
    [1, 4],
    [3, 5],
    [0, 6],
    [4, 7],
    [3, 8],
    [5, 9],
    [6, 10],
    [8, 11]
]

weight_list = [0, 3, 6, 8, 6, 5, 7, 8, 3]

n = len(time_list)

p = [0 for i in range(n)]

makeP(time_list, n, p)

wis(weight_list, n, p)
```
