# 백준 1987번 알파벳(DFS)
from sys import stdin
import copy
input = stdin.readline
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input().rstrip())

# 동, 남, 서, 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
alpha = [False]*26
alpha[ord(matrix[0][0]) - 65] = True
answer = 0
def dfs(x, y, now, alpha):
    global answer
    answer = max(answer, len(now))
    if answer == 26:        # 모든 알파벳을 돌면 26개가 됨
        return
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if 0 <= temp_x < n and 0 <= temp_y < m:    # 범위 확인
            # if matrix[temp_x][temp_y] not in now:  # 문자열 확인(이게 시간초과의 이유?)
            temp = ord(matrix[temp_x][temp_y]) - 65
            if alpha[temp] == False:
                alpha[temp] = True
                # print(now+matrix[temp_x][temp_y])
                dfs(temp_x, temp_y, now+matrix[temp_x][temp_y], alpha)
                alpha[temp] = False
    return

dfs(0, 0, matrix[0][0], alpha)
print(answer)
