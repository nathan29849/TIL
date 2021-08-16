> 1주차 : 개론, 시간복잡도

# 1장. Introduction

---

## 1. 알고리즘

> - 문제 해결 절차를 체계적으로 기술한 것

- 문제의 요구조건
  - 입력과 출력으로 명시할 수 있음
  - 알고리즘은 입력으로부터 출력을 만드는 과정을 기술

<br/>

#### < 알고리즘 단어의 유래 >

> 알-콰리즈미(al-Khwarizmi) : 페르시아 과학자, 근대 수학의 아버지

<br/>

### pseudo-language(의사 코드)

> - 알고리즘 기술을 위한 언어

- 프로그래밍 언어보다 융통성이 있음
- 모호함이 없이 명령어를 정의하면 됨
  (의사코드는 실제 프로그래밍 언어처럼 엄격한 문법을 따를 필요X)

#### pseudo-language 구성

- 대입문 : A = B, A <- B
- 연산자 :

1.  산술연산자(+, -, \*, /, %)
2.  비교연산자(>, <, ==, != 등)
3.  논리연산자(and, or, nor)

- 비교문 : if then (else) 등
- 반복문 : for, while문
- return문
- 함수 정의 및 호출
- 자연어 명령어 : Set total to zero, Inintialize total to zero

<br/>

---

## 2. 알고리즘 평가기준

> ##### <span style="color:green">1) 정확성(Correctness)</span>

##### <span style="color:red">2) 수행시간</span>

##### <span style="color:red">3) 사용하는 메모리 공간</span>

##### <span style="color:green">4) 최적성(Optimality)</span> : 해당 문제를 푸는데 있어 "가장 적은 수의 기본 연산"으로 수행되는 알고리즘

Algorithm Efficiency 평가 기준 : **"수행시간"**과 **"사용하는 메모리 공간"**

- 이들은 입력 크기와 관계가 있음

<br/>

---

## 3. 알고리즘의 효율성

문제의 해를 구하는 여러 알고리즘이 있을 때, 어떤 알고리즘이 좋은가?

> 문제
> 입력 : 배열 a에 저장된 정수들 ( a = [25, 90, 53, 11, 23] )
> 출력 : 최솟값

1. 알고리즘 A (A, B, C 중 가장 효율적)

```pseudo
Algorithm Max(a, n)
m = a [0]
for i = 1 to n-1 // n은 입력크기
	if m > a[i] then m <- a[i]
output m
```

2. 알고리즘 B

- 입력 자료를 오름차순으로 정렬한다.
- 정렬된 자료의 첫 번째 원소를 반환한다.
- 정렬 알고리즘 사용하기(선택정렬, 버블정렬, 삽입정렬등 - 2주차 때 배움)

3. 알고리즘 C

- 배열 a의 각 원소 a[i]에 대하여, 이 원소가 최솟값인지 검사

```pseudo
Algorithm Max(a, n)
i = -1
flag = true

while(flag):
	i += 1
    	m = a[i]
    	flag = false
    	for j = 0 to n-1:
    		if m > a[j] then flag = true
output m
```

<br/>

---

## 4. 알고리즘의 수행시간 분석

알고리즘을 프로그래밍 언어로 구현하여, 직접 컴퓨터에서 실행하는 수행시간 측정

```python
# Python기준
import time
start = time.time()
...
fininsh = time.time()
print(finish - start) // 단위 : second
```

<br/>

### 일반적인 수행시간 분석

> - 수행되는 연산(step, operation, primitive operation)의 수를 계산

- 장점 : 코딩 환경에 독립적이고 **구현을 하지 않은 상태**에서 분석
- 수행 시간의 단위는?
  - 기본연산(비교, 사칙 연산등) : 알고리즘 수행시간에 가장 큰 영향을 미치는 연산

### 입력에 따른 수행시간 분석

- 수행시간은 입력의 크기 n과 관계가 있음 (n의 크기와 수행시간은 비례)
- 입력 형태와도 관련이 있음 (ex. 정렬된 입력 or 역순 정렬된 입력 등에 따라 달라짐)<br/>

