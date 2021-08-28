from sys import stdin
input = stdin.readline
k = int(input())
now = 0
count = 0

if k < 0:
    while k < now:
        now -= 2**(count) 
        count += 1
else:
    while k > now:
        now -= 2**(count) 
        count += 1

if k == now:
    print(count) 
else:
    print(-1)