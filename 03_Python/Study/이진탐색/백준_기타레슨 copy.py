# 백준 2343번 기타레슨 (블루레이 크기를 조절)
from sys import stdin
import copy
input = stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))

def upper_bound(arr, target):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < target:
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

original_acc = accumulate(video)
blu_ray = original_acc[-1]//m
original_video = video
while True:
    result = []
    acc = original_acc
    video = original_video
    for _ in range(m-1):
        idx = upper_bound(acc, blu_ray)
        if len(acc) == 0:
            result.append(0)
        else:
            result.append(acc[idx-1])
        video = video[idx:]
        acc = accumulate(video)
    result.append(sum(video))
    if max(result) > blu_ray:
        blu_ray += 1
    else:
        print(blu_ray)
        break
# print(result)


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

# 9 9
# 1 2 3 4 5 6 7 8 9