# 백준 2981번 검문
from sys import stdin
from collections import deque
import math
input = stdin.readline
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)  # 내림차순 정렬
arr = []
for i in range(len(numbers)-1):
    temp = abs(numbers[i] - numbers[i+1])
    arr.append(temp)

arr.sort(reverse=True)
arr = deque(arr)
result = []
# print(math.gcd(*arr))
# 최대 공약수 구하기
while arr:
    if len(arr) > 1:
        a = arr.popleft()
        b = arr.popleft()
        while a % b != 0:
            temp = a % b
            a = b
            b = temp
        if b not in result:
            arr.appendleft(b)
    else:
        a = arr.popleft()
        if a not in result:
            result.append(a)
answer = []
# 최대 공약수의 약수 구하기
while result:
    r = result.pop()
    for i in range(1, int(r**(1/2))+1):
        if r % i == 0 and i not in answer:
            answer.append(i)
            if (i != (r//i)):
                answer.append(r//i)

if len(answer) >= 1:
    answer.sort()
    answer.pop(0)   # 1 빼기
    for i in range(len(answer)-1):
        print(answer[i], end=" ")
    print(answer[-1])
else:
    print(r)


