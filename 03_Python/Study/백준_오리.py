# 백준 12933번 오리
from sys import stdin
input = stdin.readline
hawling = input().rstrip()

check = "quack"
start = 0
count = 0
flag = False

# 연속해서 내는 경우 추가해야 함
for h in hawling:
    if check[start] == h:
        if start == 4:
            start = 0
            count += 1
            if flag == True:        # 만약 한 오리가 연속해서 울었다면
                count -= 1
            else:                   # 연속해서 울지 않았다면
                flag = True
        else:
            start += 1
    else:
        flag = False
if count:            
    print(count)
else:
    print(-1)