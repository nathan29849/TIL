# 백준 1644번 소수의 연속합
from sys import stdin
from itertools import combinations
input = stdin.readline
n = int(input())
prime_arr = []
if n == 1:
    print(0)
else:
    if n % (n**(0.5)) != 0: # n이 소수라면
        prime_arr.append(n)
    mid = n // 2  
    for number in range(2, mid):
        i = 2
        prime = True
        while i*i <= number:
            if number % i == 0:
                prime = False
            i += 1
        if prime:
            prime_arr.append(number)
    print(prime_arr)