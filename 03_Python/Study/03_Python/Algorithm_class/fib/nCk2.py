def dpBinominal(n, k):
    C = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    
    return C[n][k]
    