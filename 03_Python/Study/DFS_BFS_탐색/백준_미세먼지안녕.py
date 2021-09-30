# 백준 17144번 미세먼지 안녕!
from sys import stdin
input = stdin.readline
R, C, T = map(int, input().split())
air = []
for _ in range(R):
    air.append(map(int, input().split()))

cleaner = []
dust = []
# 동 남 서 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]

def fuse_dust(dust):
    global air
    global dx
    global dy
    temp = []
    for d in range(len(dust)):
        fine_dust = air[x][y]//5
        count = 0
        for i in range(4):
            nx = dust[d][0] + dx[i]
            ny = dust[d][1] + dy[i]
            if air[nx][ny] == 0:
                continue
            else:
                count += 1
        air[x][y] -= fine_dust * count
        air

    


for i in range(R):
    for j in range(C):
        if air[i][j] == -1:
            cleaner.append((i, j))
        elif air[i][j] != 0:
            dust.append((i, j))

for t in range(T):
