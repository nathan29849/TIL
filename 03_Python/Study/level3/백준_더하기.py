# 백준 9095번 1,2,3 더하기 (class3)
from sys import stdin
input = stdin.readline

def solution(n):
    arr = [1, 2, 3]
    temp = [0]*(n+1)
    # basecase 
    temp[0], temp[1] = 1, 1
    if n>=2:
        for i in range(2, n+1):
            for j in arr:
                if j <= i:
                    temp[i] += temp[i-j]
    return temp[n]

t = int(input())
result = []
for i in range(t):
    n = int(input())
    result.append(solution(n))

for j in range(t):
    print(result[j])
