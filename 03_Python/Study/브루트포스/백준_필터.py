# 백준 1895번 필터
from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))
t = int(input())

# 3x3 filter
def filter(start_r, start_c):
    global matrix
    temp = []
    for i in range(start_r, start_r+3):
        for j in range(start_c, start_c+3):
            temp.append(matrix[i][j])
    temp.sort()
    return temp[4]


filtered_img = []
for i in range(r-2):
    for j in range(c-2):
        filtered_img.append(filter(i, j))
count = 0
for img in filtered_img:
    if img >= t:
        count += 1



print(count)