input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    for j in range(len(array)-1):   # n의 길이만큼 반복
        for i in range(len(array)-1-j): # 맨 뒤 부터 차곡차곡 1개씩은 최댓값이 정렬되기 때문, n의 길이만큼 반복
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!