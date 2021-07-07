from sys import stdin

def solution(n):
    string = str(n)
    mid = len(string)//2
    num_1 = string[:mid]
    num_2 = string[mid:]
    result_1 = 0
    result_2 = 0

    for i in num_1:
        result_1 += int(i)

    for j in num_2:
        result_2 += int(j)
    
    if result_1 == result_2:
        return "LUCKY"
    else:
        return "READY"


n = int(stdin.readline())
print(solution(n))