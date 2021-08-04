# 백준 14501번 퇴사(DP)
from sys import stdin
f = stdin.readline
n = int(f())
consulting = [(0, 0)]
for i in range(n):
    t, p = map(int, f().split())
    consulting.append((t, p))

def solution(n, consulting):
    temp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        
        if consulting[i][0] + i - 1 <= n:
            # Ti + day - 1
            temp[consulting[i][0] + i - 1] = max(consulting[i][1] + max(temp[:i]), temp[consulting[i][0] + i - 1])
    # print(consulting)
    # print(temp)
    return max(temp)

print(solution(n, consulting))