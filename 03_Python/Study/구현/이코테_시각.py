# 이것이 코딩 테스트다 - 시각 (4-2)
from sys import stdin
def solution(n):
    second = 0
    minute = 0
    hour = 0
    count = 0
    while hour <= n:
        second += 1
        if second == 60:
            minute += 1
            second = 0
        if minute == 60:
            hour += 1
            minute = 0

        if "3" in str(hour) + str(minute) + str(second):
            count += 1

    return count


n = int(stdin.readline())
print(solution(n))