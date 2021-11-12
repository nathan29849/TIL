# 백준 1181번 단어 정렬
from sys import stdin
input = stdin.readline
n = int(input())

length = [[] for _ in range(51)]
for i in range(n):
    temp = input().rstrip()
    length[len(temp)].append(temp)
result = []
pre = "@"
for i in length:
    i.sort()
    for j in i:
        if pre == j:
            pre = j
            pass
        else:
            pre = j
            print(j)
