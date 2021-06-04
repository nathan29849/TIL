# 1. 재귀(recursion, 순환)

설명 : 문제의 해를 부분문제(subproblem, 작은 크기의 입력에 대한 동일한 문제)의 해를 이용하여 해결하는 방법.

ex. 0 이상의 정수 n에 대한 n!(팩토리얼) 정의
n! = 1 ... if n = 0 (base case)
n! = n\*(n-1)! ... if n > 0 (recursive case)

## (1) n!을 구하는 Recursive function

- recursive function : 자기 자신을 호출하는 함수

```python
def fact(n):
# Precondition(사전조건) : n >= 0.
    if n == 0:	# base case
    	return 1
    else:		# recursive case(general case)
    	return n * fact(n-1)

```

#### 수행시간 분석

n! 계산에서 기본 연산 : 두 정수의 곱셈
T(n) : fact(n)을 수행할 때 수행되는 기본 연산의 수

```
T(n) = 0	# n = 0
     = 1 + T(n-1) # n > 0
```

위의 점화식으로부터 T(n)을 구한다.

```
T(n) = 1 + T(n-1)
     = 1 + [1 + T(n-2)]
     = 2 + T(n-2)
     ...
     = k + T(n-k)
```

n-k = 0이라면, k = n이다. 따라서 T(n) = n + T(1) = n 이므로

시간 복잡도는 O(N)을 갖는다.

## (2) gcd (최대 공약수, greatest common divisor)

- 양의 정수 a, b의 최대 공약수 gcd(a,b)의 재귀적 정의

```
gcd(a,b) = b	// a가 b로 나누어지면 (base case)
	 = gcd(b, a%b) // 그렇지 않으면 (recursive case)
```

---

```python
def gcd(a, b):
    if (a%b) == 0:
    	return b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
```

#### 수행시간 분석

기본 연산 : 대략적 분석
a >= b라 하자.
gcd(a,b) = gcd(b, a%b) = gcd(a%b, b%(a%b))
a%b <= a/2이다.
그 이유는? : gcd를 2번 호출하면 gcd 첫 번째 매개변수가 a/2보다 같거나 작게 된다.

gcd(a, b)의 시간 복잡도 : O(log(max(a,b))

<img src="https://images.velog.io/images/nathan29849/post/aa36d668-7e49-429a-b6be-494a8750a3fd/image.png" width="40%">

시간 복잡도 증명에 관한 참고 : [Onsil's blog - programming](https://onsil-thegreenhouse.github.io/programming/algorithm/2018/04/01/gcd/)

## (3) x^n 계산

### (3-1) 0이상 정수 n에 대하여 x^n 계산 (재귀 사용 X)

```python
def exp1(x, n):
    result = 1
    for i in range(1, n+1):
    	result *= x

    return result
```

수행시간 : `O(n)`

---

### (3-2) x^n의 재귀적 정의(n>=0):

```
x^n = 1 		if n = 0
    = x*x^(n-1)		if n > 0
```

파이썬으로 재귀 사용하기

```python
def exp2(x, n):	# n 은 0이상의 정수
    if n == 0:
        return 1
    else:
        return x*exp2(x, n-1)
```

수행시간 분석
T(n) : exp2(x, n)을 수행할 때 곱셈의 수

```
T(n) = 0				// n = 0이면,
     = 1 + T(n-1)		 	// n > 0이면,
```

즉 T(n)은 `O(N)`이다.

---

### (3-3) 홀수 짝수로 나누어 정의

x^n의 재귀적 정의(n>=0)

```
x^n = 1			if n = 0
    = (x^n/2)^2 	if n is even(짝수)
    = x*x^(n-1) 	if n is odd(홀수)
```

파이썬으로 나타내기

```python
def exp3(x, n):
    if n == 0:
    	return 1
    elif (n%2 == 0):
    	temp = exp3(x, n/2)
        return temp*temp
    else:
    	return x*exp3(x, n-1)
```

수행시간의 대략적 분석
T(n) : exp3(x, n)을 수행할 때 두 정수 곱셈 수

```
T(n) = 0		n = 0이면
     <= 2 + T(n/2)	n > 0 이면 (n을 짝수 홀수 구분안하고 대략적으로 나타냄)

...
T(n) <= 2 + T(n/2)		// n을 짝수 홀수 구분안하고 대략적으로 나타냄
     <= 2 + [2 + T(n/2^2)]
     <= 2 + 2 + T(n/2^2)
     <= 2 + 2 + [2 + T(n/2^3)]
     <= 2 + 2 + 2 + T(n/2^3)
     ...
     <= 2*k + T(n/2^k)
```

즉, n/2^k = 1 이면, 2^k = n이다. (k = logn)

따라서 T(n) <= 2\*logn + T(1) ( T(1) = 1 ) 이므로
`O(logN)`의 시간 복잡도를 갖는다.

### (3-4) X^n 계산

- x^n의 재귀적 정의

```
x^n = 1 		if n = 0
    = (x^2)^n/2 	if n is even(짝수)
    = x*(x^2)^(n-1)/2	if n is odd(홀수)
```

파이썬 코드로 나타내기

```python
def exp4(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exp4(x*x, n/2)
    else:
        return x*exp4(x*x, (n-1)/2)
```

## (4) 이진탐색 (binary search)

- 정렬되어 있는 리스트 A에서 item과 같은 원소의 위치를 찾아라.

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
```

binarySearch(A, item, 0, n-1)을 호출
수행시간은 `O(logN)`
