# 백준 20551번 Sort 마스터 배지훈의 후계자
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
q = []
for i in range(n):
    q.append(int(input()))
q.sort()
check = []
D = []
for j in range(m):
    D.append(int(input()))

for now in D:
    start = 0
    end = n       # n??
    while start < end:
        mid = (start + end)//2
        if now <= q[mid]:
            end = mid
        else:
            start = mid+1
    if 0 <= start < n and q[start] == now:            
        check.append(start)
    else:
        check.append(-1)

for j in range(m):
    print(check[j])