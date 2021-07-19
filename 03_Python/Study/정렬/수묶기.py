# 백준 1744번 정렬
from sys import stdin
from collections import deque
def solution(n, arr):
    answer = 0
    queue = deque()
    arr.sort(reverse=True)  # 내림차순 정렬
    plus_count = 0 # 양수 개수 카운트
    zero_count = 0
    minus_count = 0
    for i in range(n):
        if arr[i] > 0:
            plus_count += 1
        elif arr[i] == 0:
            zero_count += 1
        else:
            minus_count += 1
        queue.append(arr[i])

    while queue:
        v = queue.popleft()
        if len(queue) == 0:
            answer += v
        else:
            w = queue.popleft()
            if v > 1 and w > 1:
                answer += v * w
            elif w == 1:
                answer += v + w
            elif v == 1 and w == 0:
                answer += v
                if minus_count % 2 != 0:
                    queue.appendleft(w)
            elif v > 1 and w < 0:
                answer += v
                if minus_count % 2 == 0:
                    queue.appendleft(w)
                else:
                    answer += w
                    minus_count -= 1
            elif v == 0 and w == 0: 
                if minus_count % 2 != 0:
                    queue.appendleft(w)
            elif v == 0 and w < 0:
                if minus_count % 2 == 0:
                    queue.appendleft(w)
                else:
                    minus_count -= 1
            elif v < 0 and w < 0:
                if minus_count % 2 != 0:
                    answer += v
                    queue.appendleft(w)
                    minus_count -= 1
                else:
                    answer += v * w

    return answer

n = int(stdin.readline())
arr = []
for i in range(n):
    arr.append(int(stdin.readline()))

print(solution(n, arr))

# 10
# 5
# 4
# 3
# 2
# 1
# 1
# 0
# -1
# -2
# -3
