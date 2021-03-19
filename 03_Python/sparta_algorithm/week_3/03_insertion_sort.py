input = [4, 6, 2, 9, 1]

def insertion_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            # print(i-j)
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break   # 이전의 숫자들은 비교할 필요가 없어짐 (선택정렬과 다른점 - 최선의 경우 O(N)의 시간이 걸림)
    return

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!