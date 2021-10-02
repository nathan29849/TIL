# 백준 1065번 한수
from sys import stdin
input = stdin.readline
n = input().rstrip()

number = int(n)
count = 0
for i in range(number, 0, -1):
    n = str(i)
    if len(n) > 1:
        temp = int(n[0]) - int(n[1])
        flag = True
        for j in range(len(n)-1):
            if temp != int(n[j]) - int(n[j+1]):
                flag = False
        if flag == True:
            count += 1
    else:
        count += 1

print(count)