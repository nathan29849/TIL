# 백준 16937번 두 스티커
from sys import stdin
input = stdin.readline
h, w = map(int, input().split())
n = int(input())
arr = []
visited = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
    visited.append(0)

for i in range(arr):
    a, b = arr[i]
    # 스티커가 범위 안에 들어갈 수 있다면
    if (h >= a and w >= b) or (h >= b and w >= a):
        temp = a * b
        
