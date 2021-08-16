# 이코테 실전문제 4번

n, k = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_1.sort()    # 오름차순 정렬
arr_2 = list(map(int, input().split()))
arr_2.sort(reverse=True)    # 내림차순 정렬

for i in range(k):
    if arr_1[i] <= arr_2[i]:
        arr_1[i], arr_2[i] = arr_2[i], arr_1[i]
    else:
        break

sumNum = 0
for j in range(n):
    sumNum += arr_1[j]

print(arr_1)
print(sumNum)

# 5 3
# 7 7 7 7 7
# 5 5 6 6 5
# [7, 7, 7, 7, 7]