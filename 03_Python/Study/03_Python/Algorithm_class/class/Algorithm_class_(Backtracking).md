# Backtracking

## 🍉 백트래킹 설명

> 백트래킹은 어떤 테크닉인데 ‘조합 알고리즘 문제’에 대해 모든 가능한해를 나열하는 것이다. 그렇다. 백트래킹은 모든 조합의 수를 살펴보는 것인데 단 조건이 만족할 때 만이다. 모든 경우의 수를 모두 찾는 것보다 ‘경우에 따라' 훨씬 빠를 수 있다. 왜냐하면 조건이 만족하는 경우라는 조건이 있기 때문이다.

참고 : [Jeong Dowon's medium](https://jeongdowon.medium.com/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-backtracking-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-13492b18bfa1)

- 해의 형태는 n-tuple(x1, 2, ..., xn)이고,
  각 xi는 어떤 유한집합 Si에서 선택된다.

- 기준함수(criterion function)인 P(x1, x2, ..., xn)를 최대(혹은 최소 혹은 만족하는)화 하는 해를 구하는 문제를 해결하는데 적용하는 방법으로, 효율적인 알고리즘이 존재하지 않을 경우에 사용한다.

- mi를 Si의 크기라 하자. 그러면 가능한 후보 해가 m= m1m2...mn개 있다.
  Backtracking 알고리즘은 문제의 입력에 대한 해의 공간을 체계적으로(주로 DFS) 탐색함으로서 m보다 매우 작은 횟수의 시도로 해를 찾는다.

---

## 🍉 Ex. N-Queens 문제

- nxn 격자에 다음 조건을 만족하도록 n개의 Queen을 놓아라

  - 조건 1) 같은 행에 두 개의 Queen이 놓여서는 안된다.
  - 조건 2) 같은 열에 두 개의 Queen이 놓여서는 안된다.
  - 조건 3) 같은 대각선에 두 개의 Queen이 놓여서는 안된다.

- 해 : (x1, x2, ..., xn)
  여기서 xi(1≤i≤n)는 i번째 행에 놓여지는 Queen의 열의 위치이다.

  - (1≤xi≤n)
  - 해 공간의 크기 n^n 혹은 n!

- 예 : 4-Queen 문제
  해(x1, x2, x3, x4) = (2, 4, 1, 3)
  <img src="https://images.velog.io/images/nathan29849/post/3604159e-1cb6-4a5c-b27d-9edfbaa50d18/image.png" width="30%">
  - x1 : 1~n까지의 값을 가질 수 있음 -> 후보해 : n개
  - x2 : 1~n까지의 값을 가질 수 있음 -> 후보해 : n개
  - x3 : 1~n까지의 값을 가질 수 있음 -> 후보해 : n개
  - x4 : 1~n까지의 값을 가질 수 있음 -> 후보해 : n개
    - 대략 `n^2`의 후보해가 존재한다.
  - 디테일하게 구하면, 이전에 선택한 값을 더 이상 선택하지 않도록 할 수 있다.
    - Permutation으로 가능하다. (후보해가 `n^2`보다는 적을 것이다.)
    - 허나 그렇다고해서 무조건 후보해가 다 답이라고 할수는 없다.
    - Ex.
    | O   |     |     |
    | --- | --- | --- |
    |     | O   |     |
    |     |     | O   |

---

## 🍉 백트래킹 알고리즘

- 상태공간트리(State Space Tree) : 모든 가능한 해(solution space:해공간)를 트리로 구성한 것
- 체계적인 탐색 방법 (DFS with bounding function)
  - 문제의 state space(상태공간)을 체계적으로 탐색
  - 탐색시, 해로 도달하지 못하는 것을 발견할 경우, 탐색 공간을 prune(가지치기 : Bounding function)을 이용하여 탐색이 필요없는 부분을 제외시킨다.
    - root부터 leaf까지 DFS로 탐색하면서 노드 생성시마다 답이 존재할 수 있는지 판단.(Bounding function을 잘 만들어야 효율적)

<img src="https://images.velog.io/images/nathan29849/post/74d74081-f4df-4765-97e9-0a32e6667017/image.png" width="50%">

### 🍳 백트래킹 알고리즘 설명

- 기본적으로 백트래킹 알고리즘은 **재귀(recursion)** 를 사용한다.
- 알고리즘의 기본 골격

<img src="https://images.velog.io/images/nathan29849/post/9472c068-4d9d-42f2-8ba5-cdd43090aa19/image.png">

- T(x1, x2, ..., xk) : the set of all possible values for xk+1
- Bk : Bounding function
  - 만약 root로부터 현재 노드까지의 경로(x1, x2, ..., xk)에 대하여, 해를 계속 찾아볼 필요가 있는지를 판단하는 함수로 참 혹은 거짓을 반환
  - Bk(x1, x2, ..., xk)가 거짓이면 이 경로는 더 이상 확장하지 않음
- Backtrack(x, k+1, n)을 호출(DFS, recursion)

### 🍳 N-Queens 문제에 대한 백트래킹 알고리즘

#### Pseudo code : nQueen(x, k, n)

