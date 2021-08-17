# 백준 1074번 Z
from sys import stdin

def solution(n, r, c):
    base = 0
    while n > 1:
        # 행(row)이 2^n 절반보다 작다면
        if r < (2**n)//2:
            if c < (2**n)//2:           # 좌 상
                pass
            else:                       # 우 상
                base += (2**(n-1))**2 * 1
                c -= (2**n)//2 # 열 update

        else:   # r >= (2**n)//2        
            if c < (2**n)//2:           # 좌 하
                base += ((2**(n-1))**2) * 2
                r -= (2**n)//2 # 행 update

            else:                       # 우 하
                base += ((2**(n-1))**2) * 3
                # 행, 열 update
                r -= (2**n)//2
                c -= (2**n)//2
        n -= 1

    if r==0 and c==0:   # 좌 상
        return base
    elif r==0 and c==1: # 우 상
        return base+1
    elif r==1 and c==0: # 좌 하
        return base+2
    else:
        return base+3
    

input = stdin.readline
n, r, c = map(int, input().split())


print(solution(n, r, c))