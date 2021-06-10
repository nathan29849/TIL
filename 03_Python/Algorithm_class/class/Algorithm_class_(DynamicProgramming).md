# Dynamic Programming (동적 계획법)

> 1.  개요
> 2.  피보나치 수열
> 3.  이항계수

## 1. 개요

- 분할과 정복 방법은 Top-Down Design으로써 문제를 부분문제(subproblem)들로 나누고 이들 부분문제들의 해를 recursive하게 구하여 이들 해들로부터 원래의 문제 해를 구한다.
  - 작은 문제들이 **독립적**이다.
- 동적 계획법도 주어진 문제의 해를 부분문제(subproblem)들의 해를 이용하여 구한다.(+recursion)
  - 분할과 정복과는 달리, 주어진 문제의 해를 구하는데 필요한 부분문제들은 서로 **독립적이지 않다**(겹친다.) (부분문제들이 overlap 된다.)

### (1) 두 가지 접근 방법

> 1.  **Memoization**
>     기본적으로 작은 문제들의 해를 이용하기 때문에 recursion을 사용한다.
>     이 부분문제들의 해를 구한 뒤 배열에 이들을 기록하고, 필요한 값을 찾아온다.

> 2.  **Bottom-Up**
>     작은 부분문제들부터 시작하여 큰 부분문제들까지 해를 차례대로 구한다.
>     부분문제들에 대한 해를 구하면 이를 테이블에 저장한다.
>     부분 문제에 대한 해를 구할 때 필요한 작은 부분문제들의 해는 다시 계산하지 않고, 테이블을 참조한다.

## 2. 피보나치 수열

- f_0 = 0, f_1 = 1
- f_n = f_n-1 + f_n-2 (n>=2)

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

(a+b)/a = a/b 에서 a:b가 a+b:a와 같도록 하는 것이 "황금비율"이다.
이 황금비율은 피보나치 수열과 동일하다고 보면 된다.

### 구현 방법 1 (비효율적 방법)

```python
def fib1(n):
   if n == 0 or n == 1:
      return n
   else:
      return fib1(n-1) + fib1(n-2)
```

- 방법 1이 비효율적인 이유 : 동일한 부분문제에 대한 해를 여러번 반복하여 구한다.
- fib1(n-1)과 fib1(n-2)가 overlap한다. (동일한 부분문제를 가짐)
- 시간 복잡도 : 수행시간 T(n) = T(n-1) + T(n-2) + c(상수)

따라서 지수승 알고리즘 `O(2^n)`을 갖는데, 이는 n이 커질수록 시간이 기하급수적으로 증가한다.

### 구현 방법 2 (효율적 방법 - memoization 활용)

```python
def initialize(n):
    lookupTable = [-1 for i in range(n+1)]
    return lookupTable


def fib(n, lookupTable):
    if lookupTable[n] != -1:
        return lookupTable[n]

    else:
        if n <= 1:
            return n
        else:
            lookupTable[n] = fib(n-1, lookupTable) + fib(n-2, lookupTable)
            return lookupTable[n]

def main():
    n = int(input())
    lookupTable = initialize(n)
    print(fib(n, lookupTable))

if __name__ == "__main__":
    main()
```

시간 복잡도 : `O(n)`

### 구현 방법 3 (효율적 방법 - Bottom up 활용)

```python
def fib(n):
    if n <= 1:
        return n
    F = [0 for i in range(n+1)]
    F[0] = 0
    F[1] = 1

    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]

    return F[n]

def main():
    n = int(input())

    print(fib(n))

if __name__ == "__main__":
    main()
```

시간 복잡도 : `O(n)`

### 구현 방법 4 (O(1)의 메모리 공간 사용)

```python
def fib(n):
    if n<= 1:
        return n

    # prev_prev = 0
    # prev = 1

    # for i in range(2, n+1):
    #     current = prev_prev + prev
    #     prev_prev = prev
    #     prev = current

    prev = 0
    current = 1
    for i in range(2, n+1):
        current, prev = current + prev, current


    return current

def main():
    n = int(input())
    print(fin(n))

if __name__ == "__main__":
    main()
```

시간 복잡도 : `O(n)`

O(1)만큼의 공간을 사용하기 때문에 `In-place` 알고리즘이다.
( ≤ c log N 정도의 추가 메모리를 사용할 때 in-place 라고 한다. )

출처: https://algs4.tistory.com/41 [알고리즘 노트]

## 3. 이항계수

### 정의

1. nCk : n개의 원소에서 k개를 선택하는 경우의 수
2. 원소 n을 선택하는 경우들과 선택하지 않는 경우들로 나눌 수 있다.

   - nCk = (n-1)C(k-1) + (n-1)Ck
   - ex. n = 4, k = 3
     4를 선택하는 경우들 : {1, 2, 4}, {1, 3, 4}, {2, 3, 4}
     4를 선택하지 않는 경우들 : {1, 2, 3}

   - 정의 2의 재귀적 정의 (부분문제 각각이 중복되어 계산된다.)

```python
   def C(n, k):
      if k == 0 or n == k:
         return 1
      else:
         return C(n-1,k-1) + C(n-1, k)
```

- 시간 복잡도 : 수행시간 T(n) = T(n-1) + T(n-2) + c(상수)
  - `O(2^n)` : 지수승의 시간 복잡도를 갖는다.

### 정의 2, 동적 계획법을 사용하기

- 2차원 배열의 이용
  - iCj 를 배열 원소 C\[i]\[j]에 저장

```python
def dpBinomial(n, k):
    C = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    print(C)
    return C[n][k]



def main():
    n, k = input().split()
    n, k = int(n), int(k)
    print(dpBinomial(n, k))


if __name__ == "__main__":
    main()
```

시간 복잡도 : `O(n*k)` ( 사실상 n X k 배열을 만드는 것이므로.. )

<img src="https://images.velog.io/images/nathan29849/post/9129f1ad-cb31-4cec-b9a3-994de45dfa52/image.png" width="70%">

## (추가) 동적 계획법

- 동적 계획법은 주로 최적화(optimization) 문제를 해결하는 데 주로 사용한다.
  - 최적화 문제 : 목적 함수 값을 최대 혹은 최소로 하는 해를 구하는 문제
- 동적 계획법은 다음의 최적화 원칙이 적용되는 문제의 해를 구하는 데 사용된다.

  - 최적화 원칙(Principle of Optimality)
    문제의 최적 해는 모든 부분 문제의 최적 해를 포함한다.

  - 문제의 최적 해를 구하는 일련의 선택들을 D1, D2, ... Dn-1, Dn이라 하면, 첫 번째 선택 D1을 한 후의 상태에서 D2, ... Dn은 최적해가 된다.

- 동적 계획법을 이용한 문제 해결은 아래의 4단계를 거친다.
  1.  최적 해의 구조를 파악한다.
  2.  최적해의 (목적함수) 값을 재귀적으로 정의한다.
  3.  단계 2의 재귀적 정의로부터 최적 해의 (목적함수) 값을 bottom-up 혹은 memoization으로 구하면서 테이블에 저장한다.
  4.  단계 3에서 구한 정보를 이용하여 최적 해를 찾는다.

\*\* 단계 1 - 3은 동적 계획법으로 해를 구할 때 필수적인 과정.
(단계 4는 최적 해의 목적 함수 값만 구하는 경우는 필요 없고, 최적 해를 찾고자 하는 경우에 필요)
