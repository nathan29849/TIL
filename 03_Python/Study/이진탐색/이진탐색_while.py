def binarySearch(target, arr, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


arr = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]
target = 7

print(binarySearch(target, arr, 0, 9))    