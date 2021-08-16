a=[3, 44, 38, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50]

n = len(a)

for i in range(n-1):    # loop n-1번 반복
    index = i  # 루프를 돌면서 가장 큰 원소를 찾아 그 인덱스를 저장
    for j in range(i+1, n-1):   # 가장 큰 수 찾기 위한 원소 비교횟수
        if a[index] >= a[j]:    
            index = j
    
    a[index], a[i] = a[i], a[index]

print(a)