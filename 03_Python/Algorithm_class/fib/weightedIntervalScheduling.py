def wis(weight_list, n, p):
    opt = [0 for i in range(n)]
    for i in range(n):
        opt[i] = max(weight_list[i]+opt[p[i]], opt[i-1])
    
    print(opt)

def searchP(time_list, start, end, k, p):
    # 이전의 끝나는 시간이 k의 시작 시간과 겹치지 않을 때
    if start <= end:
        mid = (start+end)//2
        if time_list[mid][1] == time_list[k][0]:
            p[k] = mid
            return p[k]
        elif time_list[mid][1] < time_list[k][0]:
            start = mid + 1
            return searchP(time_list, start, end, k, p)
        else:   # time_list[mid][1] > time_list[k][0]:
            end = mid - 1
            return searchP(time_list, start, end, k, p)
    else:
        return 0

def makeP(time_list, n, p):
    for k in range(n-1, 0, -1):
        start = 0
        end = k
        searchP(time_list, start, end, k, p)
    print(p)


# time_list [[시작시간, 끝나는 시간]]
time_list = [
    [0, 0],
    [1, 4],
    [3, 5],
    [0, 6],
    [4, 7],
    [3, 8],
    [5, 9],
    [6, 10],
    [8, 11]
]

weight_list = [0, 3, 6, 8, 6, 5, 7, 8, 3]

n = len(time_list)

p = [0 for i in range(n)]

makeP(time_list, n, p)

wis(weight_list, n, p)