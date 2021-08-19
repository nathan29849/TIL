# 백준 5430번 AC 문자열
from sys import stdin
from collections import deque
input = stdin.readline

def solution(n, arr, command):
    temp = ""
    count = 1
    for x in range(len(command)-1):
        if command[x] == command[x+1]:
            count += 1
        else:
            temp += str(count) + command[x]
            count = 1
    temp += str(count) + command[-1]
    command = temp

    tempCount = ""
    for x in command:
        if x != "R" and x !="D":
            tempCount += x
        else:
            number = int(tempCount)  
            tempCount = ""
            if x == "R":
                if number % 2 == 0 :
                    continue
                else:
                    arr.reverse()
            else:
                if number > n:
                    return "error"
                else:
                    if number == 1:
                        arr.popleft()
                    else:
                        arr = list(arr)[number:]
                    n -= number
                    arr = deque(arr)
    return list(arr)


t = int(input())
answer = []
for i in range(t):
    command = input().rstrip()
    n = int(input())   
    temp = input().rstrip()
    if len(temp) > 2:
        arr = deque(map(int, temp.strip("[]").split(",")))
    else:
        arr = []
    answer.append(solution(n, arr, command))    
for i in range(len(answer)):
    print(answer[i])