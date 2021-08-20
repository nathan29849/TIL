# 백준 7662번 이중 우선순위 큐
from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

def solution(k):
    min_arr = []
    max_arr = []
    dictionary = {}
    for i in range(k):
        ins, n = map(str, input().split())
        if ins == "I":
            heappush(min_arr, int(n))
            heappush(max_arr, -int(n))
            if dictionary.get(int(n)):
                dictionary[int(n)] += 1
            else:
                dictionary[int(n)] = 1
        else:
            if n == "1":
                # arr.pop()       # 이렇게 하면 안되는 이유 : 힙구조상 최솟값은 확실하지만 최댓값이 무엇일지 알 수 없음 (트리구조이기 때문)
                while max_arr:
                    temp = -heappop(max_arr)
                    if dictionary[temp] > 0:
                        dictionary[temp] -= 1
                        break
            else:
                while min_arr:
                    temp = heappop(min_arr)
                    if dictionary[temp] > 0:
                        dictionary[temp] -= 1
                        break
    result = []
    for key, value in dictionary.items():
        if value > 0:
            result.append(key)
   
    if len(result)>0:
        result.sort()   # 오름차순 정렬
        return (result[-1], result[0])
    else:
        return "EMPTY"

answer = []
t = int(input())
for i in range(t):
    k = int(input())
    result = solution(k)
    answer.append(result)
for i in range(t):
    if answer[i] == "EMPTY":
        print(answer[i])
    else:
        print(answer[i][0], answer[i][1])