# 백준 4358번 생태학
from sys import stdin
input = stdin.readline
dic = {}
def solution(string):
    if dic.get(string):
        dic[string] += 1
    else:
        dic[string] = 1

count = 0
while True:
    string = input().rstrip()
    if not string:
        break
    count += 1
    solution(string)

dic = dict(sorted(dic.items(), key=(lambda x:x[0])))

for key, value in dic.items():
    a = value/count * 100
    print(f"{key} {a:0.4f}")
    
    