# 백준 1316번 그룹 단어 체커
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
count = 0
for i in range(n):
    temp = deque(list(input().rstrip()))
    temp_set = set()
    pre = "@"
    flag = True
    while temp:
        now = temp.popleft()
        if now in temp_set:
            if pre != now:
                flag = False
                break
            else:
                pre = now
        else:
            temp_set.add(now)
            pre = now
    if flag:
        count += 1  
print(count)  
    
