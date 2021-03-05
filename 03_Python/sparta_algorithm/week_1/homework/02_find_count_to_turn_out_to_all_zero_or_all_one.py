# Q. 0과 1로만 이루어진 문자열이 주어졌을 때, 
# 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 
# 할 수 있는 행동은 문자열에서 '연속된 하나 이상의 숫자'를 잡고 모두 뒤집는 것이다. 
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

# 예를 들어 S=0001100 일 때,
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 
# 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
input = "011110"
# input =  "010001"
# input =  "010101"
# input = "110011"
# input = "101001"
# input = "1110011"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    overlap = 0
    count = 0
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            continue
        else:   # string[i-1] != string[i]
            count += 1
            if string[i] != string[-1]:
                overlap += 1

    return count-overlap

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
            



    # for i in range(1, len(string)-1):   # 0 1 2 3 4
    #     if string[0] == "0":  # 맨 앞 숫자가 0일 때.
    #         if string[i-1] == string[i]:    # 이전 숫자가 현재 숫자와 같을 때.
    #             if string[i] == string[i+1]:    # 다음 숫자가 현재 숫자와 같을 때.
    #                 continue
    #             else:   # 이전 숫자와는 같지만 다음 숫자와는 다를 때.
    #                 count_first_zero += 1
    #         else:   # 직전 숫자와 현재 숫자가 다를 때.
    #             if string[i] == string[i+1]: # 다음 숫자가 현재 숫자와 같을 때.
    #                 continue
    #             else:   # 현재 숫자가 이전 숫자도 다르고 다음 숫자도 다를 때
    #                 continue
    #     else:   # 맨 앞 숫자가 1일 때.
    #         if string[i-1] == string[i]:    # 이전 숫자가 현재 숫자와 같을 때.
    #             if string[i] == string[i+1]:    # 다음 숫자가 현재 숫자와 같을 때.
    #                 continue
    #             else:   # 이전 숫자와는 같지만 다음 숫자와는 다를 때.
    #                 count_first_one += 1
    #         else:   # 직전 숫자와 현재 숫자가 다를 때.
    #             if string[i] == string[i+1]: # 다음 숫자가 현재 숫자와 같을 때.
    #                 continue
    #             else:   # 현재 숫자가 이전 숫자도 다르고 다음 숫자도 다를 때
    #                 continue

