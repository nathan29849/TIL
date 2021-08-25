# 백준 1013번 contact
from sys import stdin
from collections import deque
input = stdin.readline

# (100+1+ | 01+)+


def solution(radio):
    n = len(radio)
    arr = deque()
    for x in range(n):
        arr.append(radio[x])
    i = 0
    while n:
        if arr[0] == "0" and len(arr) > 1:
            if arr[i+1] == "1": 
                arr.popleft()
                arr.popleft()
            else:
                return "NO"
        else:
            count = 0
            try:
                a = arr.popleft() # 1
                b = arr.popleft() # 0
                c = arr.popleft() # 0
            except:
                return "NO"
            if a == "1" and b == "0" and c== "0":
                while arr:
                    now = arr.popleft()
                    if now == c:
                        continue
                    else:
                        count += 1
                        if count > 1:
                            break
                        b = c
                        c = now
                if count == 2:
                    if len(arr) > 0:
                        temp = arr.popleft()
                        arr.appendleft(temp)
                        arr.appendleft(now)
                        if temp == now and b != "0":
                            arr.appendleft(c)
                    else:
                        arr.appendleft(now)
                elif count == 1:
                    pass
                else:
                    return "NO"
            else:
                return "NO"
        n = len(arr)
    return "YES"

            
t = int(input())
result = []
for _ in range(t):
    radio = input().rstrip()
    result.append(solution(radio))

for i in range(t):
    print(result[i])
