# 백준 14500번 테트로미노
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.appned(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

def dfs(start, dist, max_num):
    stack = [start]
    visited = [[False]*m for _ in range(n)]
    while stack:
        r, c = stack.pop()
        visited[r][c] = True
        

