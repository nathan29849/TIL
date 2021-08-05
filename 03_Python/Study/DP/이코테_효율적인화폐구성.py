# 이코테 실전문제 5번 효율적인 화폐 구성
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

    for j in range(1, m+1):
        temp = []
        if money[j] == 0:
            for x in wallet:
                if j >= x:            
                    if money[j-x] != 0:
                        temp.append(money[j-x])
            if len(temp) != 0:
                money[j] = min(temp) + 1
    print(money)    
    return money[m] if money[m] > 0 else -1

print(solution(wallet, n, m))


    

