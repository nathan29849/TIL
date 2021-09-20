# 백준 17266번 어두운 굴다리
from sys import stdin
import math
input = stdin.readline
N = int(input())
M = int(input())
lights = list(map(int, input().split()))
height = max(lights[0], N - lights[-1])
for m in range(1, M):
    left = ((lights[m] + lights[m-1]) // 2) - lights[m-1]
    right = lights[m] - ((lights[m] + lights[m-1]) // 2)
    temp = max(left, right)
    if temp > height:
        height = temp
print(height)


