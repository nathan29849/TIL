# 백준 1003번 피보나치 함수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())


def fibonacci(n, temp):
    if n <= 1:
        return temp[n]
    else:
        for i in range(2, n+1):
            # if temp[i][0] == 0 or temp[i][1] == 0:
            temp[i] = [temp[i-1][0] + temp[i-2][0], temp[i-1][1] + temp[i-2][1]]
    return temp[n]

result = []
# base case
temp = [[0,0] for _ in range(41)]   # 0 <= N <= 40
temp[0] = [1, 0]
temp[1] = [0, 1]
for i in range(t):
    n = int(input())
    arr = fibonacci(n, temp)
    result.append(arr)

for j in range(t):
    print(result[j][0], result[j][1])