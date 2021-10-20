# 백준 이진수 덧셈
from sys import stdin
input = stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(str, input().split())))

# 0 + 0 = 0   
# 1 + 0 = 1   
# 0 + 1 = 1
# 1 + 1 = 10 *
# 1 + 1 + 1 = 11 *

for a, b in arr:
    temp = 0    # 올림수
    # 길이 비교(a의 자리수가 항상 크게 되도록)
    if len(a) < len(b):
        a, b = b, a
    la = len(a)-1
    lb = len(b)-1
    result = []
    for i in range(len(b)):
        if temp == 0:
            if b[lb-i] == "0":
                if a[la-i] == "0":
                    result.append("0")
                else:
                    result.append("1")
            else:   # b = "1"
                if a[la-i] == "0":
                    result.append("1")
                else:
                    result.append("0")
                    temp = 1
        else:
            if b[lb-i] == "0":
                if a[la-i] == "0":
                    result.append("1")
                    temp = 0
                else:
                    result.append("0")
            else:   # b = "1"
                if a[la-i] == "0":
                    result.append("0")
                else:
                    result.append("1")
    # print(result)                    
    a = a[:la-lb]
    la = len(a)-1
    if la == -1:
        if temp == 1:
            result.append("1")
        else:
            result.append("0")
    else:
        for i in range(la+1):            
            if temp == 1:   # 올림수가 존재하고,
                if a[la-i] == "1":  # 1이면
                    result.append("0")
                else:
                    result.append("1")
                    temp = 0
            else:           # 올림수가 존재하지 않고,
                if a[la-i] == "1":  # 1이면
                    result.append("1")
                else:
                    result.append("0")
        if temp == 1:
            result.append("1")
    flag = False
    # print(result)
    for i in range(len(result)-1, 0, -1):
        if flag == False:
            if result[i] == "1":
                flag = True    
                print(result[i], end="")
        else:
            print(result[i], end="")
    print(result[0])