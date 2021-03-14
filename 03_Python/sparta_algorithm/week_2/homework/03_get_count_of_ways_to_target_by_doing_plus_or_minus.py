numbers = [1, 1, 1, 1, 1]
# numbers = [2, 3, 1]의 경우도 생각해보기 -> 아예 안될 경우도 있긴 함
target_number = 3

result_count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index, current_sum, target):
    # 구현해보세요!
    if len(array) == current_index:
        if current_sum == target:
            global result_count
            result_count += 1
        return

    get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], target)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], target)







get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0, 0, target_number)  # 5를 반환해야 합니다!
print(result_count)


