# 백준 1697번
import sys
from collections import deque

def solution(start, dest):
    queue = deque()
    temp = [start]
    queue.append(temp)
    visited = [False] * (10**5+1)
    visited[start] = True
    count = 0
    while queue:
        arr = queue.popleft()
        temp = []
        for x in arr:
            if x == dest:
                return count
            if x - 1 >= 0:
                if visited[x-1] == False:
                    visited[x-1] = True
                    temp.append(x-1)
            if x != 0 and x*2 <= 10**5:
                if visited[x*2] == False:
                    visited[x*2] = True
                    temp.append(x*2)
            if x <= dest:
                if visited[x+1] == False:
                    visited[x+1] = True
                    temp.append(x+1)
        queue.append(temp)
        count += 1


n, k = map(int, sys.stdin.readline().split())
print(solution(n, k))