1. 최악의 경우 수행시간 (worst case running time)
   - 모든 가능한 입력에 대하여 실행되는 기본 연산 수의 최댓값
   - W(n)으로 표기
   - 장점 : 수행시간의 상한(upper bound)을 제공, 수행시간 측정 용이
   - 단점 : 정확한 수행시간 보다는 수행시간의 최댓값만 제시
   - 알고리즘 수행시간 분석은 보통 최악의 경우에 함 (실제에서도 유용)
     <br/>
2. 평균적인 경우 수행시간 (average case running time)
   - 모든 가능한 입력에 대하여 실행되는 기본 연산 수의 평균값
   - A(n)으로 표기
   - 최악의 경우 수행시간 분석보다 구하기 어려움
     <br/>
3. 최선의 경우 수행시간 (best case running time)
   - 모든 가능한 입력에 대하여 실행되는 기본연산 수의 최솟값
   - B(n)으로 표기

- 알고리즘의 수행시간(running time)은 T(n)으로 표기
  T(n) = 실행되는 기본 연산의 개수 <= W(n)
- 수행시간 대신 시간복잡도(time complexity)라는 용어를 사용하기도 함 [점근적인 분석]

<python 예시>

```python
# 1. 리스트에서 item과 같은 리스트 원소의 위치를 반환. Item과 같은 원소가 없으면 -1을 반환
def seqSearch(list, item):
	for i in range(len(list)):
    	if(list[i] == item):
        	return i
	return -1


# 2. 리스트(배열)에서 최대값 찾는 문제
Algorithm arrayMax(list, n):
	m = list[0]
    for i in range(1, len(list)):
    	if m < list[i]:
        	m = list[i]
	return m
```

1. 기본 연산 : item과 리스트 원소의 비교
   [최악의 경우 수행시간] W(n) = n

2. 기본연산 : 두 원소의 비교
   [최악의 경우 수행시간] W(n) = n-1
   -> 위의 두 경우에는 입력 형태가 역순이 되더라도 수행시간이 같음
   <br/>

---

## 5. 점근적(asymptotic) 증가율에 의한 함수 분류

입력 크기가 작을 때는 알고리즘 효율성이 중요하지 않지만, 입력 크기가 충분히 크다면 알고리즘의 효율성이 중요하다.

즉, 증가율에 의한 분석을 **점근적 분석(Asymptotic Analysis)**라고 한다.

<center><함수의 증가율 비교 그래프 1><img src ="https://images.velog.io/images/nathan29849/post/fec5e958-9edc-4749-9693-97eae26d6542/image.png" width="70%">
</center>
  
<br/>
  
<center><함수의 증가율 비교 그래프 2><img src ="https://images.velog.io/images/nathan29849/post/b30ddbea-5ccc-4d2a-b94d-8db3c4ce6c08/image.png" width="70%"></center>

### 증가율에 의한 함수 표기법

#### 1. "Big-O" notation(표기)

- O(f(n)) : 어떤 실수 c와 음이 아닌 정수 n0에 대하여,
  n >= n0인 모든 n에 대하여 c\*f(n) >= g(n)을 만족하는 함수 g의 집합
- 즉, 증가율이 f(n) 보다 작거나 같은 함수의 모임
- 기껏해야 f(n)의 비율로 증가하는 함수들의 집합
- 함수 g는 함수 f보다 빠르게 증가하지 않는다. (상수 비율의 차이는 무시)
<center><img src ="https://images.velog.io/images/nathan29849/post/6ef53e3b-b3f9-4afd-a471-c13f71c3fea4/image.png"></center>

* 최고차 항만 남기고 나머진 모두 무시.
* 최고차 항에 곱해진 상수도 무시.
* 가능한 tight하게 나타냄 (Tight하지 않은 만큼 정보의 손실이 일어남)

  <center><img src="https://images.velog.io/images/nathan29849/post/e16c58d7-9bb9-465b-b605-93995f2bc165/image.png"></center><br/>

#### 2. "Big-Ω" notation(표기)

