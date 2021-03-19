array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    # 이 부분을 채워보세요!
    n = len(array1)
    m = len(array2)
    start_1 = 0
    start_2 = 0
    array3 = []
    for i in range(n+m):
        if start_1 == n and start_2 != m:
            array3.extend(array2[start_2:])
            return array3
        elif start_2 == m and start_1 != n:
            array3.extend(array1[start_1:])
            return array3
        elif start_1 == n and start_2 == m:
            return array3
        else:
            pass
        print("start_1", start_1)
        print("start_2", start_2)
        if array1[start_1] < array2[start_2]:
            print(array1[start_1])
            array3.append(array1[start_1])
            # array1.pop(start_1)
            start_1 += 1
            print(array3)
        else:
            print(array2[start_2])
            array3.append(array2[start_2])
            # array2.pop(start_2)
            start_2 += 1
            print(array3)


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!