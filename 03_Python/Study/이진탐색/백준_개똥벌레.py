# 백준 3020번 개똥벌레
from sys import stdin
input = stdin.readline
n, h = map(int, input().split())
mite = [] # 석순
tite = [] # 종유석

def binarySearch_LowerBound(start, end, arr, target):
    # 최초로 만나는 지점을 찾아야 하므로
    while start < end:
        mid = (start+end)//2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

heights = [0 for _ in range(h+1)]
for i in range(n):
    temp = int(input())
    if i % 2 == 0:
        mite.append(temp) # 석순
    else:
        tite.append(temp) # 종유석

mite.sort()   # 석순 오름차순 정렬
tite.sort()   # 종유석 오름차순 정렬

for i in range(1, h+1):
    r = binarySearch_LowerBound(0, n//2, mite, i)
    heights[i] += n//2 - r

for i in range(h, 0, -1):
    r = binarySearch_LowerBound(0, n//2, tite, h-i+1)
    heights[i] += n//2 - r

min_num = min(heights[1:])

result = 0
for i in range(1, h+1):
    if min_num == heights[i]:
        result += 1

print(min_num, result)


