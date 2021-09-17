# 백준 1759번 암호 만들기
from sys import stdin
from itertools import combinations
input = stdin.readline
L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
vowel = ["a", "e", "i", "o", "u"]
v_list = [] # vowel : 모음
c_list = [] # consonant : 자음
sentence = []
answer = []
for i in range(C):      # 주어진 문자들 중 모음과 자음을 분리
    if arr[i] in vowel:
        v_list.append(arr[i])
    else:
        c_list.append(arr[i])

for i in range(1, (L-2)+1):    # 모음 최소 1개, 자음 최소 2개를 남길 수 있는 for문
    temp_V = list(combinations(v_list, i))
    temp_C = list(combinations(c_list, L-i))
    for c in temp_C:
        for v in temp_V:
            sentence.append(c + v)
for i in range(len(sentence)):
    answer.append(''.join(list(sorted(sentence[i]))))
answer.sort()
for i in range(len(answer)):
    print(answer[i])