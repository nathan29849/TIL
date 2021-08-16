# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 
# 만약 그런 문자가 없다면 _ 를 반환하시오.
input = "abadabac"
 

def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26
    once_alphabet = []
    # first_alphabet = 0
    for i in string:
        alphabet_occurrence_array[ord(i)-ord('a')] += 1 # 알파벳 나올 떄마다 횟수 추가
    
    for num in range(len(alphabet_occurrence_array)):
        if alphabet_occurrence_array[num] == 1:
            once_alphabet.append(chr(num+ord('a')))

    # 예외처리에 try & except를 이용하였음. (but 너무 비효율적)
    # try:
    #     for a in input:
    #         for b in once_alphabet:
    #             if a == b:
    #                 # first_alphabet = a
    #                 raise NotImplementedError
    # except:
    #     first_alphabet = a
    for char in string:
        if char in once_alphabet:
            return char

    return '_'
            
    
result = find_not_repeating_character(input)
print(result)