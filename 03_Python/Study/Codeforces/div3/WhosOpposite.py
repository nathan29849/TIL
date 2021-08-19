# Codeforces div3 B Who's Opposite?
from sys import stdin
input = stdin.readline

def solution(a, b, c):
    maxNum = max(a, b, c)
    first = max(a, b)
    second = min(a, b)
    start = maxNum//2
    temp = [start]
    count = 0
    while temp:
        n = temp.pop()
        if n < 1:  
            return -1
        elif 2*n + 1 <= first:
            return -1
        arr = [i for i in range(2*n+1)]
        if c > 2*n:
            n += 1
            count += 1
            if count > 2:
                return -1
        else:
            c_idx = arr.index(c)

        if first - second == n:
            if c_idx > n:
                return arr[c_idx - n]   # 1부터 인덱스 시작
            else:
                return arr[c_idx + n]   # 1부터 인덱스 시작
        elif (first - second)<n:
            n -= 1
            temp.append(n)
            count += 1
        else:
            n += 1
            temp.append(n)
    return -1
        
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    print(solution(a, b, c))