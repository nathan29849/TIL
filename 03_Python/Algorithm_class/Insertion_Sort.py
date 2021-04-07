a=[3, 44, 38, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50]

n = len(a)

for i in range(1, n):
    temp = a[i]
    for j in range(i-1, -1, -1):
        if (a[j]>temp):
            a[j+1] = a[j]
        else:
            break
        a[j] = temp # 큰 것과 교환

print(a)