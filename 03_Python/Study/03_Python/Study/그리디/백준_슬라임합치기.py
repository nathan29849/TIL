# 백준 14241번
from sys import stdin
from collections import deque

def slime(n, slimes):
    slimes.sort(reverse=True)   # 큰 순서대로 정렬하기

    deq = deque()
    for i in range(n):
        deq.append(slimes[i])

    result = 0  # 얻는 점수

    while (len(deq) > 1):
        x = deq.popleft()
        y = deq.popleft()
        result += x*y   # 곱한 만큼 점수로 추가
        deq.appendleft(x+y) # 합친 슬라임은 다시 deq에 집어넣기

    return result   # 점수 반환

n = int(stdin.readline())
slimes = list(map(int, stdin.readline().split()))

result = slime(n, slimes)
print(result)
