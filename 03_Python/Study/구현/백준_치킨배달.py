# 백준 15686번 치킨배달
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

chicken = []
home = deque()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            chicken.append([i, j])
        elif matrix[i][j] == 1:
            temp = []
            home.append([i, j, []])
                        # r, c, 거리, 치킨집좌표
for i in range(len(home)):
    for j in range(len(chicken)):
        absolute = abs(home[i][0]-chicken[j][0]) + abs(home[i][1]-chicken[j][1])
        home[i][2].append(chicken[j]+[absolute])
for i in range(len(home)):
    home[i][2] = sorted(home[i][2], key=lambda x : x[2])
print(home)
# final = 0
# arr = []
# while chicken:
#     now = chicken.pop()
#     temp = 0
#     for i in range(len(home)):
#         absolute = abs(home[i][0]-now[0]) + abs(home[i][1]-now[1])
#         if home[i][2] > absolute:
#             home[i][2] = absolute
#             home[i][3] = now


# print("arr", arr)
# new_arr = sorted(arr, key = lambda x : x[2], reverse=True)
# new_arr = deque(new_arr[:m])
# print("new_arr", new_arr)
# for i in range(len(home)):
#     home[i][2] = n**2
    

# while new_arr:
#     now = new_arr.popleft()
#     temp = 0
#     for i in range(len(home)):
#         absolute = abs(home[i][0]-now[0]) + abs(home[i][1]-now[1])
#         if home[i][2] > absolute:
#             home[i][2] = absolute
#             now[2] += 1
#             home[i][3] = now
#     arr.append(now)


# print(home)
# for i in range(len(home)):
#     final += home[i][2]

# print(final)
# 5 1
# 2 0 1 0 0
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 2 0 0
# 0 0 0 0 1