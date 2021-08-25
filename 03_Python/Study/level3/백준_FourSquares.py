# 백준 17626번 Four Squares
from sys import stdin
import time
input = stdin.readline

n = int(input())
dp = [0] * (n+1)
# start = time.time()
i = 1
squareArr = []
while i**2 <= n:
    dp[i**2] = 1
    squareArr.append(i**2)
    i += 1

for j in range(1, n+1):
    if dp[j] != 1:
        temp = 4
        for x in squareArr:
            if x <= j:
                if dp[j-x] <= 3:
                    if dp[j-x]+1 < temp:
                        temp = dp[j-x] + 1
            else:
                break
        dp[j] = temp

print(dp[n])