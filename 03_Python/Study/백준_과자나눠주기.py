# 백준 16401번 과자 나눠주기
from sys import stdin
import copy
import heapq
input = stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

def search(target, arr, m):
    result = []
    while len(result) != m:
        now = -1*heapq.heappop(arr)
        if now > target:
            heapq.heappush(arr, -(now-target))
            result.append(target)
        elif now == target:
            result.append(target)
        else:
            break
    if len(result) == m:
        return min(result)
    else:
        return 0

start = 0
end = max(snacks)
answer = 0
target = (max(snacks) + min(snacks))//2
temp = []
for s in snacks:
    temp.append(-1*s)
heapq.heapify(temp)
while start <= end:
    mid = (start + end)//2
    arr = copy.deepcopy(temp)
    result = search(mid, arr, m)
    if result != 0:
        answer = max(result, answer)
        start = mid + 1
    else:
        end = mid - 1

if answer == 0:
    print(0)
else:
    print(answer)