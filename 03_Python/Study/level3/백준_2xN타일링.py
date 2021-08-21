# 백준 11726 2xN 타일링
from sys import stdin
input = stdin.readline
def solution(n):
  temp = [0] * (n+1)
  for i in range(1, n+1):
    if i == 1:
      temp[i] = 1
    elif i == 2:
      temp[i] = 2
    else:
      temp[i] = temp[i-1] + temp[i-2]
  
  return temp[n]
n  = int(input())
result = solution(n)%10007
print(result)
