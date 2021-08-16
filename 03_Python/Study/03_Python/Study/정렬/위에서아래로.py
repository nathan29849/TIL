# 이코테 정렬 실전 2번
from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    # temp = int(stdin.readline())
    # if len(arr) == 0:
    #     arr.append(temp)
    # else:
    #     for j in range(len(arr)):
    #         if arr[j] < temp:   # 3 5
    #             arr = arr[:j] + [temp] + arr[j:]
    #         else:
    #             arr.append(temp)
    #             break
    arr.append(int(stdin. readline()))

arr.sort(reverse = True)


for k in range(len(arr)):
    print(arr[k], end=" ")