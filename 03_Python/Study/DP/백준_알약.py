# 백준 4811번 알약
from sys import stdin
input = stdin.readline

def solution(n, glass_bottle, table):
    temp = []
    for W, H in glass_bottle:
        if (W, H) == (0, 0):
            print(table[W][H])
            return
        else:
            if W > 0:
                if table[W-1][H+1] == 0:
                    table[W-1][H+1] += table[W][H]
                    temp.append((W-1, H+1))
                else:
                    table[W-1][H+1] += table[W][H]
            if H > 0:
                if table[W][H-1] == 0:
                    table[W][H-1] += table[W][H]
                    temp.append((W, H-1))
                else:
                    table[W][H-1] += table[W][H]
    solution(n, temp, table)

result = []
while True:
    n = int(input())
    if n != 0:
        glass_bottle = [(n, 0)]
        table = [[0]*(n+1) for _ in range(n+1)]  # memoization table (2차원)
        table[n][0] = 1 # initialize
        result.append(solution(n, glass_bottle, table))
    else:
        break




         
    
    
