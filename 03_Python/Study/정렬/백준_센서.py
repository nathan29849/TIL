# 백준 2212번 센서(중복순열로 생각한 풀이 -  메모리 초과)
from sys import stdin
from itertools import product
input = stdin.readline

n = int(input())
k = int(input())
temp = set(map(int, input().split()))    # 중복 원소 제거용
road = list(temp)

new = len(road) - k
P = list(product([i for i in range(new+1)], repeat = k))    # 중복 순열
arr = []
for p in P:
    if sum(p) == new:
        arr.append(p)

final = int(1e9)
for a in arr:
    count = 0
    pre = 0
    back = a[0]+1
    for i in range(1, len(a)+1):
        if len(road[pre:back]) > 1: # 묶음의 원소가 1개 이상일 때
            count += road[back-1] - road[pre]
        if i < len(a):
            pre = back
            back += a[i]+1
    final = min(count, final)
print(final)

