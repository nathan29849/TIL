# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for i in string:
        # print(i.isalpha())
        if i.isalpha() is True:
            alphabet_occurrence_array[ord(i)-ord('a')] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        
        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet(input)
print(result) 