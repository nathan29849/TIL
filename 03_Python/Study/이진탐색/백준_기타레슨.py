# 백준 2343번 기타레슨
from sys import stdin
import copy
import math
input = stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))

start = max(video)
end = sum(video) + 1
result = 10**9 + 1
while start <= end:
    mid = (start + end)//2
    temp = 0
    total = 0
    for v in range(len(video)):
        if temp + video[v] <= mid:
            temp += video[v]
            if v == n-1:
                total += 1
        else:
            total += 1
            temp = video[v]
            if v == n-1 and temp <= mid:
                total += 1
    # for i in range(len(video)):
    #     if temp+video[i] > mid:
    #         total+=1
    #         temp=0
    #     temp+=video[i]
    # if temp:
    #     total+=1    
    if total <= m:
        end = mid - 1
        # if total == m:    ... 이것 때문에 100%에서 틀렸음.. 왜 그런 것일까? 
        # ... m개를 집어 넣지 못하는 경우에도 정답이 될 수 있나? 그런것같긴 함 
        # 왜냐하면, 부족한 경우에는 이미 들어간 것을 쪼개면 되기 때문
        # 그에 대한 반례가 100%에 들어있었던 것 같음
        result = min(mid, result)
    else: # 줄여야 함 (total < m)
        start = mid + 1

if result < 10**9 + 1:
    print(result)
else:
    print(max(video))

# 8 7
# 3 3 10 10 3 2 6 2

# 5 2
# 1 1 1 1 100

# 7 7
# 1 5 9 9 9 2 9
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