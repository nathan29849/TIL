input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    if fibo_memo.get(n):       # 그냥 fibo_memo[n]을 하게되면 해당 키가 없을 때 key error를 반환한다. 
        # 따라서 .get()을 통해 판단하는 것이 좋다. 또는 n in fibo_memo로 해도 좋음.
        return fibo_memo[n]
    else:   # fibo_memo[n]이 없다면,
        fibo_memo[n] = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
        return fibo_memo[n]
        



print(fibo_dynamic_programming(input, memo))