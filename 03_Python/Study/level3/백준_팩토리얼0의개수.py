# 백준 1676번 팩토리얼 0의 개수
from sys import stdin
input = stdin.readline
n = int(input())
def solution(n):
    temp = [0]*(n+1)
    if n == 0 or n == 1:
        return 1
    else:
        temp[0], temp[1] = 1, 1
        for i in range(2, n+1):
            temp[i] = temp[i-1] * i
        return temp[n]

result = str(solution(n))
count = 0
for x in range(len(str(result))-1, -1, -1):
	if result[x] == "0":
		count += 1
	else:
		break
print(count)
