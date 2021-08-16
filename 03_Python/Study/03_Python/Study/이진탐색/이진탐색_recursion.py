def binarySearch(target, arr, start, end):
    if start > end:
        return None

    mid = (start+end)//2
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] > target:
        return binarySearch(target, arr, start, mid-1)  # 재귀를 끝내려면 꼭 return을 넣어주어야 한다.
    else:
        return binarySearch(target, arr, mid+1, end)     # 재귀를 끝내려면 꼭 return을 넣어주어야 한다.



arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

print(binarySearch(target, arr, 0, 9))
