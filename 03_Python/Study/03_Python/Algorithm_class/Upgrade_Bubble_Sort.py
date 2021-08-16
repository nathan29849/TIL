a=[3, 44, 38, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50]

n = len(a)


for i in range(n-1, 0, -1):    # 마지막 원소는 자동으로 정렬!
    sorted_list = False
    for j in range(i):
        if a[j] >= a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            sorted_list = True
        
        
    if sorted_list == False:
        break
print(a)