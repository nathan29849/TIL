# 백준 11399번
from sys import stdin

def ATM(n, waitTime):
    waitTime.sort() # 우선 대기시간 빠른대로 정렬 .. O(logN)
    result = waitTime[0] # 초기화
    for i in range(1, n):
        waitTime[i] += waitTime[i-1]
        result += waitTime[i]
    return result
    
n = int(stdin.readline())
waitTime = list(map(int, stdin.readline().split()))

result = ATM(n, waitTime)
print(result)
