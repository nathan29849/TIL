input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []
    for split_size in range(1, n//2 + 1):
        splited = []

        splitted = [
            string[i:i+split_size] for i in range(0, n, split_size)
        ]
        compressed = ""
        count = 1   # 이전 값과 자기 값을 비교하는 것이기 때문에..
        for j in range(1, len(splitted)):
            prev, cur = splitted[j-1], splitted[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count)+prev)
                else:
                    compressed += prev
                count = 1

        if count > 1:
            compressed += (str(count)+splitted[-1])
        else:
            compressed += splitted[-1]
        compression_length_array.append(len(compressed))


        print(compressed)

    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!