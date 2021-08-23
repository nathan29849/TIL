# 백준 9935번 문자열 폭발
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

string = input().rstrip()
exp = input().rstrip()

def solution(string, exp):
    n = len(string)
    m = len(exp)
    temp = []
    for i in range(n):
        temp.append(string[i])
        if len(temp) >= m:
            if temp[-1] == exp[-1]:
                flag = True
                # len(temp) = 8 -> 7, 6
                # len(exp) = 2  -> 1, 0
                for x in range(len(temp)-1, len(temp)-m-1, -1):
                    if temp[x] != exp[x-(len(temp)-m)]:
                        flag = False
                        break
                if flag:    # 만약 temp의 끝 부분들이 exp와 같다면 제거해야 함.
                    for y in range(m):
                        temp.pop()
    result = ""
    for i in range(len(temp)):
        result += temp[i]
    return result if len(result) > 0 else "FRULA"

print(solution(string, exp))