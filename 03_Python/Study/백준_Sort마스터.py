# 백준 20551번 Sort 마스터 배지훈의 후계자
from sys import stdin
n = stdin.readline

n, m = map(int, input().split())
q = []
s = set()
for i in range(n):
    temp = int(input())
    q.append(temp)
    s.add(temp)
q.sort()
check = [False for _ in range(m)]
D = []
for j in range(m):
    D.append((int(input()), j))
flag = False
while D:
    now, idx = D.pop()
    if now in s:
        start = 0
        end = n-1
        while start < end:
            mid = (start + end)//2
            if q[mid] == now:
                if check[idx] == False:
                    check[idx] = i
                break
            elif q[mid] < now:
                end = mid - 1
            else:
                start = mid + 1
    else:
        check[idx] = -1


for j in range(m):
    print(check[j])


