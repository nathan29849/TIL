from sys import stdin
import math
input = stdin.readline

n = int(input())
for i in range(n):
    r, n = map(int, input().split())
    result = math.factorial(n)//(math.factorial(r) * math.factorial(n-r))
    print(result)