from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()
start = 0
end = n-1
cnt = 0
dic = {}
for i in range(n):
    if dic.get(arr[i]):
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1
print(dic)        
# 두 개로 갑옷을 만들 수 있는지 여부 체크
for i in range(n):
    now = m - arr[i]
    if dic.get(now):
        print(now)
        if dic[now] > 0:
            dic[now] -= 1
            cnt += 1

print(cnt//2)
