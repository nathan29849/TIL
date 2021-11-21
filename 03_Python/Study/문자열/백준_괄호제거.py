# 백준 2800번 괄호 제거
from sys import stdin
from itertools import combinations
input = stdin.readline

string = list(input().rstrip())
r = []
bracket = []
for i in range(len(string)):
    if string[i] == "(":
        r.append(i)
    elif string[i] == ")": 
        bracket.append((r.pop(), i))                      

result = set()  # 중복 제거용
for i in range(1, len(bracket)+1):
    comb = list(combinations(bracket, i))  # 제거할 괄호의 쌍 구하기
    for c in comb:
        temp = string[:]
        for s, e in c:
            temp[s] = ""
            temp[e] = ""
        result.add("".join(map(str, temp)))
    
result = list(result)
result.sort()
for i in range(len(result)):
    print(result[i])
