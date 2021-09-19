# 백준 2981번 검문
from sys import stdin
input = stdin.readline
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

numbers.sort()  # 오름차순 정렬
result = []
min_number = numbers[0]
max_number = numbers[-1]
for M in range(2, max_number):
    flag = True
    temp = min_number % M
    for number in numbers:
        if number % M != temp:
            flag = False
            break
    if flag:
        result.append(M)

for i in range(len(result)-1):
    print(result[i], end=" ")
print(result[-1])

# 2
# 100000000
# 3