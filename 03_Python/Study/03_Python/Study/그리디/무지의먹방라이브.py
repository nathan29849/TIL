def solution(food_times, k):
    n = len(food_times)
    
    for i in range(k):
        count = 0
        cur = i%n   # 현재 위치
        temp = i    # 0 ~ k-1
        if food_times[cur] > 0: # 현재 위치에 먹을 음식이 남아있다면,
            food_times[cur] -= 1
        else:                   # 현재 위치에 먹을 음식이 남아있지 않다면,
            for m in range(n-1):   # (초가 count되지 않으므로 따로 for문을 돌렸다.)
                if (food_times[cur] != 0): 
                    break    
                else:   # 남은 음식이 없을 때 
                    temp += 1
                    cur = (temp)%n  # 현재 위치를 +1 만큼 이동
                    count += 1  # 건너뛴 횟수 기록
            if (food_times[cur] == 0):  # 다 돌았음에도 불구 먹을 음식이 없다면, 
                return -1
            else:
                food_times[cur] -= 1
    # k초가 지난 후
    temp = k+count
    for m in range(n-1):
        cur = temp % n
        if (food_times[cur] != 0): 
            break    
        else:   # 해당 index에 남은 음식이 없을 때 
            temp += 1
    if (food_times[cur] == 0):  # 다 돌았는데도 0이라면, -1 return
        return -1
    else:
        answer = cur + 1
        return answer

food_times = [3, 1, 2, 2, 3]
k = 10

print(solution(food_times, k))