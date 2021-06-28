# 백준 9237번
from sys import stdin

def invite(n, tree):
    tree.sort(reverse=True)

    for i in range(n):  # 끝나는 시간 만들기 (원래 나무가 자랄 시간 + 심기 시작한 시간)
        tree[i] += i

    max_num = max(tree) # 끝나는 시간이 가장 큰 원소 골라내기
    print(tree)
    return max_num+2    # 처음 심을 때 소요되는 1일 + 다 끝나고 나서 이장님을 불러야 하므로 +1




n = int(stdin.readline())
tree = list(map(int, stdin.readline().split()))

result = invite(n, tree)
print(result)