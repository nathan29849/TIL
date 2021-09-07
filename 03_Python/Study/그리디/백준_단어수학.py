# 백준 1339번 단어 수학
from sys import stdin
input = stdin.readline

n = int(input())
arr = []
for i in range(n):
    temp = input().rstrip()
    arr.append(temp)

number = [0]*30
for string in arr:
    m = len(string)
    for s in range(m):
        number[ord(string[s])-65] += 10**(m-s-1)

number.sort(reverse=True)
count = 9
result = 0
for a in number:
    result += count * a
    count -= 1
print(result)

# # 백준 1339번 단어 수학
# from sys import stdin
# input = stdin.readline

# n = int(input())
# arr = [[]for _ in range(9)] # 수의 최대 길이 8 (0 ~ 8까지 인덱스로 표현)
# for i in range(n):
#     temp = input().rstrip()
#     length = len(temp)
#     arr[length].append(temp) # 같은 길이의 문자열을 하나의 리스트에 포함시키기

# alpha = [-1] * (10) # A B C D E F G H I J (알파벳 최대 10개)
# new = list(reversed(arr)) # 길이가 긴 문자열부터 탐색하기 위해 뒤집는다.
# result = [] # 숫자 변환이 모두 끝난 문자열을 int로 변환하여 저장
# count = 9     # 9부터 내림차순으로 알파벳에 저장될 숫자를 따로 보관

# for i in range(8):
#     temp_length = len(new[i])
#     if temp_length < 1: # 아무 원소도 없다면 continue
#         continue
#     elif i == 7:   # 한자리 숫자라면
#         for j in range(temp_length):
#             idx = ord(new[i][j][0])-65
#             if alpha[idx] == -1: # 만약 한 번도 안나왔던 알파벳이라면
#                 alpha[idx] = count
#                 count -= 1
#             result.append(alpha[idx])
#     else:                   # 두자리 숫자 이상이라면
#         for j in range(temp_length):
#             x = new[i][j][0]           # 가장 높은 자리 숫자만 뽑아내기             
#             idx = ord(x)-65
#             if alpha[idx] == -1: # 만약 한 번도 안나왔던 알파벳이라면
#                 alpha[idx] = count
#                 count -= 1
#             result.append(alpha[idx]*(10**(7-i)))
#             # 나머지 자리 숫자
#             new[i+1].append(new[i][j][1:])

# # print(result)
# print(sum(result))