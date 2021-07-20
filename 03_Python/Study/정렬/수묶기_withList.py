# 백준 1744번 정렬
from sys import stdin

def solution(n, arr):
    answer = 0
    arr.sort(reverse=True)  # 내림차순 정렬
    plus = [] 
    one = []
    zero = []
    minus = []
    for x in arr:
        if x > 1:
            plus.append(x)
        elif x == 1:
            one.append(x)
        elif x == 0:
            zero.append(x)
        else:
            minus.append(x)

    if len(plus) % 2 == 0:
        for i in range(0, len(plus), 2):
            answer += plus[i] * plus[i+1]
    else:
        for i in range(0, len(plus)-1, 2):
            answer += plus[i] * plus[i+1]
        answer += plus[-1]

    answer += len(one)

    minus.sort()
    if len(minus) % 2 == 0:
        for i in range(0, len(minus), 2):
            answer += minus[i] * minus[i+1]
    else:
        for i in range(0, len(minus)-1, 2):
            answer += minus[i] * minus[i+1]

        if len(zero) == 0:
            answer += minus[-1]

    return answer



n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

print(solution(n, arr))