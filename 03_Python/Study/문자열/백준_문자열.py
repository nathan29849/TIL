# 백준 1120번 문자열
from sys import stdin
from itertools import combinations
input = stdin.readline
a, b = map(str, input().rstrip().split())
len_a = len(a)
len_b = len(b)

def check(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
arr = []
difference = len_b - len_a
for i in range(difference+1):
    temp = difference - i
    arr.append((i, temp))

# print(arr)
result = int(1e9)
if difference == 0:
    result = check(a, b)
else:
    for front, back in arr:
        number = b[:front] + a + b[len_b-back:]
        result = min(check(number, b), result)

print(result)