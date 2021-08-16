# Q. 문자열 요약해 보기
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다. --> 문제를 제대로 읽자 ( 더 효율적 알고리즘을 만들 수 있는 열쇠이다.)
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.

# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.
# 문제의 번호별 조건에 대한 입력 예시와 출력
# Ex 1)
# abc 	# a1/b1/c1
# Ex 2-1)
# aaabbbc	# a3/b3/c1
# Ex 2-2)
# abbbc	# a1/b3/c1
# Ex 3-1)
# ahhhhz	# a1/h4/z1
# Ex 3-2)
# acccdeee	# a1/c3/d1/e3

def summarize_string(input_str):
    # 이 부분을 채워보세요!
    final_string = ''
    alphabet_occurrence_array = [0]*26
    for char in input_str:
        if char.isalpha() is True:
            alphabet_occurrence_array[ord(char)-ord('a')] += 1
    for index in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[index] > 0:
            final_string += chr(index+ord('a'))+str(alphabet_occurrence_array[index])+'/'
    return final_string[:-1] # python에서 마지막 문자를 제거하는 방법



input_str = "acccdeee"

print(summarize_string(input_str))
