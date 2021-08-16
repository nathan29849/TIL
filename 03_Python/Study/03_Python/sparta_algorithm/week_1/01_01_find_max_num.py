# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]
    # for i in range(1, len(array)):
    #     if array[i-1] > array[i]:
    #         max_num = array[i-1]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)