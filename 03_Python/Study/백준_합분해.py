# 백준 2225번 합분해
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

# 0 부터 20까지의 정수 2개를 더해서 그 합이 20이
# 되는 경우의 수를 구하는 프로그램을 작성하라.

# 0, 20
# 1, 19
# 2, 18
# 3, 17
# 4, 16
# 5, 15
# 6, 14
# 7, 13
# 8, 12
# 9, 11

# 10, 10  # 한 개의 수를 여러 번 쓸 수도 있음

# 20개 + 1
C = [0 for i in range(n+1)]
C[0] = 1
for i in range(n+1):
    for j in range(n+1):
        if i >= j:
            C[i] += C[i-j]
        else:
            break
print(C)