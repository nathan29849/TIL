# 백준 1946번
from sys import stdin

def hire(n, rank, arr):
    resume = sorted(rank, key=lambda x : x[0]) # 서류 기준으로 분류
    count = 1
    temp = resume[0][1]     # 면접 전형의 점수를 기록할 변수 (가장 적은 점수만을 기록하게 됨)
    for i in range(1, n):
        if temp > resume[i][1]:
            temp = resume[i][1]
            count += 1

    arr.append(count)

t = int(stdin.readline())
arr = []
for k in range(t):
    n = int(stdin.readline())
    rank = []
    for i in range(n):
        rank.append(tuple(map(int, stdin.readline().split())))
    hire(n, rank, arr)

for i in range(t):
    print(arr[i])

# 1 4 .
# 2 3 .
# 3 2 .
# 4 1 .
# 5 5

# 1 4
# 2 5
# 3 6
# 4 2
# 5 7
# 6 1
# 7 3

# 6 1
# 4 2
# 7 3
# 1 4
# 2 5
# 3 6
# 5 7

