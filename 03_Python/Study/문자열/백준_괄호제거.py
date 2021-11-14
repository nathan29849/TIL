# 백준 2800번 괄호 제거
from sys import stdin
from itertools import combinations
input = stdin.readline

def check(expression):
    n = len(expression)
    result = []
    cnt = 0
    max_cnt = 0
    flag = True         # "(" 시작점 파악 용도
    b_idx =  [0] * n
    for i in range(n):    # 괄호 수 세기
        if flag == True:
            if expression[i] == "(":
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                b_idx[i] = cnt
            elif expression[i] == ")":
                flag = False
                b_idx[i] = cnt
                cnt -= 1
        else:
            if expression[i] == "(":
                flag = True
                cnt = max_cnt+1
                max_cnt = cnt
                b_idx[i] = cnt
            elif expression[i] == ")":
                b_idx[i] = cnt
                cnt -= 1

    # 괄호 쌍을 리스트 형태로 담을 예정
    bracket = [[] for _ in range(max_cnt+2)]         
    for i in range(len(b_idx)):
        bracket[b_idx[i]].append(i)
    bracket.pop(0)

    for i in range(len(bracket)):
        if len(bracket[i]) == 0:
            bracket = bracket[:i]
            break
    
    arr = []
    # len(bracket)+1로 해주는 이유 : 모든 괄호를 제거하는 경우를 포함
    for i in range(1, len(bracket)+1):
        comb = combinations(bracket, i)
        for com in comb:
            temp = []
            for c in com:
                temp += c
            arr.append(temp)
    
    for a in arr:
        temp = ""
        for i in range(n):
            if i not in a:
                temp += expression[i]
        result.append(temp)

    result = set(result)    # 중복 제거
    result = list(result)
    result.sort()   # 사전 순 정렬
    return result


expression = input().rstrip()
answer = check(expression)
for a in answer:
    print(a)

     