import time
a = [list((x, x) for x in range(1000)) for _ in range(1000)]
# a = list(x for x in range(1000000))
result = 0
start = time.time()
for i in range(len(a)):
    for k, j in a[i]:
        result += j
end = time.time()

result = 0
b = [{x:x for x in range(1000)} for _ in range(1000)]
# b = {x:x for x in range(1000000)}
start_B = time.time()
for i in range(len(b)):
    for k, j in b[i].items():
        result += j
end_B = time.time()

print(end-start)
print(end_B - start_B)

# 리스트와 딕셔너리를 각각 비교 했을 때 for문 돌리는 시간은 list가 근소 우위
# 리스트 안에 리스트를 원소로 가질 때와 리스트 안에 딕셔너리를 원소로 가질 때를 비교했을 때
# for 문을 돌리는 시간은 딕셔너리가 완전 우위
# 결론 : 리스트 내부 원소로 리스트보다 딕셔너리일 때 탐색 속도가 더 빠르다.