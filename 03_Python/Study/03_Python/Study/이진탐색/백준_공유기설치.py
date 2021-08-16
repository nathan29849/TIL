# 백준 2110번
import sys
def solution(n, c, arr):
    arr.sort()  # 오름차순 정렬
    start = 1
    end = arr[-1] - arr[0]
    result = 0
    while start <= end:
        cnt = 0
        mid = (start+end)//2
        for i in range(n):
            if i == 0:
                router = arr[i]
                cnt += 1
            else:
                if arr[i] >= router + mid:
                    router = arr[i]
                    cnt += 1

        if cnt >= c:
            start = mid + 1
            if result < mid:
                result = mid
        else:
            end = mid - 1
    return result


f = sys.stdin.readline
n, c = map(int, f().split())
arr = []
for _ in range(n):
    arr.append(int(f()))

print(solution(n, c, arr))



# 5 3
# 1
# 2
# 8
# 4
# 9
# [1, 2, 4, 8, 9]