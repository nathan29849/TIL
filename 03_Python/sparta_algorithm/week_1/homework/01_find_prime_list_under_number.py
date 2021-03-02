# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    if number <= 0:
        return "양의 정수를 입력하여 주세요."
    elif number == 1:
        return "1은 소수가 없습니다."
    else:
        for num in range(2, input+1):   # 1, 2, 3, 4, 5, 6, ... 소인수분해하면 간단한데...
            if num % 
                prime_list.append(num)
        

    return prime_list


result = find_prime_list_under_number(input)
print(result)