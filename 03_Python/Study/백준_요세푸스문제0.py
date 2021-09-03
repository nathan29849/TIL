# 백준 11866번 요세푸스 문제 0
from sys import stdin
from collections import deque
input = stdin.readline
n, k = map(int, input().split())

arr = deque([i+1 for i in range(n)])
result = []
count = 0
while arr:
    now = arr.popleft()
    if count == k-1:
        result.append(now)
        count = 0
    else:
        count += 1
        arr.append(now)

temp = ", ".join(map(str, result))
print("<"+temp+">")  

#############
# 백준 11866번 요세푸스 문제 0 (deque 이용 X)
# from sys import stdin
# input = stdin.readline
# n, k = map(int, input().split())

# arr = [i+1 for i in range(n)] 
# idx = k-1
# result = []
# while n > 1:    # n = len(arr)
#     if idx < n:
#         now = arr.pop(idx)
#         result.append(now)
#         idx += (k-1)
#         n -= 1
#     else:
#         idx = idx % n

# result.append(arr[0])
# temp = ", ".join(map(str, result))
# print("<"+temp+">")  