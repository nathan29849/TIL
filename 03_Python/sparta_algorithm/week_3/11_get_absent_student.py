all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # check = dict()
    # for i in range(len(present_array)):
    #     check[present_array[i]] = i  
    
    # for j in all_array:
    #     # print(j)
    #     if j not in check:
    #         return j
    student_dict = {}
    for key in all_array:   # O(N)
        student_dict[key] = True    # 공간 복잡도 또한 O(N)
        # 해쉬 테이블은 시간은 극대화시킬 수 있되, 공간을 대신 사용하는 자료구조이다.
    
    for key in present_array:   #O(N)
        del student_dict[key]
    
    for key in student_dict.keys():
        return key


print(get_absent_student(all_students, present_students))