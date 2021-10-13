from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def binarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "False"

arr.sort()
temp = []
for t in range(m):
    result = binarySearch(arr, targets[t])
    temp.append(result)

for t in range(m):
    if temp[t] != "False":
        print(1)
    else:
        print(0)
