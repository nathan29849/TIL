# 백준 1633번 최고의 팀 만들기
from sys import stdin
input = stdin.readline
count = 0
W = []
B = []

while True:
    try:
        w, b= map(int, input().split())
        if w < b:
            if len(B) < 16:            
                B.append(b)
            else:
                if len(W) < 16:
                    W.append(w)
            
        else:
            if len(W) < 16:
                W.append(w)
            else:
                if len(B) < 16:
                    B.append(b)
    except:
        break
print(sum(W)+sum(B))
