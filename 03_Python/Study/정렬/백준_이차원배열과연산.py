# 백준 17140번 이차원 배열과 연산
from sys import stdin
input = stdin.readline
r, c, k = map(int, input().split())
matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().split())))

sec = 0
r -= 1
c -= 1
while (sec <= 100):
    if len(matrix) - 1 >= r and len(matrix[0]) -1 >= c:
        if matrix[r][c] == k:
            break
    sec += 1
    # col_len, row_len
    col_len = len(matrix)
    row_len = len(matrix[0])
    flag = ""
    max_len = 0
    if col_len >= row_len:      # R 연산
        flag = "R"
        for i in range(col_len):
            temp_dict = {}
            for j in range(row_len):
                temp = matrix[i][j]
                if temp != 0:
                    if temp_dict.get(temp):
                        temp_dict[temp] += 1
                    else:
                        temp_dict[temp] = 1
            temp = list(sorted(temp_dict.items(), key=lambda x:(x[1], x[0])))  # value가 작은 순, 그 다음으로 key가 작은 순
            temp_arr = []
            for key, value in temp:
                temp_arr.append(key)
                temp_arr.append(value)
            matrix[i] = temp_arr                   
            max_len = max(max_len, len(temp_arr))
    else:                       # C 연산
        flag = "C"
        temp_matrix = []
        for i in range(row_len):
            temp_dict = {}
            for j in range(col_len):
                temp = matrix[j][i]
                if temp != 0:
                    if temp_dict.get(temp):
                        temp_dict[temp] += 1
                    else:
                        temp_dict[temp] = 1
            temp = list(sorted(temp_dict.items(), key=lambda x:(x[1], x[0])))   # value가 작은 순, 그 다음으로 key가 작은 순
            temp_arr = []
            for key, value in temp:
                temp_arr.append(key)
                temp_arr.append(value)
            temp_matrix.append(temp_arr)     
            max_len = max(max_len, len(temp_arr))
        matrix = temp_matrix

    col_len = len(matrix)
    row_len = max_len
    for i in range(col_len):
        for j in range(row_len):
            temp_len = len(matrix[i])
            if temp_len < max_len:
                sub = max_len - temp_len
                for s in range(sub):
                    matrix[i].append(0)

    if flag == "C":   # "C"  (row, col change)
        temp_matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]
        for i in range(col_len):
            for j in range(row_len):
                temp_matrix[j][i] = matrix[i][j]
        matrix = temp_matrix
if sec > 100:
    print(-1)
else:
    print(sec) 