# 이코테 실전문제 3번 개미전사
from sys import stdin
f = stdin.readline
n = int(f())
food = list(map(int, f().split()))

def solution(n, food):
    temp = [0 for _ in range(n+1)]
    temp[1] = food[0]
    temp[2] = max(food[0], food[1])
    for i in range(3, n+1):
        temp[i] = max(temp[i-2]+food[i-1], temp[i-1])
    
    return temp[n]

print(solution(n, food))