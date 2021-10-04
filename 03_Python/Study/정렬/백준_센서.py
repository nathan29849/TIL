# 백준 2212번 센서
from sys import stdin
input = stdin.readline
n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))


if k >= n:
    print(0)
else:
    temp = []
    for i in range(1, n):
        temp.append(sensors[i] - sensors[i-1])
    
    temp.sort(reverse=True)

    for j in range(k-1):
        temp.pop(0)
    
    print(sum(temp))

