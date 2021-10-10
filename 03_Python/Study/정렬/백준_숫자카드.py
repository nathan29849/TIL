# 백준 10815번 숫자카드
from sys import stdin
input = stdin.readline
n = int(input())
cards = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
check_check = [0 for i in range(m)]
dic = {}

for j in range(m):
    if check[j] in cards:
        check_check[j] +=1

for k in range(m-1):
    print(check_check[k], end=" ")
print(check_check[-1])