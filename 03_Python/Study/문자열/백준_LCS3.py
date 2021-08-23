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
C = [([0] * len1) for _ in range(len2)]
result = "%"
for i in range(len2):
    for j in range(len1):
        if i == 0 or j == 0:
            C[i][j] = 0
        elif str1[j] == str2[i]:
            C[i][j] = C[i-1][j-1] + 1
            result += str1[j]
        else:
            C[i][j] = max(C[i][j-1], C[i-1][j])

S = [0] * len(result)
for i in range(1, len3):
    for j in range(len(result)):
        if j == 0:
            S[j] = 0
        elif str3[i] == result[j]:
            S[j] += 1
        else:
            S[j] = max(S[j], S[j-1])

print(S[-1])


# [0, 0, 0, 0], 
# [0, 0, 0, 0], 
# [0, 0, 0, 0], 
# [0, 1, 1, 1], 
# [0, 1, 2, 2], 
# [0, 1, 2, 3]

# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 1, 1, 1, 1, 1], 
# [0, 1, 1, 1, 1, 1], 
# [0, 1, 2, 2, 2, 2], 
# [0, 1, 2, 3, 3, 3], 
# [0, 1, 2, 3, 4, 4], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5], 
# [0, 1, 2, 3, 4, 5]]