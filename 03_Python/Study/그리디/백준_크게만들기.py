# 백준 2812번 크게 만들기
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
number = list(map(int, input().rstrip()))
stack = []
for i in range(n):
    while len(stack)>0 and stack[-1] < number[i] and 0 < k:
        stack.pop()
        k -= 1
    stack.append(number[i])

while 0 < k:
    stack.pop()
    k -= 1

result = "".join(map(str, stack))
print(result)