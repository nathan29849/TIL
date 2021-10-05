# 백준 1092번 배
from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
box = deque(box)
sec = 0
while len(box) > 0:
    temp_len = len(box)
    for i in range(n):
        if len(box) > 0:
            now = box.popleft()
            if crane[i] < now:      # 크레인이 들 수 있는 무게인지 체크, 만약 들 수 있다면, box에서 제거      
                for j in range(len(box)-1):
                    new = box.popleft()
                    if crane[i] >= new:
                        break
                    else:
                        box.append(new)
                box.appendleft(now)
        else:
            break
    if temp_len == len(box):        # 크레인이 들 수 없는 박스가 존재할 때
        break
    sec += 1
    # box = deque(sorted(box, reverse=True))      # 역순 정렬

if len(box)>0:
    print(-1)
else:
    print(sec)

# 3
# 6 8 9
# 9    
# 1 2 3 4 5 6 7 8 9    

# 3
# 1 2 3
# 6
# 2 2 2 2 2 2
