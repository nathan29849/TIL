def fib(n):
    if n <= 1:
        return n
    
    prev = 0
    current = 1
    for i in range(2, n+1):
        current, prev = current + prev, current
    
    return current

