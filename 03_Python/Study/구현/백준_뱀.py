# 백준 3190번 뱀
from sys import stdin
from collections import deque
input = stdin.readline
# 빈칸 0, 사과 1, 뱀 2

n = int(input())
maze = [[0 for _ in range(n)] for _ in range(n)]

maze[0][0] = 2      # 뱀 표시

k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    maze[r-1][c-1] = 1

l = int(input())
time = deque(["P"]*(n**2 + 1))
for i in range(l):
    a, b = map(str, input().split())
    time[int(a)] = b
time.popleft()
direction = 0
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
now = (0, 0)
body = deque([(0, 0)])
count = 0
while time:
    count += 1
    now = (now[0]+dx[direction], now[1]+dy[direction])
    if 0 <= now[0] < n and 0 <= now[1] < n:
        if maze[now[0]][now[1]] == 1:   # 사과
            body.append(now)
            maze[now[0]][now[1]] = 2
        elif maze[now[0]][now[1]] == 0: # 비어있는 칸
            pre = body.popleft()
            maze[pre[0]][pre[1]] = 0 
            body.append(now)
            maze[now[0]][now[1]] = 2
        else:                           # 자기 몸통
            break
    else:
        break
    # x초 후 방향 변경(방향을 변경하고 진행하는 것이 아님!!)
    command = time.popleft()
    if command == "D":   # Right
        direction = (direction + 1) % 4
    elif command == "L": # Left
        direction = (direction + 3) % 4
print(count)

# [[2, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0], 
#  [0, 0, 0, 1, 0, 0], 
#  [0, 0, 0, 0, 0, 0], 
#  [0, 0, 1, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0]]