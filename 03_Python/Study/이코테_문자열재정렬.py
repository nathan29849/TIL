# 이것이 코딩 테스트다 - 문자열재정렬 (구현)
string = input()

def solution(string):
    result = []
    sumNumber = 0
    for i in string:
        try:
            sumNumber += int(i)
        except ValueError:
            result.append(i)
    
    result.sort()
    temp = ""
    for j in result:
        temp += j
    temp += str(sumNumber)
    return temp

print(solution(string))

# K1KA5CB7
# AJKDLSI412K4JSJ9D