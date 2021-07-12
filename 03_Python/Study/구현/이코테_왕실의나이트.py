# 이것이 코딩 테스트다 - 왕실의 나이트 (구현 실전문제)
from sys import stdin
def solution(location):
    col = int(location[1])
    row = ord(location[0])-ord("a")+1
    count = 0
    
    dx = [2, 2, 1, -1, -2, -2, -1, +1]
    dy = [-1, +1, +2, +2, +1, -1, -2, -2]
    
    for i in range(8):
        new_col = col + dx[i]
        new_row = row + dy[i]

        if 1 <= new_col <= 8 and 1 <= new_row <= 8:
            count += 1

    return count 

location = stdin.readline()
print(solution(location))

