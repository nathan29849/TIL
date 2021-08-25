# 백준 1013번 contact
from sys import stdin
import re
input = stdin.readline

# (100+1+ | 01)+
            
t = int(input())
result = []
p = re.compile("(100+1+|01)+")
for _ in range(t):
    radio = input().rstrip()
    result.append(p.fullmatch(radio))
for i in range(t):
    if result[i] == None:
        print("NO")
    else:
        print("YES")
