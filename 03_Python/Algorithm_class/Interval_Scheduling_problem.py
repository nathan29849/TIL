A = [4, 1, 3, 8, 6, 2, 5, 7, 10]

def partition(A, left, right):
    i = left + 1
    j = right
    pivot = A[left]
    while(i<=j):
        while(i<=right and A[i] < pivot):
            i += 1
        while(j>=left and A[j] >= pivot):
            j -= 1
        if (i<=j):
            A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j


def quick_sort(numbers, left, right):
    if left <= right:
        pivot_point = partition(numbers, left, right)
        quick_sort(numbers, left, pivot_point - 1)  # left side
        quick_sort(numbers, pivot_point + 1, right)     # right side


quick_sort(A, 0, len(A)-1)
