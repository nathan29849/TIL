# 백준 22864번 피로도
from sys import stdin
input = stdin.readline

A, B, C, M = map(int, input().split())

now = 0   # 현재 피로도
time = 0  # 현재 시각
result = 0 # 일 처리 양

while time < 24:   # 하루에 최대 얼마나 일을 할 수 있는가
    time += 1
    if (now + A) > M:  # 휴식이 필요함.
        if now - C >= 0:
            now -= C
    else:
        now += A
        result += B
    # print("result, time", result, time)
print(result)




