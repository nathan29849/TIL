current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def redirection(r, c, d):
    if d == 0: 
        d = 3      # 서쪽이라면,
        c = c - 1   # 바라보는 방향이 (r, c-1)
    elif d == 1:    
        d = 0      # 북쪽이라면,   
        r = r - 1   # 바라보는 방향이 (r-1, c)
    elif d == 2:
        d = 1      # 동쪽이라면,     
        c = c + 1   # 바라보는 방향이 (r, c+1)
    elif d == 3:
        d = 2      # 남쪽이라면,
        r = r + 1   # 바라보는 방향이 (r+1, c)
    return r, c, d

# def reverse(r, c, d):
#     r, c, d = redirection(r, c, d)
#     r, c, d = redirection(r, c, d)
#     return r, c, d


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    r = r - 1    # index가 0부터 시작하므로 조정
    c = c - 1    # index가 0부터 시작하므로 조정
    count = 1 # 청소 구역 count
    room_map[r][c] = 2
    flag = True
    # room_map[r][c] = 1 # 시작점은 무조건 0, 바로 청소한다고 생각.
    while flag:
        for i in range(4): # 0 ~ 3 (총 4번 반복) 서, 남, 동, 북 탐색
            r, c, d = redirection(r, c, d)  # 왼쪽 방향부터 탐색
            print(r, c, d)
            if room_map[r][c] == 0:
                count += 1
                room_map[r][c] = 2
                break
            elif i == 3:
                if room_map[r][c] != 0 : # 만약 현 위치가 위 for문을 다 돌았음에도, 0을 못찾았다면,
                    if d == 0:  # 북쪽 방향을 바라보고 있으면,
                        # r = r + 1 # 원래 자리로 복귀 후에 후진.
                        r = r + 2
                    elif d == 1:    # 동쪽 방향을 바라보고 있으면,
                        # c = c - 1   # 원래 자리로 복귀 후에 후진.
                        c = c - 2
                        d = 1
                    elif d == 2:    # 남쪽 방향을 바라보고 있으면,
                        # r = r - 1   # 원래 자리로 복귀 후에 후진.
                        r = r - 2
                        d = 2
                    elif d == 3:    # 서쪽 방향을 바라보고 있으면,
                        # c = c + 1   # 원래 자리로 복귀 후에 후진.
                        c = c + 2
                        d = 3
                if room_map[r][c] == 1: # 후진 했는데, 벽이라면,,,
                    flag = False
    return count

(6, 
[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 1, 1, 1, 1, 0, 1], 
[1, 0, 0, 1, 1, 0, 0, 0, 0, 1], 
[1, 0, 1, 1, 0, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 2, 0, 0, 0, 1], 
[1, 0, 2, 2, 0, 0, 0, 1, 0, 1], 
[1, 0, 0, 0, 2, 0, 1, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 1, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    









    # while cur_location == 0:
    #     if d == 0:
    #         if room_map[r-1][c-2] == 0:
    #             cur_location = room_map[r-1][c-2]
    #             count += 1
    #             redirection(d) # 서쪽  
    #         elif room_map[r][c-1] == 0:
    #             cur_location = room_map[r][c-1]
    #             count += 1
    #             d = 2   # 남쪽
    #         elif room_map[r-1][c] == 0:
    #             cur_location = room_map[r-1][c]
    #             count += 1
    #             d = 1 # 동쪽
    #         elif room_map[r-2][c-1] == 0:
    #             cur_location = room_map[r-2][c-1]
    #             count += 1
    #             d = 0 # 북쪽
    #         else:   # 모든 방향이 다 청소가 됐거나 벽이거나 할 때.
    #             cur_location = [r][c-1]

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
