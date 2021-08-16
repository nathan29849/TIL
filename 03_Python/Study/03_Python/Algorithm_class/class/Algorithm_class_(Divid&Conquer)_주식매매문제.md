# 주식 매매 문제 - 분할과 정복

문제 : 어떤 회사의 주식 가격이 날짜 별로 n개 주어져 있다. 한 번 주식을 사서 한 번 팔 수 있다고 하자. 얻을 수 있는 최대 이득을 구하는 프로그램을 작성하시오.

ex) \[30, 25, 50, 10, 40, 15, 80, 5, 60, 65]일 때, 최대 이득은 70이다.

## 방법 1. 반복을 통한 해결 O(N^2)

## 방법 2. 분할과 정복을 통한 해결 O(log N)

- 입력을 반으로 나눈다.
- 왼쪽 반의 해(leftSol)를 구하고, 오른쪽 반의 해(rightSol)를 구한다.
- 주어진 입력에 대한 해는 max(leftSol, rightSol, 오른쪽 반 최댓값 - 왼쪽 반 최솟값)

```pseudo
Algorithm maxProfit(price, left, right):
    // 리스트(배열) price의 left 위치에서 right 위치까지 원소들에 대하여
    // 반환값 : profit(최대이득), minimum, maximum
    if (left == right):
        maxProfit = 0
        minimum = maximum = price[left]
    else:
        mid = (left + right) / 2  	// 2로 나눈 몫
        leftSol, l_min, l_max = maxProfit(price, left, mid)의 profit, minimum, maximum
        rightSol, r_min, r_max = maxProfit(price, mid+1, right)의 profit, minimum, maximum
        solCandidate = r_max - l_min
        profit = max(leftSol, rightSol, solCandidate)
        minimum = min(l_min, r_min)
        maximum = max(l_max, r_max)
    return profit, minimum, maximum
```

main에서 maxProfit(price, 0, n-1)을 호출 (n은 원소의 개수)
