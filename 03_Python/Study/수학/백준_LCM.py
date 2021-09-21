# 백준 5347번 LCM
from sys import stdin
input = stdin.readline
t = int(input())
answer = []
for i in range(t):
    a, b = map(int, input().split())
    max_num = max(a, b)
    min_num = min(a, b)
    if max_num % min_num == 0:
        answer.append(max_num)
    else:
        temp = 1
        j = 1
        while j <= min_num: 
            j += 1
            if a % j == 0 and b % j == 0:
                temp *= j
                a //= j
                b //= j
                j = 1
                min_num = min(a, b)
        answer.append(temp*a*b)
for i in range(len(answer)):
    print(answer[i])
         
# 1
# 524287 524287