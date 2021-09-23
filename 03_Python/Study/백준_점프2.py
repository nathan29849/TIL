# 백준 1890번 점프(DP)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
matrix = []
dp = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    dp.append(list(0 for _ in range(n)))

# top-down (recursion)
temp = []
def path_finder(dp, matrix, start):
    now = matrix[start[0]][start[1]]
    if now == 0:        # 0이면 점프할 수 없음(이것 때문에 메모리초과 뜸)
        return 0
    Below = (start[0]+now, start[1])
    Right = (start[0], start[1]+now)
    if Right == (n-1, n-1) or Below == (n-1, n-1):
        dp[start[0]][start[1]] = 1
        return dp[start[0]][start[1]]
    else:
        a, b = 0, 0
        if 0 <= Right[1] < n: # 범위 안에 드는지 확인
            # dp 확인
            if dp[Right[0]][Right[1]] != 0:
                a = dp[Right[0]][Right[1]]
            else:
                a = path_finder(dp, matrix, Right)
            
        if 0 <= Below[0] < n:
            if dp[Below[0]][Below[1]] != 0:
                b = dp[Below[0]][Below[1]]
            else:
                b = path_finder(dp, matrix, Below)
        
        dp[start[0]][start[1]] = a + b
        return dp[start[0]][start[1]]

path_finder(dp, matrix, (0, 0))
print(dp[0][0])