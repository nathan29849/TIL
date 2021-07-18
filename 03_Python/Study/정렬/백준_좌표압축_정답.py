# 백준 18870번 정렬
from sys import stdin
def solution(n, arr):
    answer = [0] * n
    temp = set()
    for i in range(n):
        temp.add(arr[i])
    
    comparison = []
    for t in temp:
        comparison.append(t)
    comparison = sorted(comparison)
    
    dictionary = {}
    for c in range(len(comparison)):
        dictionary[comparison[c]] = c 
    
    for k in range(n):
        answer[k] = dictionary[arr[k]]
    
    for k in range(n-1):
        print(answer[k], end=" ")
    print(answer[-1])


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
solution(n, arr)