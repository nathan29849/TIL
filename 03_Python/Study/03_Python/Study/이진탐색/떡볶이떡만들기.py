# 이코테 실전문제 3번
from sys import stdin
def solution(n, m, arr):
    start = 0
    end = max(arr)
    pre_mid = 0                 # 이전에 설정한 절단기의 높이
    while start < end:
        ddeok = 0
        mid = (start+end)//2    # 현재 설정한 절단기의 높이
        for x in arr:
            if (x - mid) >= 0:
                ddeok += (x-mid)
        
        if ddeok >= m:          # 잘린 떡의 총합이 기준치(m)을 넘는다면, 
            start = mid + 1     # 시작점을 더 올려도 된다.
            if pre_mid < mid:   # 이 전에 설정한 절단기의 높이와 비교
                pre_mid = mid
        else:                   # 잘린 떡의 총합이 기준치(m)을 넘지 못한다면,
            end = mid - 1       # 끝점을 내려야 한다.(기준치를 맞추기 위해)
    return pre_mid



f = stdin.readline
n, m = map(int, f().split())
arr = list(map(int, f().split()))

print(solution(n, m, arr))