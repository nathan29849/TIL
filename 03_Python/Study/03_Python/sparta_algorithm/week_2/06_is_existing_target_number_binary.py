finding_target = 37
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
finding_numbers = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    start = 0
    finish = len(array) - 1
    # count = 0
    # 겹치는 순간부터는 finish가 start보다 먼저 오게되어 애초에 값을 찾을 수 없음.
    # 언제까지 while문을 돌려야할지 미리미리 생각하고 코드를 짜자.
    while start <= finish:
        mid = (start + finish) // 2 # 이 연산자를 통해 나머지 없이 몫만 나타낼 수 있음.
        if (array[mid] == target):
            return True
        elif (array[mid] < target):
            start = mid+1
        else:
            finish = mid-1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)

# 질문 : 만약 first 또는 finish에 target이 위치하게 될 때는 false가 뜰 수 밖에 없도록
# while문 조건이 그렇게 되어있다.. 이진 탐색으로도 못 찾는 것이 있는가.