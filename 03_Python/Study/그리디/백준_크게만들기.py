# 백준 2812번 크게 만들기
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
number = list(map(int, input().rstrip()))
arr = []

for i in range(n):
    while 



if count < k:
    arr = arr[:len(arr)-(k-count)]

result = ""
for k in range(len(arr)):
    result+=str(arr[k])

print(result)