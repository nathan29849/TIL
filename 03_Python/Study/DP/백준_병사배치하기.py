# 백준 18353번 병사 배치하기 (DP)
# 남는 병사수 최대로, 내림차순은 유지하면서~ 

from sys import stdin
f = stdin.readline
n = int(f())
soldiers = list(map(int, f().split()))

def solution(n, arr):
    answer = 0
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)


        # print(dp)

    return n - max(dp)



print(solution(n, soldiers))