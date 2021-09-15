# 백준 16208번 귀찮음
from sys import stdin
input = stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
sum_num = sum(numbers)
while numbers:
    x = numbers.pop()
    sum_num -= x
    answer += x*sum_num
    
print(answer)
