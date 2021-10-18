# 백준 1110번 더하기 사이클
from sys import stdin
input = stdin.readline
n = int(input())
M = n
if n < 10:
    a = "0"+str(n)
count = 0
while True:
    count += 1
    a = str(n)
    if len(a)> 1:
        a = str(int(a[0]) + int(a[1]))
    b = a[-1]
    c = str(n)[-1]
    n = int(c+b)
    if n == M:
        break

print(count)
