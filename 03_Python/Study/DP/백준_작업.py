# 백준 2056번 작업
from sys import stdin
input = stdin.readline

n = int(input())
time = [0]*(n+1)                # 해당 노드에서 걸리는 시간
pre = [[] for _ in range(n+1)]  # 선행해야하는 노드 번호들

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    if temp[1] != 0:
        pre[i] = temp[2:]

for i in range(1, n+1):
    temp = 0   
    for j in pre[i]:    # 선행작업이 존재하는 경우
        temp = max(temp, time[j])
    time[i] += temp
print(max(time))