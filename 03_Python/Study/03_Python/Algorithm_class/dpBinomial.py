def dpBinomial(n, k):
    C = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    print(C)
    return C[n][k]
    


def main():
    n, k = input().split()
    n, k = int(n), int(k)
    print(dpBinomial(n, k))


if __name__ == "__main__":
    main()


[0, 0, 0, 0, 0, 0, 0], 
[1, 1, 0, 0, 0, 0, 0], 
[1, 1, 1, 0, 0, 0, 0], 
[1, 1, 2, 1, 0, 0, 0], 
[1, 1, 3, 3, 1, 0, 0], 
[1, 1, 4, 6, 4, 1, 0], 
[1, 1, 5, 10, 10, 5, 1]


[[0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 0, 0, 0, 0],
[1, 2, 1, 0, 0, 0, 0],
[1, 3, 3, 1, 0, 0, 0],
[1, 4, 6, 4, 1, 0, 0],
[1, 5, 10, 10, 5, 1, 0],
[1, 6, 15, 20, 15, 6, 1]]
