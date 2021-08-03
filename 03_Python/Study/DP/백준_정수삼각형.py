# 백준 1932번 정수삼각형(DP)
from sys import stdin
f = stdin.readline
n = int(f())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, f().split())))


def solution(n, triangle):
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:                                  # 처음 수
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:               # 끝 수
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[n-1])

print(solution(n, triangle))