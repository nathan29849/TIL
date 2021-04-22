def coin(n, A):
    C = [[0 for i in range(len(A)+1)] for j in range(n+1)]
    print(C)
    for i in range(n+1):
        for j in range(len(A)+1):
            if j == 0:
                C[i][j] = 0
            elif j > 0 and i == 0:
                C[i][j] = 1
            # elif j == 1 and i < A[0]:  
            #     C[i][j] = 0
            elif i == 1:
                C[i][j] = 1
            elif i == 2:
                C[i][j] = 1

            elif i < A[-1]:
                C[i][j] = C[i][j-1]
            else:
                C[i][j] = C[i-j][j] + C[i][j-1]
                C[3][2] = C[1][2] + C[3][1]
    print(C)




A = [1, 3, 5]

coin(10, A)

[[0, 1, 1, 1]
, [0, 1, 1, 1]
, [0, 1, 1, 1]
, [0, 0, 1, 0]
, [0, 0, 0, 0]
, [0, 0, 1, 2]
, [0, 0, 0, 0]
, [0, 0, 1, 1]
, [0, 0, 0, 2]
, [0, 0, 1, 1]
, [0, 0, 0, 1]]