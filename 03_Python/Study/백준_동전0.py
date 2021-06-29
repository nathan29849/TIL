# 백준 11047번
from sys import stdin
def coin(n, k, wallet):
    wallet.sort(reverse = True)
    count = 0
    for w in wallet:
        if w <= k:
            count += (k//w)
            k = k % w 
        if k == 0:
            return count


n, k = map(int, stdin.readline().split())
wallet = []

for i in range(n):
    wallet.append(int(stdin.readline()))

print(coin(n, k, wallet))