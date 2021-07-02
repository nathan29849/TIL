# 백준 11000번
from sys import stdin
import heapq
# 최소의 강의실 사용하여 모든 수업을 가능케 해야함.. 
# 강의실 개수를 출력해야 함
def room(n, time):
    newList = sorted(time, key=lambda x: (x[0], x[1]))
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, newList[0][1])   # 시작시간이 가장 빠른 회의를 추가함

    for i in range(1, n): # 만약 한 회의실에 회의를 더 배정할 수 있다면,(heap에 들어간 회의의 종료시간 <= 새로운 회의의 시작시간)
        if heap[0] <= newList[i][0]: 
            heapq.heappop(heap) # 해당 원소를 heap에서 제외시키고
            heapq.heappush(heap, newList[i][1])   # 힙에 새로 원소를 추가한다.
        else:   
            # heap에 들어간 회의의 종료시간이 새로운 회의의 시작시간을 넘기면,
            heapq.heappush(heap, newList[i][1])   # 힙에 새로 원소를 추가한다.

    return len(heap)

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