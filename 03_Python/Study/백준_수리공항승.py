# 백준 1449번

from sys import stdin

def repair(n, l, pipe):
    pipe.sort()
    print(pipe)
    count = 1   # 테이프 필요 개수 
    cur = pipe[0]
    for i in range(1, n):
        if(cur + l > pipe[i]):  # ( 현재 위치 + 테잎 길이 )가 구멍난 곳의 위치를 포함시킬 수 있을 때
            continue
        else:                   # ( 현재 위치 + 테잎 길이 )가 구멍난 곳의 위치를 포함시킬 수 없을 때
            count += 1          # 새 테이프를 써야하므로 count += 1
            cur = pipe[i]       # 새 테이프를 붙이므로 현재 위치도 update

    return count


n, l = map(int, stdin.readline().split())
pipe = list(map(int, stdin.readline().split()))

result = repair(n, l, pipe)
print(result)