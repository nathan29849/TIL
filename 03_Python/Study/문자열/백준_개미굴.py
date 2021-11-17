# 백준 14725번 개미굴
from sys import stdin
from collections import deque
from heapq import heappush, heappop, heapify
input = stdin.readline
n = int(input())

class Node:                     # 개미굴에 대한 정보를 담는 노드
    def __init__(self, vertex):
        self.vertex = vertex    # 노드 내용
        self.next = []          # 다음 노드들을 담는 리스트

burrow = [] # 시작 노드들을 담을 리스트

for i in range(n):
    # temp = arr[i]
    temp = list(map(str, input().rstrip().split()))
    nunmber = int(temp[0])
    temp = temp[1:]
    
    f = False                       # burrow에 있는지 여부를 체크
    now = Node(temp[0])             # 시작 노드를 생성    
    for b in burrow:                
        if now.vertex == b.vertex:  # burrow에 있다면
            f = True                # 체크 해주고
            now = b                 # now를 해당 노드로 교체 해준다.(이 부분이 없으면 새로운 클래스로 인식하여 중복 값이 들어가게 됨)
            break
    if not f:   # burrow에 없으면,,
        burrow.append(now)          # 추가해준다.
    for t in range(1, len(temp)):
        new_node = Node(temp[t])    # start의 다음 노드부터 시작!  
        if len(now.next) == 0:      # next 노드에 아무것도 없다면
            now.next.append(new_node)   # new_node를 next에 추가!
            flag = True             # new_node가 추가되었다는 sign
        else:
            flag = False            # 아직 new_node가 append되지 않음
            for n in now.next:      
                if n.vertex == new_node.vertex:
                    new_node = n    # node update (중복 방지)
                    flag = True     
                    
        if not flag:  # 존재하지 않을 때:       
            now.next.append(new_node)
            # next 노드 내에서 사전 순으로 정렬될 수 있도록 해주기
            now.next = list(sorted(now.next, key=lambda x : x.vertex))
        now = new_node  # now 를 next 로 업데이트
        
def dfs(node):
    temp = []
    depth = 0
    maxHeap = deque([(depth, node)])
    while maxHeap:
        depth, node = maxHeap.popleft()
        temp.append("--" * depth + node.vertex)
        for next_node in node.next:
            maxHeap.append(((depth+1), next_node))
        maxHeap = deque(list(sorted(maxHeap, key = lambda x : x[0], reverse=True)))
    return temp

result = []
for b in burrow:
    temp = dfs(b)
    result.append(temp)

# 시작 노드들이 사전순으로 정렬될 수 있도록 해주기(result 원소 내 리스트 중 첫 번째가 시작 노드)
result = list(sorted(result, key = lambda x : x[0]))

for re in result:
    for r in re:
        print(r)