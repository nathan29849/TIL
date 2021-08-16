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


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def redirection(d):
    return (d+3) % 4

def reverse(d):
    return (d+2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count = 1 # 청소 구역 count
    room_map[r][c] = 2
    queue = list([[r, c, d]])
    while queue:
        r, c, d = queue.pop(0)
        temp_d = d
        for i in range(4): # 0 ~ 3 (총 4번 반복) 서, 남, 동, 북 탐색
            temp_d = redirection(temp_d)
            new_r, new_c = r+dr[temp_d], c+dc[temp_d]
            
            if room_map[new_r][new_c] == 0 and 0 <= new_r < n and 0 <= new_c < m:
                count += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            elif i == 3:
                new_r, new_c = r+dr[reverse(d)], c+dc[reverse(d)]
                queue.append([new_r, new_c, d])

                if room_map[new_r][new_c] == 1:
                    return count

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
