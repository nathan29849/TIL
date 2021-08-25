from sys import stdin
import heapq
input = stdin.readline

arr = []
n = int(input())
for i in range(n):
    m = int(input())
    if m == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, m)