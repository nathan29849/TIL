def insert(A, key):
    n = len(A)
    n += 1
    i = n-1
    while (i > 0 and A[Parent(i)] < key):
        A[i] = A[Parent(i)]
        i = Parent(i)
    A[i] = key
    
        

def Parent(n):
    return (n-1)/2