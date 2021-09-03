# 백준 2876번 그래픽스 퀴즈
from sys import stdin
input = stdin.readline

n = int(input())
grade = [[0, 0] for _ in range(n)]
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

idx = 0
x = [0, 1, 0, 1]
y = [0, 1, 1, 0]
for j in range(1, n):
    for z in range(4):
        if arr[i-1][x] == arr[i][y]:
            grade[i-1][x] = 

print(arr)
print(max(grade), grade.index(max(grade)))



