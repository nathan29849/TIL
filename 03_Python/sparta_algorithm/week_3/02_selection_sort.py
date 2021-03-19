input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(n-i):
            if array[i + j] < array[min_index]: # index i 에 j를 추가시켜주는 방법으로 반복문 실행
                  min_index = j+i   # min_index 라는 변수에 최저값의 index를 저장
                  
        array[i], array[min_index] = array[min_index], array[i]

    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!