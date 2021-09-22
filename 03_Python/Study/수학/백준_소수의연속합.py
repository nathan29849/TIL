# 백준 1644번 소수의 연속합
from sys import stdin
from itertools import combinations
input = stdin.readline
n = int(input())
prime_arr = []

def prime_check(n):
    for number in range(2, int(n**(0.5))+1):
        if n % number == 0:
            return False
    return True   

# 에라토스테네스의 체
def prime_search(n):
    temp = [True] * n
    m = int(n** 0.5)
    for i in range(2, m+1):
        if temp[i] == True:
            for j in range(i+i, n, i):
                temp[j] = False
    return [i for i in range(2, n) if temp[i] == True]

if n == 1:
    print(0)
else:
    # n 미만의 소수 다 찾기
    prime_arr = prime_search(n)
    p_length = len(prime_arr)
    result = 0
    start = -1
    p = -1
    count = 0
    # 투포인터로 시도해보기!
    while p < p_length:
        # 연속된 소수의 합이 n보다 작거나 같을 경우
        if result <= n:
            p += 1
            if result == n: # 같으면 count += 1
                count += 1
            if p < p_length:
                result += prime_arr[p]
        else:   # 연속된 소수의 합이 n보다 클 경우
            while result > n:
                if start < p:
                    start += 1
                    result -= prime_arr[start]
                else:
                    break
    # n이 소수라면
    if prime_check(n):
        count += 1
    print(count)
    