# 백준 2225번 합분해
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

# 0 부터 20까지의 정수 2개를 더해서 그 합이 20이
# 되는 경우의 수를 구하는 프로그램을 작성하라.

C = [[0]*(n+1) for i in range(k+1)]
# base case
for i in range(1, n+1):
    for j in range(1, k+1):
        if j == 1:
            C[j][i] = 1
        elif i == 1:
            C[j][i] = j
        else:
            C[j][i] = C[j][i-1] + C[j-1][i]
print(C[k][n]%1000000000)



