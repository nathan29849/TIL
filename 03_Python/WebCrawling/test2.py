arr = [0 for _ in range(11)]

def fibo(n):
    global arr
    arr[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

fibo(10)
print(arr)