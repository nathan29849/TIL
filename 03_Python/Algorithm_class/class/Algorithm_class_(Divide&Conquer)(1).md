다룰 내용

> 1.  분할과 정복 방법
> 2.  재귀(Recursion, 순환)
> 3.  분할과 정복에 의한 정렬 알고리즘(병합정렬과 퀵정렬)

# 1. 분할과 정복(Divide and Conquer)

#### 알고리즘

1. 문제를 작은 문제(subproblem)들로 나눈다.
2. 단계 1의 작은 문제들의 해를 재귀적으로(recursively) 구한다.
3. 단계 2에서 구한 작은 문제들의 해를 이용하여 원래 문제의 해를 구한다.

## (1) 리스트(배열)에서 최댓값 찾기

#### 문제 : 리스트(배열) a에서 최댓값을 찾아라. (n: 원소 개수)

<img src="https://images.velog.io/images/nathan29849/post/2eca108b-0eb2-44de-95ba-483dac7c457a/image.png" width="40%">

우선, 파이썬 코드로 다음을 나타내보자. (built-in 함수인 max()를 사용하지 않았다.)
(결국 시간 복잡도는 `O(n)`으로 같음)

```python
def maximum(a, first, last):
	if (first == last):
            return a[first]
        else:	# if (first < last)
            mid = (first + last) // 2
            lmax = maximum(a, first, mid-1)
            rmax = maximum(a, mid+1, last)
            if lmax > rmax:
                return lmax
            else:
                return rmax
```

main program : maximum(a, 0, len(a)-1)을 호출

#### 수행시간 분석

T(n) : maximum(a, 0, n-1)의 수행시간 (원소 비교 횟수)

- n = 2^k일 경우 ( 일반적인 경우와 비슷함 )

```
T(n) = 0 			// n = 1
     = 2T(n/2) + 1 		// n > 1
     = 2[2T(n/2^2) + 1]
     = 2^2 * T(n/2^2) + 2 + 1
     = 2^2 [2T(n/2^3) + 1] + 2 + 1
     = 2^3 * T(n/2^3) + 2^2 + 2 + 1
     ...
     = 2^k * T(n/2^k) + 2^(k-1) + ... + 1
     = 2^k * T(n/2^k) + 2^k
     ...
     n * 1 + n = 2n
```

T(n)은 `O(N)`이다.

## (2) 점화식 풀기 (닫힌 형태 구하기)

#### 예 1

> ```
> f(n) = a (a는 상수) 		if n = 1
> ```

     = f(n-1) + bn (b는 상수) 	if n > 1

```

---

```

f(n) = f(n-1) + bn
= [f(n-2) + b(n-1)] + bn = f(n-2) + b[(n-1) + n]
= [f(n-3) + b(n-2)] + b[(n-1) + n] = f(n-3) + b[(n-2) +(n-1) + n]
= ...
= f(n-k) + b[(n-(k-1)) + ... + (n-1) + n]
= f(n-k) + b(n-k+1 + n)k/2 -> 등차수열의 합 공식
...
(n-k = 1 일 때)
= f(1) + b(n+2)(n-1)/2

```

따라서 f(n)은 `O(N^2)`의 시간 복잡도를 갖는다.

---

#### 예 2
```

n = 2^k 일 경우
f(n) = a (a는 상수) if n = 1
= 2f(n/2) + b (b는 상수) if n > 1

```

---

```

f(n) = 2 _ f(n/2) + b = 2[2f(n/2^2) + b] + b
= 2^2 _ f(n/2^2) + 2b + b = 2^2[2f(n/2^3) + b] + 2b + b
= 2^3 _ f(n/2^3) + 2^2b + 2b + b = 2^3[2f(n/2^4) + b] + 2^2b + 2b + b
...
= 2^k _ f(n/2^k) + (2^(k-1) + ... + 2^2 + 2 + 1)b
= 2^k \* f(n/2^k) + (2^k - 1)b
...
n = 2^k라고 하면,
= nf(1) + (n-1) = 2n - 1

```

따라서 f(n)은 `O(N)`의 시간 복잡도를 갖는다. (n이 2^k가 아닐 경우에도 만족한다.)

---
#### 예 3 (병합정렬의 점화식과 같음)
```

n = 2^k 일 경우
f(n) = a (a는 상수) if n = 1
<= 2f(n/2) + bn (b는 상수) if n > 1

```
---

```

f(n) <= 2 _ f(n/2) + bn
<= 2[2f(n/2^2) + bn/2] + bn
<= 2^2 _ f(n/2^2) + bn + bn
<= 2^2[2f(n/2^3) + bn/2^2] + 2bn
<= 2^3 _ f(n/2^3) +3bn
...
<= 2^k _ f(n/2^k) + kbn
...
n / 2^k = 1 이라고 하면, k = logn
= nf(1) + bn(logn) = an + bnlogn

````

따라서 f(n)은 `O(NlogN)`의 시간 복잡도를 갖는다. (n이 2^k가 아닐 경우에도 만족한다.)

## (3) 이진탐색(Binary Search)
- 정렬되어 있는 리스트(배열) A에서 item과 같은 원소의 위치를 찾아라.
- 분할과 정복을 이용한 기본적인 알고리즘
   - item을 A의 중앙 위치의 원소와 비교하여, 같으면 이 위치 반환
   - item이 A 중앙 원소보다 작으면, 왼쪽 부분에서 이진탐색
   - item이 A 중앙 원소보다 크면, 오른쪽 부분에서 이진탐색

```python
def binarySearch(A, item, left, right):
    if left <= right:
        mid = (left + right)//2
        if item == A[mid]:
            return mid
        elif item < A[mid]:
            return binarySearch(A, item, left, mid-1)
        else:
            return binarySearch(A, item, mid+1, right)
````

수행시간 분석
T(n) : binarySearch(A, item, 0, n-1)을 수행할 때 원소 비교 횟수

```
T(n) = 0 			if n = 1
     <= T(n/2) + 1		if n > 1

대략적인 분석 (X^n을 계산하는 함수 exp3(x,n) 수행시간 분석과 유사함)
...
T(n) <= T(n/2^k) + k
...
n/2^k = 1 (즉, k = log n) 일 때,
T(n) <= T(1) + logn
```

참고 : [exp3(x,n)을 다루는 부분](https://velog.io/@nathan29849/Python-Algorithm-class-%EC%9E%AC%EA%B7%80-Recursion)

수행시간 : item과 A의 원소 비교횟수 `O(log N)`
