# 백준 16401번 과자 나눠주기
from sys import stdin
import copy
import heapq
input = stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

start = 0
end = max(snacks)

result = 0
snacks.sort(reverse=True)       # sort를 하니까 더 오래걸렸음 ... n log n 이라서 그런듯

while (start <= end):
    total = 0
    mid = (start + end)//2
    if mid == 0:
        break
    
    for snack in snacks:        # sort 안했을 땐 k*n 만큼의 시간이 걸림 (n이 클 수록 k*n < n*logn)
        if snack >= mid:
            total += (snack//mid)
        else:
            break
        
    if total >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
