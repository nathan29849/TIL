# 이코테 실전문제 2
from sys import stdin
f = stdin.readline

def partsSearch(n, m, arr1, arr2):
    for i in range(m):
        flag = False
        start = 0
        end = n-1
        target = arr2[i]
        while start <= end:
            mid = (start + end)//2
            if arr1[mid] == target:
                print("yes", end=" ")
                flag = True
                break
            elif arr1[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if flag != True:
            print("no", end=" ")


n = int(f())
arr1 = list(map(int, f().split()))
m = int(f())
arr2 = list(map(int, f().split()))

partsSearch(n, m, arr1, arr2)

# 5
# 8 3 7 9 2
# 3
# 5 7 9