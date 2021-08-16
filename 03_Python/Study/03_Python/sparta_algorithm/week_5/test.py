data = [1, 9, 10, 4, 2, 4, 3, 5]
n = len(data)
maxContigSum = []   
# data[0] ~ data[i]까지의 원소들에 대하여, data[i]에서 끝나는 연속하는 원소들의 합 중에서 최댓값
maxContigSum[0] = data[0]
for i in range(1, n):
    if (maxContigSum[i-1] > 0):
        maxContigSum[i] = maxContigSum[i-1] + data[i]
    else:
        maxContigSum[i] = data[i]
    print(maxContigSum)

maxSum = maxContigSum[0]
for i in range(1, n):
    if (maxSum < maxContigSum[i]):
        maxSum = maxContigSum