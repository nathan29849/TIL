from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
dic = {}
for i in range(n):
    temp = arr[i]
    if dic.get(temp) is None:
        dic[temp] = i

test = []
for _ in range(m):
    temp = int(input())
    if dic.get(temp) is not None:
        print(dic[temp])
    else:
        print(-1)