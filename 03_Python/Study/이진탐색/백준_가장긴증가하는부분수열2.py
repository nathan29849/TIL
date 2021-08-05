# 백준 12015번 가장 긴 증가하는 부분 수열 2(이진탐색)
from sys import stdin
f = stdin.readline
n = int(f())
numbers = list(map(int, f().split()))

# def binarySearch(start, end, arr, target):
#     while start < end:
#         mid = (start+end)//2
#         if arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid
    
#     return 


def solution(n, arr):
    temp = [arr[0]]

    for target in arr:  
        start = 0
        end = len(temp)-1    
        mid = (start+end)//2
        while start < end:
            mid = (start+end)//2
            if temp[mid] < target:
                start = mid + 1
            else:
                end = mid
        if temp[-1] < target:
            temp.append(target)
        else:
            temp[end] = target
    return len(temp)

print(solution(n, numbers))