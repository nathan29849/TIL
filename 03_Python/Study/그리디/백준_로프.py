# 백준 2217번
from sys import stdin

def rope(n, weights):
    weights.sort(reverse=True)
    for i in range(1, n):       
        weights[i] = weights[i]*(i+1)      # 누적 합으로 만들기 

    # print("weights", weights)
    return max(weights)



n = int(stdin.readline())
weights = []
for i in range(n):
    weights.append(int(stdin.readline()))


result = rope(n, weights)
print(result)

