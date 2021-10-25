import numpy as np
my_arr = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
my_list = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_arr.shape)     # (10, ) (배열의 크기를 출력함, 뒤에 쉼표가 붙음)

my_arr2 = np.arange(0, 10, 2) # [0 2 4 6 8]  
print(my_arr2.shape) # (5, )

my_arr3 = np.zeros(5)   # [0. 0. 0. 0. 0.]  -> 0. : 실수
print(my_arr3.shape) # (5, )

my_arr4 = np.zeros((2, 3))  # (행, 열)
# [[0. 0. 0.]
#  [0. 0. 0.]]
print(my_arr4.shape)    # (2, 3) : (행, 열)

my_arr5 = np.full((2, 3), 8)    # (행, 열), 채울 수
# [[8 8 8]
#  [8 8 8]]
print(my_arr5.shape)    # (2, 3)

my_arr6 = np.eye(4) # 4x4 행렬을 만들고, 대각선을 채운다. (실수로 채움)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
print("my_arr6[1]", my_arr6[1])
print(my_arr6.shape)   # (4, 4)

my_arr7 = np.random.random((2, 4))  # random values in the half-open interval [0.0 1.0]
# [[0.12089772 0.15911176 0.69344681 0.4692327 ]
#  [0.01539711 0.67858001 0.85492088 0.62552196]]
print(my_arr7)

list1 = [1, 2, 3, 4, 5]
r1 = np.array(list1)
print(r1)   # [1 2 3 4 5]
print(r1[0]) # 1
print(r1[4]) # 5

list2 = [6, 7, 8, 9, 0]
r2 = np.array([list1, list2])   # 2차원 array
# [[1 2 3 4 5]
#  [6 7 8 9 0]]
print(r2)
print(r2[1])    # [6 7 8 9 0]

print(r2.shape) # (2, 5)
print(r2[1,1]) # 7 [행, 열]
print(r2[1,3]) # 9 [행, 열]
print(r2>7)     
# [[False False False False False]
#  [False False  True  True False]]
print(r2[1]>7)  # [False False  True  True False]
print(r2[r2>7]) # [8 9] r2 중 조건에 맞는 r2를 array 형태로 출력

nums = np.arange(20)
print(nums)

odd_num = nums[nums % 2 == 1]
print(odd_num)

a = np.array([[1, 2, 3, 4, 5],
                [4, 5, 6, 7, 8],
                [9, 8, 7, 6, 5]])

print(a)

b1 = a[1:3, :3]
#[[4 5 6]
#[9 8 7]]
print(b1)

b2 = a[-2:, -2:]
print(b2)

# [[7 8]
#  [6 5]]

b3 = a[1:, 2:]
# [[6 7 8]
#  [7 6 5]]
print(b3)


b3[0, 2] = 88
# [[ 6  7 88]
#  [ 7  6  5]]
print(b3)

print(a)
# [[ 1  2  3  4  5]
#  [ 4  5  6  7 88]
#  [ 9  8  7  6  5]]

b4 = a[2:, :]
print(b4.shape)
# [[ 9  8  7  6  5]] (2차원 배열로 출력됨을 인지해야 함)
# (1, 5)

x = np.array([2, 3])
y = np.array([4, 2])
print(x, y)
z = x + y
print(z)

names = np.array(["Ann", "Joe", "Mark"])
heights = np.array([1.5, 1.78, 1.6])
weights = np.array([65, 46, 59])

bmi = weights/heights ** 2
print(bmi)  # [28.88888889 14.51836889 23.046875  ]

print("Overweight: ", names[bmi>25])
print("Underweight: ", names[bmi<18.5])
print("Healthy: ", names[(bmi >= 18.5) & (bmi <= 25)])

x2 = np.array([[1,2,3], [4,5,6]])
y2 = np.array([[7,8], [9,10], [11,12]])
print(np.dot(x2, y2))   # 행렬의 곱셈
# [[ 58  64]
#  [139 154]]

aa = np.array([(1,2,3), (4,5,6), (7,8,9)])
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(aa)

print(aa.cumsum())  # 누적합 [ 1  3  6 10 15 21 28 36 45]
print(aa.cumsum(axis=0)) # 축 = 0 ... 열 기준으로 값을 더한다.
# [[ 1  2  3]
#  [ 5  7  9]
#  [12 15 18]]
print(aa.cumsum(axis=1)) # 축 = 1 ... 행 기준으로 값을 더한다.
# [[ 1  3  6]
#  [ 4  9 15]
#  [ 7 15 24]]

ages = np.array([34, 12, 37, 5, 13])
sorted_ages = np.sort(ages)
print(ages) # [34 12 37  5 13]
print(sorted_ages)  # [ 5 12 13 34 37]

ages.sort()
print(ages[::-1]) # [ 5 12 13 34 37]  [::-1]끝에 이거 붙이면 역순 정렬

ages = np.array([34, 12, 37, 5, 13])
print(ages.argsort()[::-1]) # [3 1 4 0 2] 인덱스만 sort 해 줌, [::-1]끝에 이거 붙이면 역순 정렬

temp_list = [1, 2, 3]
temp_list2 = [4, 5, 6]
temp_ndarray = np.array(temp_list)
temp = np.array([temp_list, temp_list2, [7, 8, 9]])
print(temp[:, 1]) 
print(temp[0:2, 1:3])
print(temp_ndarray>2)
print(temp_ndarray > temp[0, 2]) # temp[0, 2] = 3
print(temp_ndarray[temp_ndarray>1])

a=np.array([[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10], 
            [11, 12, 13, 14, 15]])

b = a[-2:, -3:]
b[1, 2] = 77
print(b)