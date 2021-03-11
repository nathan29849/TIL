finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    first = 0
    last = len(numbers) - 1
    while first <= last:
        mid = (first+last) // 2
        if (numbers[mid] == target):
            return True
        elif (numbers[mid] < target):
            first = mid + 1
        else:
            last = mid - 1
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)