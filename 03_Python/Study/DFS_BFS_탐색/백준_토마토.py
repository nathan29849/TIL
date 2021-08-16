# 백준 7576번 BFS
from sys import stdin
from collections import deque

def solution(n, m, box):
    dx = [0, -1, 0, +1]
    dy = [+1, 0, -1, 0]

    # rotten = 0  # 썩은 토마토 개수 (필요없었음)
    # count = 0   # 익게 한 토마토 개수(필요없었음)
    unripe = 0  # 덜 익은 토마토 개수 
    days = 0    # 흐른 일 수 
    queue = deque()
    temp = []
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                temp.append((i, j))    # 시작점 모으기 
            elif box[i][j] == 0:
                unripe += 1
            # else: 
            #     rotten += 1         # 썩은거 골라내기 ... 굳이 있을 필요가 있을까?

    queue.append(temp)

    while queue:
        temp_list = queue.popleft() # 리스트 단위로 level 구분 짓기
        arr = []    # 다음 level에 들어갈 위치들
        for col, row in temp_list:
            for l in range(4):
                if 0 <= col+dx[l] < n and 0 <= row+dy[l] < m:
                    if box[col+dx[l]][row+dy[l]] == 0:
                        box[col+dx[l]][row+dy[l]] = 1
                        arr.append((col+dx[l], row+dy[l]))
                        unripe -= 1
        if len(arr) == 0:       # 다음 level에서 추가 된 것이 없고
            if unripe == 0:     # 덜 익은 토마토도 없을 때 (완료된 상태)
                return days
            else:           # 더 이상 익게할 수 있는 토마토가 없을 때 (미완료된 상태 : -1)
                return -1
        else:
            days += 1
            queue.append(arr)
    # return days : 이것도 굳이 필요없음 어차피 len(arr)== 0 에서 다 걸러짐


n, m = map(int, stdin.readline().split())
box = []
for i in range(m):
    box.append(list(map(int, stdin.readline().split())))
print(solution(m, n, box))
