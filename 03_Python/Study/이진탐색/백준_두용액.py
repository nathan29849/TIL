# 백준 2470번
from sys import stdin
def solution(n, arr):
    arr.sort()
    start = 0
    end = n-1
    result = (arr[start], arr[end])    # 최종적으로 도출해 낼 두 숫자
    pre_total = abs(arr[start] + arr[end])      # 두 용액의 합
    while start < end:
        total = abs(arr[start]+arr[end])
        if total == 0:
            pre_total = total
            result = (arr[start], arr[end])
            return result
        else:
            if total < pre_total:
                pre_total = total
                result = (arr[start], arr[end])

            if (arr[start]+arr[end]) > 0:
                end -= 1
            else:
                start += 1
    return result

f = stdin.readline
n = int(f())
arr = list(map(int, f().split()))

a, b = solution(n, arr)
print(a, b)