# 백준 9663번 N-Queen 
from sys import stdin
input = stdin.readline
n = int(input())
board = [-1]*n

count = 0
def backtrack(board, k, n):
    global count
        
    for i in range(n):
        if place(board, k, i):
            board[k] = i
            if k == n-1:
                count += 1
                # print('chess :', end=" ")
                # for j in range(n):
                #     print(board[j], end=" ")
                # print()
                return
            else:
                backtrack(board, k+1, n)
            

def place(board, k, i):
    for j in range(k):
        if (board[j] == i) or (abs(board[j]-i) == abs(j-k)):
            return False
    return True


backtrack(board, 0, n)
print(count)