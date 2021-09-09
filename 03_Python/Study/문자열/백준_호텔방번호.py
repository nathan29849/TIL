# 백준 5671번 호텔 방 번호
from sys import stdin
input = stdin.readline

def solution(n, m):
    count = 0
    for i in range(n, m+1):
        temp = []
        string = str(i)
        flag = True
        for j in string:
            if j in temp:
                flag = False
                break
            else:
                temp.append(j)
        if flag:
            count += 1

    return count   

result = []
while True:
    try:
        n, m = map(int, input().split())
        result.append(solution(n, m))
    except:
        break

for i in range(len(result)):
    print(result[i])