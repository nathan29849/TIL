# 백준 1965번 상자넣기
from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = [1]*n
# result[0] = (arr[0], 1)
for i in range(1, n):
    pre = 0
    pre_j = 0
    for j in range(i-1, -1, -1): # 역순 탐색
        if arr[j] < arr[i]:
            if result[j] > pre:
                pre = result[j]
    result[i] = pre+1
# print(result)
print(max(result))
# answer = sorted(result, key = lambda x : x[1], reverse=True)
# print(answer[0][1]+1)

# 6 16 4 26 27 1 12 25 9 11 18 19 29 23 20 2 22 10 5 28 24 3 21 30 15 13 7 14 17 8