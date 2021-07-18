# 백준 18870번
from sys import stdin
def solution(n, arr):
    answer = [0] * n
    temp = []
    for i in range(n):
        temp.append((arr[i], i))
    
    temp = sorted(temp, key = lambda x : x[0])

    j = 0
    for _ in range(n):
        idx = temp[j]
        if j > 0 and temp[j][0] == temp[j-1][0]:
            answer[idx[1]] = answer[temp[j-1][1]]   # 같은 값이 존재하면 answer의 이전 인덱스에 해당하는 값을 넣어준다.
            temp.pop(j)                             # 그리고 해당 값을 뺀다.
        else:
            answer[idx[1]] = temp.index(idx)
            j += 1
    
    for k in range(n-1):
        print(answer[k], end=" ")
    print(answer[-1])


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
solution(n, arr)