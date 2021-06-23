from sys import stdin
import copy

def search(n, coin):
    num = coin[-1]
    C = [0 for i in range(num+1)]
    C[0] = 1
    for i in range(1, num+1):
        copy_coin = copy.deepcopy(coin)
        for x in copy_coin:
            copy_coin.pop(copy_coin.index(x))
            if x == i:
                C[i] = 1
                break
            elif i > x:
                if C[i-x] != 0:
                    C[i] += C[i-x]
        if C[i] == 0:
            return i
    return C            


n = int(stdin.readline())
coin = list(map(int, stdin.readline().split()))
coin.sort() # O(n) ... [1, 1, 2, 3, 9]

result = search(n, coin)    
print(result)

# 5 
# 3 2 1 1 9