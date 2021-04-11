def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def main():
    n = int(input())
    print(fib1(n))

if __name__ == "__main__":
    main()