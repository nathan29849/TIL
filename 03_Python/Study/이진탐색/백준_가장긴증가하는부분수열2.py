# 백준 12015번 가장 긴 증가하는 부분 수열 2(이진탐색)
from sys import stdin
f = stdin.readline
n = int(f())
numbers = list(map(int, f().split()))

def solution(n, arr):
    temp = [arr[0]]

    for target in arr:  
        start = 0
        end = len(temp)-1    
        while start < end:
            mid = (start+end)//2
            if temp[mid] < target:
                start = mid + 1
            else:
                end = mid
        if temp[-1] < target:
            temp.append(target)
        else:
            temp[end] = target  # idx 값으로 start나 end나 상관 없음
    return len(temp)

print(solution(n, numbers))