# 2020 카카오 신입 공채 
import copy
import sys

def solution(s):
    length = len(s)
    

    answer = 0
    if length == 1:
        answer += 1
        return answer
    
    # 문자열은 제일 앞부터 정해진 길이만큼 잘라야 한다.
    # 정해진 길이만큼 자르고 남은 문자열은 그대로 붙여주면 된다.
    # lenth >= 3
    result = []
    for i in range(1, (length//2)+1):
        string = copy.deepcopy(s)   # 문자열 슬라이싱을 하기 위한 deepcopy

        if length % i == 0:                 # 묶음하려는 수로 나누어 떨어질 때
            arr_length = length//i          
                     # 이 플래그를 통해 인덱스 넘는지 안넘는지 체크 할 예정
        else:                               # 나누어 떨어지지 않을 때
            arr_length = (length//i)+1

        temp = [0 for _ in range(arr_length)]

        for j in range(1, arr_length):
            if len(string) >= 2*i:                  # 비교할 것이 남아있는지 확인
                if string[:i] == string[i:2*i]:     # i만큼 자른 문자열을 비교  (만약 다르다면 계속 0의 값을 지니게 됨)
                    if temp[j-1] == 0:                # 만약 0 이라면 
                        temp[j-1] = -1               # 이전 값 -1로 바꿔주고 ~ (나중에 비교를 더 쉽게 하기 위해)
                        temp[j] = 2                 # 2부터 시작
                    else:
                        temp[j] = temp[j-1] + 1                # 그 이후부터는 1씩 더해줌
                        temp[j-1] = -1
                string = string[i:]             # 문자열 change
        result.append(temp)

    answer = sys.maxsize
    for k in result:
        temp_answer = 0
        # 묶음 크기 정하기
        if length % len(k) == 0:
            temp_length = length//len(k)
            flag = True
        else:
            temp_length = length//len(k) + 1
            flag = False
        for m in range(len(k)):
            if flag == False:
                if m == len(k) - 1:         
                    temp_answer += length % (temp_length)  # -1을 해줘야 마지막 길이 덧셈 가능
                elif k[m] == 0:
                    temp_answer += temp_length
                elif k[m] != -1:
                    temp_answer += temp_length+1
                else:
                    pass
            else:                               # flag = True
                if k[m] == 0:
                    temp_answer += temp_length
                elif k[m] != -1:
                    temp_answer += temp_length+1
                else:
                    pass
        
        if answer > temp_answer:
            answer = temp_answer

    return answer

print(solution(	"xababcdcdababcdcd"))