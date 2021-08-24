# 백준 17626번 Four Squares
from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n+1)


i = 1
while i**2 <= n:
    dp[i**2] = 1
    i += 1
print(dp)
for j in range(1, n+1):
    if dp[j] != 1:
        count = 0
        m = j
        while m:
            divide = int(m**(1/2))
            m -= divide**2
            if dp[divide] != 0:
                count += dp[divide]
        dp[j] = count
print(dp)