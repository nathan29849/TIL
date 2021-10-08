# 백준 2467번 용액
import sys
input = sys.stdin.readline


n = int(input())
# 오름차순 정렬
arr = sorted(list(map(int, input().split())))

start = 0
end = n-1
result = []
final = int(1e9)
final_arr = []
def search(start, end):
    global final
    global final_arr
    global arr
    
    temp = abs(arr[start] + arr[end])
    if temp < final:
        final = temp
        final_arr = [arr[start], arr[end]]

    if temp == 0:
        return final_arr
    elif temp < 0:   # 합이 음수
        if end+1 < n:
            search(start, end+1)
        search(start + 1, end)
    else: # temp > 0 .. 합이 양수
        if start-1 < 0:
            search(start-1, end)
        search(start, end-1)

    return final_arr
print(search(start, end))
# print(final_arr)
