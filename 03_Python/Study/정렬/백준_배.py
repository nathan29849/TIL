# 백준 1092번 배
from sys import stdin
input = stdin.readline
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

def shift(box):
    count = 0
    if crane[0] < box[0]:
        return -1
    while box:
        for i in range(n):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    box.pop(j)
        count += 1
    return count
print(shift(box))

# 3
# 6 8 9
# 9    
# 1 2 3 4 5 6 7 8 9    

# 3
# 1 2 3
# 6
# 2 2 2 2 2 2
