def CountingSort(A, B, k):
    C = []
    n = len(A)
    k = max(A) + 1
    for i in range(k+1):
        C[i] = 0
    for j in range(n):
        C[A[j]] += 1
    for i in range(k):
        C[i] += C[i-1]
    for j in range(n-1, -1, -1):
        B[ C[A[j]] - 1 ] = A[j]
        C[A[j]] -= 1
    return B
