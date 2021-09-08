# 백준 2457번 공주님의 정원
# 겹치는 것 중 가장 긴 것 선택

from sys import stdin
from collections import deque
import datetime
input = stdin.readline

n = int(input())
flowers = []
# start month, day & end month, day
for i in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    a = datetime.date(1999, start_month, start_day)
    b = datetime.date(1999, end_month, end_day)
    flowers.append((a, b))

# 시작 날짜를 기준으로 정렬하기 -> 만약 같은 날짜에 시작한다면, 일찍 끝나는 꽃이 우선적으로 정렬
sorted_flowers = deque(sorted(flowers, key=lambda x : (x[0], x[1])))

result = []
flag = True

# 가장 긴걸 뽑기
# 겹치는 시간 최소화
# 3/1 ~ 12/1 신경쓰기
while sorted_flowers:
    start, end = sorted_flowers.popleft()
    if len(result) == 0:
        if start <= datetime.date(1999, 3, 1):
            result.append((start, end))
        else:
            flag = False
            break
    else:
        pre_start, pre_end = result.pop()
        if pre_end > end:       # 이전 꽃이 더 늦게 질 때
            result.append((pre_start, pre_end))
        else:                   # 이전 꽃이 더 빨리 질 때
            if start <= datetime.date(1999, 3, 1):
                result.append((start, end))
            elif pre_end >= datetime.date(1999, 12, 1): # 이미 result의 마지막 원소로 11/30을 포함할 때
                if len(result) == 0:
                    result.append((pre_start, pre_end))                    
                else:
                    before_start, before_end = result.pop() 
                    if start > pre_start and before_end >= pre_start:
                        result.append((before_start, before_end))
                        result.append((start, end))
                    else:
                        result.append((before_start, before_end))
                        result.append((pre_start, pre_end))                    
            else:   # 3/1, 11/30에 걸치지 않을 때
                if len(result) == 0:    # 남는거 없으면 그냥 넣기(비교대상이 없으므로)
                    result.append((pre_start, pre_end))
                    result.append((start, end))
                else:                   # 남는게 있는 경우
                    before_start, before_end = result.pop()     # 그 전 전 원소 뽑기
                    if before_end >= start:                     # 그 전 전 꽃이 현재 꽃의 시작보다 늦게 질 때 (포함하는 경우) ~ 겹치는 시간 최소화
                        result.append((before_start, before_end))
                        result.append((start, end))   
                    else:                                       # 그 전 전 꽃이 현재 꽃의 시작보다 빨리 질 때 (포함 못함)
                        result.append((before_start, before_end))
                        result.append((pre_start, pre_end))
                        result.append((start, end))                                        
# for i in range(len(result)):
#     print(result[i][0], result[i][1])


if flag:
    if result[-1][1] <= datetime.date(1999, 11, 30): # 마지막 원소가 11월 30일을 포함하지 않는 경우
        print(0)
    else:
        print(len(result))
else:
    print(0)




# 11
# 2 15 3 23
# 4 12 6 5
# 4 20 6 5
# 3 1 4 25
# 9 14 12 24
# 6 15 9 3
# 6 3 6 15
# 2 28 4 25
# 6 15 9 27
# 9 26 12 31
# 7 14 9 1