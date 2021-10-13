# 백준 2343번 기타레슨
from sys import stdin
import copy
input = stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))

def upper_bound(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end)//2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start

def accumulate(arr):
    n = len(arr)
    acc = copy.deepcopy(video)
    for i in range(1, n):       # 누적합
        acc[i] += acc[i-1]
    return acc

count = 1
acc = accumulate(video)
result = []
t = acc[-1]//m
if m == 1:
    result = acc
else:
    while count < m-1:
        count += 1
        idx = upper_bound(acc, t)
        print(acc)
        print(idx, t)
        result.append(acc[idx-1])
        video = video[idx:]
        acc = accumulate(video)
    # 2개로 나누기
    idx = upper_bound(acc, t)
    r1 = max(sum(video[:idx]), sum(video[idx:]))
    r2 = max(sum(video[:idx+1]), sum(video[idx+1:]))
    r3 = min(r1, r2)
    result.append(r3)
print(result)
print(max(result))


# 9 3
# 1 2 3 4 5 6 7 8 9
# [15, 13, 17]
# 17

# 9 4
# 1 2 3 4 5 6 7 8 9
# [10, 11, 7, 17]
# 17

# 5 3
# 1 3 5 7 9
# [4, 12]
# 12