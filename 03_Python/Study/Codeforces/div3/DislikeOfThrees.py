# Codeforces div3 A Dislike of Threes
from sys import stdin
input = stdin.readline

def solution():
    answer = []
    for i in range(1, 1667):
        if i % 3 == 0:
            continue
        if "3" in str(i)[-1]:
            continue
        answer.append(i)
    return answer

t = int(input())
start = 1
answer = solution()
result = []
for i in range(t):
    idx = int(input())
    result.append(answer[idx-1])

for j in range(len(result)):
    print(result[j])

