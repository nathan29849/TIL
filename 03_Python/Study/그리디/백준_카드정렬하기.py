# 백준 1715번 카드 정렬하기
from sys import stdin
from heapq import heappop, heappush, heapify
input = stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

heapify(arr)
result = 0
while n > 1:
    A = heappop(arr)
    B = heappop(arr)
    heappush(arr, A+B)
    result += A+B
    n -= 1
# last = heappop(arr)
# result += last
print(result)