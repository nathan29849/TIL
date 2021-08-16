# 백준 1793번 타일링
from sys import stdin
f = stdin.readline

# bottom up
def tile(n):
    if n <= 1:
        return 1
    else:
        temp = [0 for i in range(n+1)]
        # base case
        temp[0] = 1
        temp[1] = 1
        for i in range(2, n+1):
            temp[i] = temp[i-1] + (2*temp[i-2])

        return temp[n]

while True:
    try:
        print(tile(int(f())))
    except:
        break