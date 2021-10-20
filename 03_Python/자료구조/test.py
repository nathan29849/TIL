
arr = [0 for _ in range(4)]
def fibo(n):
    global arr 
    arr[n] += 1
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

fibo(3)
print(arr)