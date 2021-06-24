from sys import stdin

def search(n, coin):
    goal = 1
    for i in coin:
        if goal < i:
            break
        goal += i
        print("goal :", goal)
    
    return goal



n = int(stdin.readline())
coin = list(map(int, stdin.readline().split()))
coin.sort() # O(n) ... [1, 1, 2, 3, 9]

result = search(n, coin)    
print(result)

# 5 
# 3 2 1 1 9