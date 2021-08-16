# 백준 11000번
from sys import stdin
from collections import deque
# 최소의 강의실 사용하여 모든 수업을 가능케 해야함.. 
# 강의실 개수를 출력해야 함
def room(n, time):
    newList = sorted(time, key=lambda x:(x[1], x[0]))
    redundancy = deque(i for i in range(n))
    count = 0

    while len(redundancy) > 1:
        idx = redundancy.popleft()
        temp = newList[idx][1]
        arr = []
        for i in redundancy:
            if temp <= newList[i][0]:
                temp = newList[i][1]
                arr.append(i)
            
        for j in arr:
            redundancy.remove(j)
        count += 1

    if len(redundancy) == 1:
        count += 1
    return count


n = int(stdin.readline())
time = []
for i in range(n):
    time.append(tuple(map(int, stdin.readline().split())))

result = room(n, time)
print(result)

# 7
# 1 4
# 5 8
# 9 12
# 2 11
# 3 6
# 5 7
# 7 10