- Ω(f(n)) : 어떤 실수 c와 음이 아닌 정수 n0에 대하여,
  n >= n0인 모든 n에 대하여 g(n) >= c\*f(n)을 만족하는 함수 g의 집합
- f(n)보다 함수 증가율이 크거나 같은 함수의 모임
- 적어도 f(n)의 비율로 증가하는 함수들의 집합
- 함수 g는 f보다 느리게 증가하지 않는다.
  <br/>

#### 3. "Big-Theta" notation(표기)

- θ(f(n)) : n ≥ n0인 모든 정수 n에 대하여,
  c1*f(n) ≤ g(n) ≤ c2*f(n)을 만족하는 세 수 n0, c1, c2가 존재하면,
  g(n)의 원소는 θ(f(n))에 속한다.
- f(n)과 함수의 증가율이 같은 함수의 모임
- 정확하게 f(n)의 비율로 증가하는 함수들의 집합
- Formal definition : θ(f(n)) = O(f(n)) ∩ Ω(f(n))
- 함수 g는 함수 f와 같은 정도로 증가한다.
  <br/>

> 점근적인 분석에서 실행되는 기본 연산 수에 의한 분석과
> 실행되는 문장 수에 의한 분석은 동일하다.

```python
# 예제 1
S = 0
for i in range(1, n+1):
	for j in range(1, n+1):
		S = S + 1 # 기본 연산
# 예제 2
i = 1
while (i <= n):
	S = S + 1 # 기본 연산
	i = i * b
```

예제1

- 실행되는 기본 연산의 수 : n^2
- 수행시간 (시간 복잡도 Time Complexity) : θ(n^2)

예제2

- 실행되는 기본 연산의 수 : log(b)n (밑이 b, 진수가 n인 로그)
- 수행시간 (시간 복잡도 Time Complexity) : θ(log(2)n) (밑이 2, 진수가 n인 로그)

```python
# 예제 3 : n개의 키들로 구성된 리스트 list에서 어떤 주어진 키(x)가 있는 위치를 찾아라.
# 3-1) 순차적 탐색(Sequential Search)
for index in range(len(list)):
	if x == list[index]:
		break
# 3-2) 이진탐색(Binary Search)
def binarySearch(list, key):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right)//2
        if key == list[mid]:
            return True # return mid
        elif key < list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
```

예제 3-1<br/>

- 시간 복잡도 : O(n)
- 최악의 경우 수행시간 : W(n) = θ(n) <br/>  
  예제 3-2
- 시간 복잡도 : O(log n)
- 최악의 경우 수행시간 : W(logn) = θ(log n)

<center>  
<img src="https://images.velog.io/images/nathan29849/post/9d3707e2-5ea2-4e25-b1ad-335a8571aee4/image.png" width="70%"></center>


> **수행시간 분석**
>
> > T(n) = 입력 크기 n인 정렬된 리스트에서 이진 탐색을 하는데 수행되는 키 비교 횟수
> > T(n)은 1번의 비교 후에 리스트의 1/2 즉, 앞 부분이나 뒷 부분을 재귀 호출하므로 아래와 같이 된다.

T(n) ≤ T(n/2) + 1
T(1) = 1
T(n) ≤ T(n/2) + 1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≤ [T(n/2)/2 + 1] + 1 = [T(n/2^2)] + 2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;≤ [T(n/2^2)/2 + 1] + 2 = [T(n/2^3)] + 3  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ≤ ... ≤ T(n/2^k) + k = T(1) + k

if n = 2^k, k = log n
= 1 + log n = O(log n)

#### 예제 설명 : 양의 정수 n이 소수(prime number)인지 판별하라

(소수 : 1과 자기 자신 이외의 약수를 가지지 않는 1보다 큰 자연수)

```python
# 예제 4-1)
prime = True
for i in range(2,n):
    if n%i == 0:
        prime = False
        break
if prime:
    print('Prime')
else:
    print("Not Prime")

# 예제 4-2)
prime = True
i = 2   # 2부터 연산을 시작하므로 (√n - 1)번 연산 -> O(√n)
while i * i <= n:   # i라는 약수를 가지고 있는지 보는 것. (i가 √n이 될 때까지 반복)
    if n % i == 0:
        prime = False
        break
    i += 1

if prime:
    print('Prime')
else:
    print("Not Prime")
```

