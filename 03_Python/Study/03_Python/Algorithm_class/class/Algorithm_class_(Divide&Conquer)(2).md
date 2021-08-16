# 2. 병합 정렬(Merge Sort)

> 분할과 정복 방법을 이용한다.
>
> 1. 주어진 크기가 n인 리스트 A를 크기가 n/2인 두 부분으로 나눈다.
> 2. 크기가 n/2인 두 부분을 재귀적으로(recursively) 정렬한다.
> 3. 정렬된 두 부분을 하나로 병합한다.

<img src="https://images.velog.io/images/nathan29849/post/6cf0ed4c-c930-4bc2-a5d4-b36690d8a32b/image.png" width="50%">

- 수도코드

```
Algorithm mergeSort(A, left, right)
     if (left < right)
          mid = (left + right) / 2
          mergeSort(A, left, mid)
          mergeSort(A, mid+1, right)
          merge(A, left, mid, right)
```

---

- 파이썬 코드

```python
array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    # 이 곳을 채워보세요!
    n = len(array)
    mid = (0 + n)//2
    if n == 1:
        return array

    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    array = merge(left_list, right_list)

    return array


def merge(array1, array2):      # 최악의 경우 array1과 array2의 길이의 합 만큼 시간복잡도가 걸림 : O(N)
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
```

#### 정렬된 두 리스트(배열) 병합 알고리즘 시간 분석

- 크기가 m, n인 정렬된 두 리스트의 병합 수행시간(시간 복잡도)
  - min(m,n) <= 원소 비교 횟수 <= m+n-1
  - `O(m+n)`
  - 한 리스트 원소 다 빠지면, 그냥 extend로 남은 원소들 붙여 넣으면 될듯
    - ex. result.extend(array2[array2_index:])

#### 병합정렬의 시간 복잡도 분석

T(n) : MergeSort(A, 0, n-1)을 수행하는데 최악의 경우 키 비교(기본연산) 수

- n = 1인 경우 : T(n) = 0
- n > 1인 경우 : T(n) <= 2T(n/2)+c1\*n (c1 = 1)

T(n)은 `O(n log n)`의 시간 복잡도를 갖는다.

최악의 경우든, 최선의 경우이든 모두 n log n
이유는n > 1 일 때,
T(n) >= 2T(n/2) + c2\*n (c2 = 1/2)이므로 (모든 경우 절반만 비교하고 merge)
T(n)이 Ω(n log n)이기 때문임

따라서 입력의 형태와 관련없이 **n lon n**의 시간이 걸린다.

#### 병합정렬 단점

- merge 할 때 O(n)의 추가적인 메모리가 필요하다. (비교연산에 들어감 - 공간적 측면)
- 재귀 호출시 O(log n)의 스택 메모리가 필요하다. (매 번 불러올 때마다 연산 결과를 저장해서 올라오므로??)
  (: 재귀를 이용하지 않고 반복을 이용하면 개선 가능 -> 중첩 반복문 이용)

  - 비재귀 병합정렬 예시 코드

```python
def seq_merge_sort(arr):
    rght = 0; wid = 0; rend = 0; left = 0
    k = 1

    num = len(arr)
    temp = [0] * num

    while(k < num):
        left = 0
        while(left + k < num):
            rght = left + k
            rend = rght + k
            if(rend > num):
                rend = num
            m = left; i = left; j = rght

            while(i < rght and j < rend):
                if (arr[i] <= arr[j]):
                    temp[m] = arr[i]
                    i += 1
                else:
                    temp[m] = arr[j]
                    j += 1
                m += 1

            while(i < rght):
                temp[m] = arr[i]
                i += 1; m += 1
            while(j < rend):
                temp[m] = arr[j]
                j += 1; m += 1
            m = left
            while(m < rend):
                arr[m] = temp[m]
                m += 1
            left += k * 2
        k *= 2
    return arr
```

# 3. 퀵 정렬(Quick Sort)

- 퀵 정렬은 실제 상황에서 매우 빠르다.
  퀵정렬 알고리즘
  > 1.  리스트(배열) A에서 pivot을 선택한다.
  > 2.  리스트(배열) A를 다음과 같이 분할(partition)한다.
  >     pivot보다 작은 수는 pivot의 왼쪽으로, pivot보다 큰 수는 pivot의 오른쪽으로 이동하여 재배열한다.
  > 3.  분할된 두 리스트 A1,A2를 재귀적으로 정렬한다(각각 Quick sort). 즉 같은 방법(단계1,2를 적용한다.)

<img src="https://images.velog.io/images/nathan29849/post/ce61c7f7-5c0f-4286-8a3a-8939787e8b6f/image.png" width="60%">

퀵정렬 알고리즘

- 수도코드

```
Algorithm quickSort(A, left, right)
    if (left < right) {
    pivotPoint = partition(A, left, right) // pivotPoint는 분할 후 피봇의 위치
    quickSort(A, left, pivotPoint -1)
    quickSort(A, pivotPoint+1, right)
```

