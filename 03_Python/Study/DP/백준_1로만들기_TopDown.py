# 백준 1463번
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def makeOne(arr, n):
    if n == 1:
        return 0

    if arr[n] > 0:
        return arr[n]   # 이미 채워진 것

    arr[n] = makeOne(arr, n-1) + 1

    if n % 2 == 0:
        temp = makeOne(arr, n//2) + 1
        arr[n] = temp if temp < arr[n] else arr[n]
    if n % 3 == 0:
        temp = makeOne(arr, n//3) + 1
        arr[n] = temp if temp < arr[n] else arr[n]

    return arr[n]


f = stdin.readline

n = int(f())
arr = [0 for _ in range(n+1)]
result = makeOne(arr, n)
print(result)