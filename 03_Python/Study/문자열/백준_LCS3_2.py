# 백준 1958번 LCS3 (문자열)
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

x = "%"+input().rstrip()
y = "%"+input().rstrip()
z = "%"+input().rstrip()

temp = []
heappush(temp, (len(x), x))
heappush(temp, (len(y), y))
heappush(temp, (len(z), z))

len1, str1 = heappop(temp)
len2, str2 = heappop(temp)
len3, str3 = heappop(temp)
C = [[([0] * len1) for _ in range(len2)] for _ in range(len3)]

for k in range(len3):
    for i in range(len2):
        for j in range(len1):
            if i == 0 or j == 0 or k == 0:
                C[k][i][j] = 0
            elif str1[j] == str2[i] and str2[i] == str3[k]:
                C[k][i][j] = C[k-1][i-1][j-1] + 1
            else:
                C[k][i][j] = max(C[k-1][i][j], C[k][i-1][j], C[k][i][j-1])
print(C[len3-1][len2-1][len1-1])