#### 퀵 정렬에 있어서 중요한 부분이 "partition"

리스트(배열) A의 정렬 : main 함수에서 quickSort(A, 0, n-1)을 호출

---

## 분할 알고리즘 (1) - Hoare partition

특징

> - 첫 번째 원소를 피봇으로 한다.
> - 다음 원소 i는 pivot보다 큰 수를 만날 때까지 오른쪽으로 이동한다.
> - 맨 마지막 원소 j는 pivot보다 작거나 같은 수를 만날 때까지 왼쪽으로 이동한다.
> - 만약 i < j라면 A\[i]와 A\[j]를 바꾼다.

<img src="https://images.velog.io/images/nathan29849/post/675fb4e7-ee8b-46b4-bf13-d35d93b10ac6/image.png" width="50%">
<img src="https://images.velog.io/images/nathan29849/post/884c49ad-2e58-4a67-9547-c2a2128d7d4b/image.png" width="55%">

- 수도 코드

```
Algorithm partition(A, left, right)
     i = left + 1, j = right
     pivot = A[left]
     while (i <= j)
          while(i <= right and A[i] < pivot)
               i += 1
          while(j >= left and A[j] >= pivot)
               j -= 1
          if (i <= j)
               A[i] 와 A[j]를 교환
               i를 1 증가, j를 1 감소
      A[left]와 A[j]를 교환
      return j
```

- `i > j 라면 멈춘다.`의 의미

  - pivot보다 작은 왼쪽 부분과 pivot보다 큰 오른쪽 부분의 분류가 `i>j`를 기점으로 하여 완전히 나뉘었다는 말이다.

- 파이썬 코드

```python
A = [4, 1, 3, 8, 6, 2, 5, 7, 10]

def partition(A, left, right):
    i = left + 1
    j = right
    pivot = A[left]
    while(i<=j):
        while(i<=right and A[i] < pivot):
            i += 1
        while(j>=left and A[j] >= pivot):
            j -= 1
        if (i<=j):
            A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j


def quick_sort(numbers, left, right):
    if left <= right:
        pivot_point = partition(numbers, left, right)
        quick_sort(numbers, left, pivot_point - 1)  # left side
        quick_sort(numbers, pivot_point + 1, right)     # right side


quick_sort(A, 0, len(A)-1)

```

<img src="https://images.velog.io/images/nathan29849/post/f9c5bc67-0378-45ea-a454-4cb2370a7573/image.png" width="40%">

---

## 분할 알고리즘 (2)

- pivot x는 배열의 마지막 원소로 한다.
- pivotPoint는 left-1로 초기화, i는 left로 초기화 한다.

<img src="https://images.velog.io/images/nathan29849/post/af80d267-6bb2-4adc-abad-3d5c601fda56/image.png" width="70%">

- 수도코드

```
Algorithm partition(A, left, right)
     pivot = a[right]
     pivotPoint = left - 1
     for i = left to right - 1
          if (A[i] <= pivot)
               pivotPoint를 1 증가
               A[i]와 A[pivotPoint]를 교환
     A[pivotPoint + 1]과 A[right]를 교환
     return pivotPoint + 1
```

---

## 퀵정렬 - 시간분석

### 최악의 경우(worst-case)

- 선택되는 피봇이 항상 최댓값 혹은 최솟값일 경우
  (즉 피봇이 원소들을 두 부분으로 나눌 때, 원소들이 한 쪽에 모두 있게될 경우)
  W(n) = W(n-1) + b\*n
  W(n) : O(n^2)

### 평균적인 경우(average-case)

A(n) : O(n log n)

### 가장 좋은 경우(best-case)

- 피봇이 원소들을 두 부분으로 나눌 때, 항상 같은 크기로 나눌 경우!
  B(n) = 2B(n/2) + c\*n
  B(n) : O(n log n)

---

## 분할할 때 pivot을 정하는 방법

- 정렬하고자 하는 원소들 중 첫번째 혹은 마지막 원소를 선택하는 방법
- 정렬하고자 하는 원소들 중 중간 위치에 있는 원소를 선택하는 방법
- 무작위로 선택하는 방법 -> 많이 사용하는 방법(평균적인 경우 `O(n log n)`)

#### 어떤 방법이라도 최악의 수행시간 `O(N^2)`은 변함이 없다.

#### 무작위로 선택하는 방법

```python
def partition(numbers, left, right):
    pivot = random.choice(numbers)  # 랜덤으로 pivot 선택
    n = len(numbers)
    pivot_index = numbers.index(pivot)
    numbers.pop(pivot_index)
    left_side = []
    right_side = []
    for i in range(n-2):    # 0 ~ n-2 /// n-1 은 pivot
        if (numbers[i] <= pivot): # pivot보다 작으면..
            left_side.append(numbers[i])
        else:
            right_side.append(numbers[i])
     left_side.append(pivot)	# 왼쪽 편에 pivot 넣고~
     left_side.extend(right_side) # 나머지 오른쪽 편들 다 밀어 넣기

     return left_side.index(pivot)
```
