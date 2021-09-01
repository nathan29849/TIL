# 백준 16953번 A->B 
from sys import stdin
input = stdin.readline

A, B = map(int, input().split())
count = 1
flag = False
while B > 0:
    if str(B)[-1] == "1":
        B = int(str(B)[:-1])    # 마지막 1 제거
    else:
        if B % 2 == 0:          # 나누기가 가능한지 확인
            B = B // 2
        else:
            break               # 불가능하면 break
    count += 1
    if A == B:
        print(count)
        flag = True
        break
if flag != True:
    print(-1)
