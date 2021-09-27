# 백준 1987번 알파벳(BFS)
from sys import stdin
from collections import deque
import copy
input = stdin.readline
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(input().rstrip())

# 동, 남, 서, 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
q = set()
q.add((0, 0, matrix[0][0]))
answer = 0
def bfs(q):
    global answer
    while q:
        x, y, sentence = q.popleft()
        answer = max(answer, len(sentence))
        if answer == 26:        # 모든 알파벳을 돌면 26개가 됨
            return
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < n and 0<= temp_y < m:
                if matrix[temp_x][temp_y] not in sentence:
                    q.add((temp_x, temp_y, sentence + matrix[temp_x][temp_y]))
    return
bfs(q)
print(answer)
