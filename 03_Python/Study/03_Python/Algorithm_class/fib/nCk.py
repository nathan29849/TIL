def C(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)
        