# 백준 9375번 패션왕 신해빈
from sys import stdin
from itertools import combinations
input = stdin.readline
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    category = {}
    for i in range(n):
        item, cate = map(str, input().split())
        if category.get(cate):
            category[cate].append(item)
        else:
            category[cate] = [item, None]

    final = 1
    for key, value in category.items():
        temp = list(combinations(value, 1))
        final *= len(temp)

    answer.append(final-1)

for i in answer:
    print(i)
