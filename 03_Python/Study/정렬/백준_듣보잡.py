# 백준 1764번 듣보잡

n,m = map(int, input().split())
names = set()
count = 0
arr = []
for _ in range(n):
    names.add(input())
for _ in range(m):
    name = input()
    if name in names:
        count += 1
        arr.append(name)
print(count)
arr.sort()
for a in arr:
    print(a)