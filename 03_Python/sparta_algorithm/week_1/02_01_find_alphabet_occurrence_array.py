# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for i in string:
        # print(i.isalpha())
        if i.isalpha() is True:
            alphabet_occurrence_array[ord(i)-ord('a')] += 1
        

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))