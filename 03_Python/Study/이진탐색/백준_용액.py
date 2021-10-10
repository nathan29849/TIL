# 백준 2467번 용액
import sys
input = sys.stdin.readline


n = int(input())
# 오름차순 정렬
arr = sorted(list(map(int, input().split())))

start = 0
end = n-1
final = abs(arr[start] + arr[end])
final_arr = [arr[start], arr[end]]
while start < end:
    temp = abs(arr[start] + arr[end])
    if temp < final:
        final = temp
        final_arr = [arr[start], arr[end]]
    if arr[start] + arr[end] == 0:
        break
    elif arr[start] + arr[end] < 0:   # 합이 음수
        start += 1
    else: # temp > 0 .. 합이 양수
        end -= 1

print(final_arr[0], end=" ")
print(final_arr[1])
