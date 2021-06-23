from sys import stdin



def Pick(n, ballList):
    combination = (n*(n-1))//2     # nC2 = n*n-1 // 2
    count = 0
    for i in range(n-1):
        if ballList[i] == ballList[i+1]:
            count += 1
    
    return combination - count


n, m = map(int, stdin.readline().split())
ballList = list(map(int, stdin.readline().split()))
ballList.sort() # O(n) ... [1, 2, 2, 3, 3]

result = Pick(n, ballList)
print(result)

# 5
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2

# 풀이애서 m이 필요가 없게 되어서 뭔가 좀 찝찝함... 아무리 봐도 m은 필요가 없는 듯 함..