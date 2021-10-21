# 백준 2847번 게임을 만든 동준이
from sys import stdin
input = stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
count = 0
for i in range(n-2, -1, -1):
    # print(arr[i+1], arr[i])
    if arr[i+1] <= arr[i]:
        count += arr[i] - (arr[i+1] - 1)
        arr[i] = arr[i+1]-1
print(count)