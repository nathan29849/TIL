# 백준 1516번 게임개발
from sys import stdin
input = stdin.readline

n = int(input())
time = [0]*(n+1)
pre = {i:[] for i in range(1, n+1)}
checked = [False]*(n+1)
next = []
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for j in range(1, len(temp)-1):
        pre[i].append(temp[j])

def search(start):
    temp = 0
    for i in pre[start]:
        if checked[i] == False: # 방문이 안되었다면,
            search(i)
        temp = max(temp, time[i])
    time[start] += temp
    checked[start] = True

for i in range(1, n+1):
    if checked[i] == False:
        search(i)
# print(time)
for i in range(1, n+1):
    print(time[i])