# 백준 5557번 1학년
from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = arr.pop()
result = 0
bucket = [0] * 21
bucket[arr[0]] += 1

def answer(number, bucket, ans, result):
    if number < n-1:    # 맨 마지막 원소 제외
        temp = [0] * 21
        for i in range(len(bucket)):
            if bucket[i] != 0:
                a = i + arr[number]
                b = i - arr[number]
                if a <= 20:
                    temp[a] += bucket[i]
                if 0 <= b:
                    temp[b] += bucket[i]
        if number != n-2:
            answer(number+1, temp, ans, result)
        else:
            print(temp[ans])
            return
        
answer(1, bucket, ans, result)

