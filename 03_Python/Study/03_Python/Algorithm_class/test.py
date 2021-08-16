def rebuildHeap(A, r, n):
    current = r
    value = A[r]
    while (2*current + 1 < n):
        leftChild = 2*current + 1
        rightChild = 2*current + 2

        if rightChild < n and A[rightChild] > A[leftChild]:
            largerChild = rightChild
        else:
            largerChild = leftChild
        
        if value < A[largerChild]:
            A[current] = A[largerChild]
            current = largerChild
        else:   # 더 이상 작지 않으면,,,
            break

    A[current] = value

def heapsort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        rebuildHeap(A, i, n)

    heap_size = n
    for last in range(n-1, 0, -1):
        A[0], A[last] = A[last], A[0]
        heap_size -= 1
        rebuildHeap(A, 0, heap_size)

A = [1, 9, 20, 30 , 8, 2, 1, 3]
heapsort(A)
print(A)