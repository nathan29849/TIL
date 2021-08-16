from sys import stdin



def Pick(n, m, ballList):
    combination = (n*(n-1))//2     # nC2 = n*n-1 // 2
    count = 0
    C = [1 for i in range(m+1)]
    for i in range(n-1):
        if ballList[i] == ballList[i+1]:
            C[ballList[i]] += 1
    C = [5, 1, 1]
    for j in range(m+1):
        if C[j] != 1:
            count += (C[j]*(C[j]-1))//2

    return combination - count


n, m = map(int, stdin.readline().split())
ballList = list(map(int, stdin.readline().split()))
ballList.sort() # O(n) ... [1, 2, 2, 3, 3]

result = Pick(n, m, ballList)
print(result)

# 5 3
# 2 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2

# 풀이애서 m이 필요가 없게 되어서 뭔가 좀 찝찝함... 아무리 봐도 m은 필요가 없는 듯 함.. -> 중복된 숫자 고를 때 써봤음.
# 그리디를 사용했는가? : 음.. 같은것의 개수를 무조건 빼준다.
# 시간복잡도 : O(N)