예제 4-1

- 기본연산 : n % i
- 수행시간 : O(n)<br/>

예제 4-2

- 기본연산 : n % i
- 수행시간 : O(√n)

> 예제 4-2 알고리즘에 사용된 성질 증명
>
> > n이 소수가 아니면 2이상 √n 이하의 약수를 가진다.
> > 증명 : n은 소수가 아니므로 두 자연수 p,q(2≤p≤q)의 곱으로 나타낼 수 있다.
> > n = pq
> > p는 √n보다 작거나 같다. 그렇지 않다면,
> > n = pq > √n \* √n = n이 되어 모순이다.

#### 예제 설명 : 리스트 data[0]부터 data[n-1]까지 n개의 원소(실수)들에 대하여 연속하는 원소들의 합 중에서 최댓값을 구해라

```python
# 예제 5-1)
f = open("input.txt", "r")
data = f.read()
data = data.split()
maxSum = int(data[1])
n = len(data)
for i in range(1,n):
    for j in range(i,n):
        sum = 0
        for k in range(i, j+1):
            sum += int(data[k])

        if (maxSum < sum):
            maxSum = sum
print(maxSum)

# 예제 5-2) pseudo code
maxSum = "-♾"
for i = 0 to n-1
	sum = 0
	for j = i to n-1
		sum = sum + data[j]
		if (maxSum < sum) then
  			maxSum = sum


# 예제 5-3)
maxContigSum = []
# data[0] ~ data[i]까지의 원소들에 대하여, data[i]에서 끝나는 연속하는 원소들의 합 중에서 최댓값
maxContigSum[0] = data[0]
for i in range(1, n):
    if (maxContigSum[i-1] > 0):
        maxContigSum[i] = maxContigSum[i-1] + data[i]
    else: // 0보다 작으면 청산. (새로 시작하는게 맞다.)
        maxContigSum[i] = data[i]

maxSum = maxContigSum[0]
for i in range(1, n):
    if (maxSum < maxContigSum[i]):
        maxSum = maxContigSum

```

<br/>

예제 5-1

- 시간 복잡도 : θ(n^3)

예제 5-2

- 시간 복잡도 : θ(n^2)
- 5-1과의 차이점 : k를 따로 for문으로 돌리지 않고 j를 돌리는 for문 속에서 maxSum과 sum을 비교함으로써 시간 복잡도를 한 차수 낮춤

예제 5-3

- 시간 복잡도 : θ(n)
- 5-1, 5-2와의 차이점 : maxContigSum이라는 list 자료형을 사용하여, 첫 번째 for문으로 data[0]~data[i]의 범위에 해당하는 합들을 각각 저장한 후 두 번째 for문을 통해 인덱스를 돌며 최댓값을 도출해 내었음

---

---

### 수행시간 분석 예제

```python
# 수행시간 분석 예제
# 1. O(1), θ(1)
S = n(n+1)/2

# 2. O(n), θ(n)
S = 0
for i in range(1, n+1):
    S = S + 1

# 3. O(n^2), θ(n^2)
S = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        S = S + j

# 4. O(log n), θ(log n) ... 이진수의 표현과 관련이 있음(이진수 자릿수를 역순으로 출력.)
while n != 0:
    print(n%2)
    n = n / 2

# 5. 두 수의 합이 같을 때. O(n), θ(n)
i = 0
j = n-1
while (i < j):
    if (a[i] + a[j]) == S:
        break
    elif(a[i]+a[j] < S):
        i += 1
    else:
        j += 1

# 6. O(n√n)
def prime_num_algorithm(n):
    i = 2
    while(i*i <= n):
        if(n % i == 0):
            return False
        i += 1
    return True

count = 0
for i in range(2, n-1):
    if(prime_num_algorithm(n)):   # Boolean
        count += 1
```
