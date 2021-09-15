# 백준 14467번 소가 길을 건너간 이유 1
from sys import stdin
input = stdin.readline
n = int(input())
cows = {}
cow_bucket = []
status_bucket = []
count = 0
for _ in range(n):
    cow, status = map(int, input().split())
    if cows.get(cow) is not None:
        if cows[cow] != status:
            count += 1
            cows[cow] = status
    else:
        cows[cow] = status
print(count)