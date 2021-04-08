def binarySearch(A, item, left, right):
    if left <= right:
        mid = (left + right)//2
        if item == A[mid]:
            return mid
        elif item < A[mid]:
            return binarySearch(A, item, left, mid-1)
        else:
            return binarySearch(A, item, mid+1, right)