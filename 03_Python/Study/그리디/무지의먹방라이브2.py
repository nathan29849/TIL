def solution(food_times, k):
    n = len(food_times)
    temp = k
    i = 0
    # c = 0
    while (i <= k):
        cur = i % n                 # 현재 음식의 위치
        if food_times[cur] != 0:    # 음식이 존재하면
            food_times[cur] -= 1    # 1 차감
            # c += 1
            if i == k:
                return cur+1
        else:
            k += 1                  # 음식이 아예 없어서 뛰어 넘게되는 경우
            # if c == n:
            #     return -1
        i += 1                      # (음식 존재 X -> 그냥 인덱스 + 1)

    return -1

food_times = [3, 1, 2]

k = 5

print(solution(food_times, k))

            