# 백준 14916번 거스름돈 
from sys import stdin
input = stdin.readline

n = int(input())

coin = [2, 5]
arr = [-1] * (n+1)
for i in range(n+1):
    if i == 2:
        arr[i] = 1
    if i == 5:
        arr[i] = 1        
    if arr[i] == -1:
        temp = []
        for c in coin:
            if i > c and arr[i-c] > 0:
                temp.append(arr[i-c])
        if len(temp) > 0:
            arr[i] = min(temp)+1

print(arr[n])