# 백준 1300번
from sys import stdin
def solution(n, k):
    start = 1
    end = k
    while start <= end:
        mid = (start+end)//2
        temp = 0
        for i in range(1, n+1):
            temp += min(mid//i, n)
            
        if temp >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

n = int(stdin.readline())
k = int(stdin.readline())
print(solution(n, k))