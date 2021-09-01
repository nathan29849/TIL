# 백준 2941번 크로아티아 알파벳
from sys import stdin
from collections import deque
input = stdin.readline


string = input().rstrip()
s = deque()
n = len(string)
for i in range(n):
    s.append(string[i])

arr1 = ['c', 'd', 'l', 'n', 's', 'z']
arr2 = ['c=', 'c-', 'dz', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
while s:
    now = s.popleft()
    if now in arr1 and len(s) > 0:
        next = s.popleft()
        if (now+next) in arr2:
            if (now+next) == "dz" and len(s) > 0:
                after = s.popleft()
                if (now+next+after) == "dz=":
                    count += 1
                else: # dz일 경우("dz="이 아님)
                    count += 2
                    s.appendleft(after)
            elif (now+next) == "dz" and len(s) == 0:   
                count += 2
            else:
                count += 1
        else:
            count += 1
            s.appendleft(next)
    else:  # 첫글자만 맞췄을 경우
        count += 1

print(count)