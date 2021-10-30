# 백준 2631번 줄세우기
from sys import stdin
input = stdin.readline

def LIS(arr):
    dp = [0] * (n)
    temp = [arr[0]]
    dp[0] = 1
    for i in range(1, len(arr)):
        result = lowerBound(temp, arr[i])
        if len(temp) <= result:
            temp.append(arr[i])
            dp[i] = len(temp)
        else:   # len(temp) > result + 1
            temp[result] = arr[i]
            dp[i] = len(temp[:result+1])
    return dp
    
def lowerBound(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(n - max(LIS(arr)))

# 3 7 5 2 6 1 4
# temp = [3]
# temp = [3, 7]
# temp = [3, 5]
# temp = [2, 5]
# temp = [2, 5, 6]
# temp = [1, 5, 6]
# temp = [1, 4, 6]

