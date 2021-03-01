def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for i in string:
        # print(i.isalpha())
        if i.isalpha() is True:
            alphabet_occurrence_array[ord(i)-ord('a')] += 1
        

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))