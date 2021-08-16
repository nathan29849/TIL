# 백준 11497번 정렬
import sys
from collections import deque
def solution(n, arr):
    arr.sort(reverse=True)
    queue = deque()
    queue.append(arr[0])
    cnt = 1
    right = arr[0]
    left = arr[0]
    maxNum = -sys.maxsize
    for i in range(1, n):
        if cnt % 2 != 0:    # 홀수 (오른쪽에 삽입)
            queue.append(arr[i])
            maxNum = max(maxNum, abs(right - arr[i]))
            right = arr[i]
        else:               # 짝수 (왼쪽에 삽입)
            queue.appendleft(arr[i])
            maxNum = max(maxNum, abs(left - arr[i]))
            left = arr[i]
        cnt += 1
    
    maxNum = max(maxNum, abs(right-left))

    return maxNum

t = int(sys.stdin.readline())
result = []
for i in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    result.append(solution(n, arr))

for j in range(t):
    print(result[j])