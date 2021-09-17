# 백준 1963번 소수 경로
from sys import stdin
from collections import deque
input = stdin.readline
t = int(input())
answer = []
for _ in range(t):
    n, m = map(int, input().split())
    flag = True
    if n == m:  # 두 수가 같은 경우
        answer.append(0)
        flag = False
        continue
        
    visited = [False] * (10000) 
    prime_list = []
    q = deque()
    q.append((n, 0))
    visited[n] = True
    prime_list = []
    # 먼저 소수만 뽑아내기
    for t in range(1000, 10000):    
        # 처음에 범위를 주어진 소수 내로 정해서 틀림 
        # (4자리수 소수면 다 가능토록 해야함)
        j = 2
        pr = True
        while j * j <= t:
            if t % j == 0:
                pr = False
                break
            else:
                j += 1
        if pr:
            prime_list.append(t)
    if n > m:   # 첫번째 소수가 더 큰 경우
        prime_list.sort(reverse=True)
    while q and flag:
        start, number = q.popleft()
        for test in prime_list:
            count = 0
            if visited[test] == False:
                for x in range(4):
                    if str(test)[x] != str(start)[x]:
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    q.append((test, number+1))
                    visited[test] = True
                    if test == m:
                        answer.append((number+1))
                        flag = False
                        break
    if flag == True:
        answer.append("Impossible")

for i in range(len(answer)):
    print(answer[i])
# 1
# 8179 1733
# 반대인 경우 index error
