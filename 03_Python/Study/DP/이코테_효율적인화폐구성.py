# 이코테 실전문제 3번 개미전사
from sys import stdin
f = stdin.readline
n, m = map(int, f().split())
wallet = []
for _ in range(n):
    wallet.append(int(f()))

def solution(wallet, n, m):
    money = [0 for _ in range(m+1)]

    for i in range(n):
        if wallet[i] <= m:
            money[wallet[i]] = 1
    
    # money = [0, 0, 1, 1, 0, 0, 0, 0, 0, ...]
    for j in range(money[0], m+1):
        



    

