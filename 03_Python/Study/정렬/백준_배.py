# 백준 1092번 배
from sys import stdin
input = stdin.readline
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
visited = [False]*m
sec = 0
count = 0
limit = [crane[-1]] * m
for i in range(m):
    for j in range(n):
        if crane[j] < box[i]:
            limit[i] = j
            break 
start = 0
visit = 0
flag =True
while visit < m:
    count = 0
    n_cnt = 0
    temp = 0
    for j in range(n):
        for i in range(start, m):
            if visited[i] == False:
                if limit[i] <= j:   # 한계 인덱스에 도달했을 때
                    if n_cnt == 0:
                        temp = i
                        n_cnt += 1
                else:
                    count += 1
                    visit += 1
                    visited[i] = True
                    start = i
                    break
    if temp != 0: 
        start = temp 
    sec += 1
    if count == 0:      # 크레인이 들 수 있는 무게가 없을 때
        flag = False
        break


if flag:
    print(sec)
else:
    print(-1)

# 오름차순으로 푼 풀이 (틀림)    
# while b<m:
#     flag = False
#     if start > n-1:             # crane으로 들 수 없는 무게라면 break
#         break
#     for c in range(start, n):   # crane 탐색
#         if crane[c] < box[b]:   # 크레인이 들 수 없는 무게라면,
#             start = c+1         # start를 이전에 범위 못넘은 다음 인덱스로 설정
#             break
#         else:
#             b += 1              # 만약 크레인이 들었다면,
#             flag = True         # flag 변경
#             if b >= m:          # 중간에 박스를 다 끝냈다면
#                 break
#     if flag == True:
#         count += 1              # 한 번이라도 crane 들어올렸다면 횟수로 카운트
# print(count)

# 3
# 6 8 9
# 9    
# 1 2 3 4 5 6 7 8 9    

# 3
# 1 2 3
# 6
# 2 2 2 2 2 2