```pseudo
Algorithm nQueen(x, k, n):
   // xk가 가질 수 있는 값들의 집합 : T={1, 2, ..., n}
   for i to n (xk가 가질 수 있는 값이 i)
      if (place(x, k, i) // Place(x,k,i): Bounding function
         x[k] = i;
      if (k == n) // 해를 찾은 경우
         x[1], ..., x[n]을 출력
      else
         nQueens(x, k+1, n)
```

<img src="https://images.velog.io/images/nathan29849/post/c7b51a19-ce2d-4f4f-8aa0-b5780504f652/image.png" width="50%">

#### Pseudo code : place(x, k, i)

```pseudo
Algorithm place(x, k, i):
   for j = 1 to k-1 // (각각의 Queen에 대해서)
      if((x[j] == i) or abs(x[j] - i) == abs(j-k))
         return false
      return true
```

- x\[j] == 1
  - 같은 열이면 return false
- abs(x\[j] - i) == abs(j-k)
  - 같은 대각선이면 false

#### 🤚여기서 잠깐!!🤚

- 대각선을 구하기 위해서는 `두 정점의 기울기 = 1 or -1`임을 이용하자.
  <img src="https://images.velog.io/images/nathan29849/post/07a4be95-7cd5-4056-b357-b1c94278b6cc/image.png" width="80%">

<img src="https://images.velog.io/images/nathan29849/post/25e4225a-f565-4a1b-8046-95f1930b5c79/image.png" width="80%">

---

## 🍉 백트래킹 예제

backtracking 관련한 간단한 문제

문제 1: 1, 2, ..., n의 모든 순열을 출력하시오. : nPn = n!

문제 2: 1, 2, ..., n에서 r개의 서로 다른 숫자를 선택하여 나열한 모든 r-순열을 출력하시오. : nPr = n!/(n-r)!
-> Bound function을 이용해 prune(가지치기)를 해야한다.

문제 1에 대한 예제 프로그램은 아래 코드를 참고하시오.

```python
def permutation(p, k, n, used):
# 순열 p[0],...,p[k-1]이 정해진 상태에서 p[k-1] ...p[n-1]의 모든 순열을 생성
    if(k <= n-1):                                                       # 0 <= 2
        for i in range(1,n+1):
            if not used[i]:      # i가 순열에 사용되지 않은 수이면              # i = 1
                p[k] = i                                                # p[0] = 1
                used[i] = True
                if(k == n-1):  # 하나의 순열을 생성한 경우
                    for j in range(0,n):     # 순열 출력
                        print(p[j], end = ' ')
                    print()
                    used[i] = False  # False로 두는 이유는?    "가능한 후보해로 만들기 위해"
                    return # continue 문장과의 차이점은?   "더이상 함수를 실행하지 않고 종료" continue는 "for문의 다음 i를 실행"
                permutation(p, k+1, n, used)                            # 1 <= 2
                used[i] = False      # False로 두는 이유는?
                # 이미 두 번째 for문 안에서 가능한 후보해로 만들었다 하더라도 첫 번째 for문이 아직 남았다면,
                # 가능한 후보해가 더 필요한 것이므로 False로 두어 다음 i가 들어가는 데에 지장이 없게 한다.

def main():

    n = int(input())
    p = [None] * n         # 하나의 순열을 저장하는 리스트
    used = [None]*(n+1) # 숫자 i가 순열에 사용되었는지를 나타내는 리스트

    for i in range(1,n+1):
        used[i] = False

    permutation(p, 0, n, used)

if __name__ == '__main__':
    main()
```

문제 2 예제 코드(문제 1에서 r부분 추가)

```python
def permutation(p, k, n, used, r):
# 순열 p[0],...,p[k-1]이 정해진 상태에서 p[k-1] ...p[n-1]의 모든 순열을 생성
    if(k <= n-1):
        for i in range(1,n+1):
            if not used[i]:      # i가 순열에 사용되지 않은 수이면
                p[k] = i
                used[i] = True
                if(k == r):  # 하나의 순열을 생성한 경우  (**r개의 원소로 이루어져있는지 체크**)
                    for j in range(0,r):     # 순열 출력 (**r개의 원소를 출력**)
                        print(p[j], end = ' ')
                    print()
                    used[i] = False  # False로 두는 이유는?    "가능한 후보해로 만들기 위해"
                    return # continue 문장과의 차이점은?   "더이상 함수를 실행하지 않고 종료" continue는 "for문의 다음 i를 실행"
                permutation(p, k+1, n, used, r)                            # 1 <= 2
                used[i] = False      # False로 두는 이유는?
                # 이미 두 번째 for문 안에서 가능한 후보해로 만들었다 하더라도 첫 번째 for문이 아직 남았다면,
                # 가능한 후보해가 더 필요한 것이므로 False로 두어 다음 i가 들어가는 데에 지장이 없게 한다.

def main():

    n = int(input())    # n개의 수 중에서
    r = int(input())    # r개를 택하여 나열하는 방법의 수를 구해보자.
    p = [None] * n         # 하나의 순열을 저장하는 리스트
    used = [None]*(n+1) # 숫자 i가 순열에 사용되었는지를 나타내는 리스트

    for i in range(1,n+1):
        used[i] = False

    permutation(p, 0, n, used, r)

if __name__ == '__main__':
    main()
```
