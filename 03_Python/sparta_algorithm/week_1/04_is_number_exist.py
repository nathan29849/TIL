# Q. 다음과 같은 숫자로 이루어진 배열이 있을 때, 
# 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.
input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    bool_num = 0
    for num in number:
        if number != num:  # 다른 숫자인 경우
            continue
        else:               # 같은 숫자인 경우
            bool_num = 1
    return bool(bool_num)


result = is_number_exist(3, input)
print(result)