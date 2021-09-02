# 백준 3613번 Java vs C++
from sys import stdin
input = stdin.readline

string = input().rstrip()
def solution(string):
    n = len(string)
    result = ""

    if string[0].isupper():     # 첫 글자가 대문자라면 모든 경우에 해당이 안됨
        return "Error!"

    if "_" in string:   # C++의 가능성이 있는 경우
        new = list(string.split("_"))
        for i in range(len(new)):
            if i != 0:
                if len(new[i]) == 0:    # _가 두 번 이상 나온경우
                    return "Error!"
                for j in range(len(new[i])):
                    if new[i][j].islower():
                        if j == 0:
                            result += new[i][j].upper()
                        else:
                            result += new[i][j]
                    else:    # _로 분리된 단어들 중 글자가 소문자가 아닌경우
                        return "Error!"
            else:
                for x in new[i]:
                    if x.isupper(): # nM_n (첫 문자덩어리에 대문자가 포함된 경우)
                        return "Error!" 
                result += new[i]
    else:               # Java의 가능성이 있는 경우
        for i in range(n):
            if string[i].isalpha():
                if string[i].isupper(): # 대문자라면 분리해주어야 함
                    result += "_"+(string[i].lower())
                else:
                    result += string[i]
            else:
                return  "Error!"

    if result[0].isupper():
        return "Error!"
    elif result[0].isalpha():
        return result
    else:
        return "Error!"


print(solution(string))