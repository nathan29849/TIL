# 백준 2170번 선 긋기
from sys import stdin
input = stdin.readline
n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

lines.sort()    # sort
result = [lines[0]]
for i in range(1, n):
    if result[-1][1] < lines[i][0]:         # 시작점이 r의 끝점보다 클 때
        result.append(lines[i])
    else:
        for r in result:
            if r[0] <= lines[i][0] <= r[1]: # 시작점이 r의 범위에 속할 때
                if lines[i][1] <= r[1]:     # 끝점마저 r의 범위에 속할 때
                    break
                else:   # lines[1] > r[1]   # 끝점이 r의 범위보다 더 넓을 때
                    r[1] = lines[i][1]      
                    break
answer = 0
for s,e in result:
    answer += abs(e - s)
print(answer)


