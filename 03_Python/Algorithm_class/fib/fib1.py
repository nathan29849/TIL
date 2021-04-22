def initialize(n):
    lookupTable = [-1 for i in range(n+1)]
    return lookupTable

def fib(n, lookupTable):
    if lookupTable[n] != -1:
        return lookupTable[n]
    else:
        if n<= 1:
            return n
        else:
            lookupTable[n] = fib(n-1, lookupTable) + fib(n-2, lookupTable)
    return lookupTable[n]

def main():
    n = int(input())
    lookupTable = initialize(n)
    print(fib(n, lookupTable))

if __name__ == "__main__":
    main()