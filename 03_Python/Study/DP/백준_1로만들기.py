# 백준 1463번
from sys import stdin
import sys
sys.setrecursionlimit(10**6)
def makeOne(arr, n):
    for i in range(2, n+1):
        arr[i] = arr[i-1] + 1
        if i % 3 == 0:
            arr[i] = min(arr[i//3]+1, arr[i])
        if i % 2 == 0:
            arr[i] = min(arr[i//2]+1, arr[i])
    return arr[n]
    # if n == 1:
    #     return 0
    # if arr[n] > 0:
    #     return arr[n]
    # arr[n] = makeOne(arr, n-1) + 1
    # temp = 10**6
    # temp2 = 10**6
    # if n % 2 == 0:
    #     temp = makeOne(arr, n//2) + 1
    # if n % 3 == 0:
    #     temp2 = makeOne(arr, n//3) + 1
    # arr[n] = min(arr[n], temp, temp2)
    # return arr[n]




f = stdin.readline

n = int(f())
arr = [0 for _ in range(n+1)]
result = makeOne(arr, n)
print(result)