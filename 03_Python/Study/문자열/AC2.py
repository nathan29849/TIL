# 백준 5430번 AC 문자열
from sys import stdin
input = stdin.readline

def solution(n, arr, command):
    r_count = 0
    front = 0
    back = 0
    for x in command:
        if x == "R":
            r_count += 1
        else:
            if r_count % 2 == 0:
                front += 1
            else:
                back += 1
    if front+back > n:
        return "error"
    else:
        arr = arr[front:n-back]
        if r_count % 2 != 0:
            arr.reverse()
        result = "["
        for i in range(len(arr)):
            result += str(arr[i])+","
        result = result[:-1] + "]"
        if len(result) == 1:
            result = "[]"
        return result

t = int(input())
answer = []
for i in range(t):
    command = input().rstrip()
    n = int(input())   
    temp = input().rstrip()
    if len(temp) > 2:
        arr = list(map(int, temp.strip("[]").split(",")))
    else:
        arr = []
    answer.append(solution(n, arr, command))    
for i in range(len(answer)):
    print(answer[i])