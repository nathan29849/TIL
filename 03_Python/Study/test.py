
# 첫 번째 인덱스만 기준으로 둘 때
sample_list = [[4, 500], [2, 500], [3, 800]]
new_list = sorted(sample_list, key=lambda item: item[1])
print(new_list) # [[4, 500], [2, 500], [3, 800]]

# 첫 번째 인덱스를 기준으로 정렬한 후, 0번 째 인덱스로 나머지를 정렬하여줄 때
new_list = sorted(sample_list, key=lambda item: (item[1], item[0]))
print(new_list) # [[2, 500], [4, 500], [3, 800]]

