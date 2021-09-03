# 백준 2812번 크게 만들기
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
number = input().rstrip()
arr = []

for i in range(n):
    arr.append(int(number[i]))
    
count = 0
pre = 0
for i in range(k):
    for i in range(pre, len(arr)-1):
        if arr[i] < arr[i+1]:
            if i != 0:
                pre = i-1
            arr.pop(i)
            count += 1
            break

if count < k:
    arr = arr[:len(arr)-(k-count)]

result = ""
for k in range(len(arr)):
    result+=str(arr[k])

print(result)

            
