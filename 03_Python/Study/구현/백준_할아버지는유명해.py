# 백준 5766번 할아버지는 유명해!
from sys import stdin
input = stdin.readline


def solution(n, m):
    weekly= []
    for _ in range(n):
        weekly.append(list(map(int, input().split())))

    result = {}
    for i in range(n):
        for j in range(m):
            temp = weekly[i][j]
            if result.get(temp):
                result[temp] += 1
            else:
                result[temp] = 1

    ranking = []
    for key, value in result.items():
        ranking.append((key, value))

    ranking = sorted(ranking, key = lambda x: x[1], reverse=True)
    ranking.pop(0)

    answer = []
    temp = ranking[0][1]
    for i in range(len(ranking)):
        if ranking[i][1] == temp:
            answer.append(ranking[i][0])
        else:
            break
    answer.sort()
    for j in range(len(answer)-1):
        print(answer[j], end=" ")
    print(answer[-1])

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        solution(n, m)
    
