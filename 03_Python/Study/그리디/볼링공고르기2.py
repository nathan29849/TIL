from sys import stdin



def Pick(n, ballList):
    C = []
    print("ballList :", ballList)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if ballList[i] != ballList[j]:
                C.append((ballList[i], ballList[j]))
    print(C)
    return len(C)


n, m = map(int, stdin.readline().split())
ballList = list(map(int, stdin.readline().split()))
ballList.sort() # O(n) ... [1, 2, 2, 3, 3]

result = Pick(n, ballList)
print(result)

# 5 3
# 2 3 2 3 2  -> 2, 2, 2, 3, 3

# 8 5
# 1 5 4 3 2 4 5 2

# 풀이애서 m이 필요가 없게 되어서 뭔가 좀 찝찝함... 아무리 봐도 m은 필요가 없는 듯 함..
# 그리디를 사용했는가? : 값이 같지 않으면 무조건 선택 
# 시간 복잡도 : O(N^2) ... 범위가 2000이내인 경우 O(N^2) 가능
