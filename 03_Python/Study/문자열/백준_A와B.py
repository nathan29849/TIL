# 백준 12904번 A와 B
from sys import stdin
from collections import deque
input = stdin.readline

S = input().rstrip()
T = input().rstrip()

def solution(T, S):
    n = len(T) - len(S)

    S_a, S_b, T_a, T_b = 0, 0, 0, 0
    for s in S:
        if s == "A":
            S_a += 1
        else:
            S_b += 1
    
    for t in T:
        if t == "A":
            T_a += 1
        else:
            T_b += 1

    result = deque([(S, 0, S_a, S_b)])
    while result:
        now, count, sa, sb = result.popleft()
        if len(now) != len(T):
            if count % 2 == 0:  # 짝수번 뒤집힌 상태
                a = now + "A"
                b = "B" + now
            else:               # 홀수번 뒤집힌 상태
                a = "A" + now
                b = now + "B"

            if sa < T_a:
                result.append((a, count, sa+1, sb))
            if sb < T_b:
                result.append((b, count+1, sa, sb+1))
        else:
            if count % 2 == 0:
                if now == T:
                    return 1
            else:
                if now[::-1] == T:
                    return 1
    return 0

print(solution(T, S))