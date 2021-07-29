# 백준 2110번
import sys
def solution(n, c, arr, result):
    start = 0
    end = n-1
    for i in range(c):
        mid = (start + end)//2
        # over_mid = mid + 1
        # under_mid = mid - 1
        arr[end] - arr[mid]

def binarySearch(n, arr, result, start, end): 
    mid = (start+end)//2
    # 차이 비교 (처음과 중간값) (중간값과 끝값)
    # 그래서 result에 등록? 아니면 return 해주면 될듯
    
    over_mid = mid + 1

f = sys.stdin.readline
n, c = map(int, f().split())
arr = []
for _ in range(n):
    arr.append(int(f()))
arr.sort()
result = sys.maxsize
print(solution(n, c, arr, result))



# 5 3
# 1
# 2
# 8
# 4
# 9
# [1, 2, 4, 8, 9]