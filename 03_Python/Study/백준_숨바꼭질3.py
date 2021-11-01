# 백준 13549번 숨바꼭질 3
from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
visited = [0] * (10**5+1)
visited[n] = 1
temp = deque([(n, 0)])
sec = -1
while temp:
    now, sec = temp.popleft()
    if now == m:    # 목적지 도착시
        break
    else:
        if now > m: # 만약 목적지보다 현재 위치가 더 가있는 경우 (빼기만 해야함)
            if 0 <= now-1 and visited[now-1] == 0:   # 
                temp.append((now-1, sec+1))
                visited[now-1] = 1
        else:   # 목적지에 도달하지 못한 나머지 경우 
            # 곱하기 2의 경우가 먼저 와야하는 이유 : 0초의 시간이 걸리기 때문
            if now != 0 and now*2 <= 10**5 and visited[now*2] == 0:
                temp.append((now*2, sec))
                visited[now*2] = 1
            if 0 <= now-1 and visited[now-1] == 0:
                temp.append((now-1, sec+1))            
                visited[now-1] = 1
            if now+1 <= m and visited[now+1] == 0:
                temp.append((now+1, sec+1))
                visited[now+1] = 1

print(sec)

