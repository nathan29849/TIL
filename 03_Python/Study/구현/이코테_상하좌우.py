# 이것이 코딩 테스트다 - 상하좌우 (4-1) 
from sys import stdin

def solution(n, move):
    location = [1, 1]
    for i in move:
        if i == "U":
            if location[0] != 1:    # 1행 
                location[0] -= 1
        elif i == "L":              # 1열
            if location[1] != 1:
                location[1] -= 1
        elif i == "D":              # 마지막 행
            if location[0] != n:
                location[0] += 1
        else: # i == "R"
            if location[1] != n:
                location[1] += 1

    print(f"{location[0]} {location[1]}")
    return 

n = int(stdin.readline())
move = list(map(str, stdin.readline().split()))

solution(n, move)
