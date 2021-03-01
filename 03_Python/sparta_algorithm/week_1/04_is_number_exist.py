input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    bool_num = 0
    for num in input:
        if number != num:  # 다른 숫자인 경우
            continue
        else:               # 같은 숫자인 경우
            bool_num = 1
    return bool(bool_num)


result = is_number_exist(3, input)
print(result)