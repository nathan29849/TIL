# 백준 17609번 회문
from sys import stdin
input = stdin.readline

def solution(string, count):
    n = len(string)
    r_string = list(reversed(string))
    if string == r_string:
        return 0
    else:
        if count < 1:
            start = 0
            end = n-1
            while start < end:
                if string[start] == string[end]:
                    start += 1
                    end -= 1
                else:
                    count += 1
                    a = solution(string[start+1:end+1], count)  # 왼쪽 원소 하나 제외
                    b = solution(string[start:end], count)      # 오른쪽 원소 하나 제외
                    if min(a, b) == 0:
                        return 1
                    else:
                        return 2
        else:
            return 2    # 두 개 이상 원소 제외의 경우
                    


t = int(input())
answer = []
for i in range(t):
    string = list(map(str, input().rstrip()))
    result = solution(string, 0)
    answer.append(result)

for j in range(t):
    print(answer[j])