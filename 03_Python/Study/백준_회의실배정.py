# 백준 1931번
import sys

def conference(n, time):
    # 회의 시간이 가장 빨리 끝나는 순으로 정렬한다. 
    newList = sorted(time, key = lambda x : x[1], x[0] )   # 람다로 두 번째 원소 기준 정렬하기(잘 익혀두자..)
    finishTime = newList[0][1]
    sumNum = 1
    for i in range(1, n):
        if newList[i][0] >= finishTime: # 다음 올 회의의 시작시간이, 이전 회의의 끝나는 시간보다 같거나 클 때
            finishTime = newList[i][1]
            sumNum += 1
    return sumNum

n = int(sys.stdin.readline())
time = []
for i in range(n):
    time.append(tuple(map(int, sys.stdin.readline().split())))

print(conference(n, time))

# 11
# 1 4
# 3 5
# 5 7
# 0 6
# 8 11
# 5 9
# 12 14
# 6 10
# 8 12
# 2 13
# 3 8