# 이코테 정렬 실전 3번

n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(str, input().split())))        # str로 해도 크기 비교가 가능!

arr = sorted(arr, key = lambda x : x[1])

for i in range(n):
    print(arr[i][0], end=" ")