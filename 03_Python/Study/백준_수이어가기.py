# 백준 2635번 수 이어가기
from sys import stdin
input = stdin.readline

n = int(input())

m = int(n*(1/2))+1
k = int(n*(7/10))+1

final_count = 0
final_arr = []
for i in range(m, k+1):
    count = 0
    now = n                 # 시작 숫자
    next = i                # 다음 숫자
    arr = [now, next]   
    while now:
        after = now - next  # 다다음 숫자
        if after < 0:
            break
        count += 1
        now = next          # 다음 숫자를 시작 숫자로 놓기
        next = after        # 다다음 숫자를 다음 숫자로 놓기
        arr.append(next)
    if final_count < count:
        final_count = count
        final_arr = arr

print(final_count+2)
for j in range(len(final_arr)-1):
    print(final_arr[j], end=" ")
print(final_arr[-1])

