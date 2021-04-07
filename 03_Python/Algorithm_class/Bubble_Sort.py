a=[3, 44, 38, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50]

n = len(a)
# 마지막 부터 차곡차곡 쌓는다
for i in range(n-1, 0, -1):    # 마지막 원소는 자동으로 정렬!
    for j in range(i):
        if a[j] >= a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)