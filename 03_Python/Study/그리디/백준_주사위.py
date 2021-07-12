# 백준 1041번
from sys import stdin

def findMin(n, dice):
    # dice.sort()  # 오름차순으로 정렬 -> A B C D E F 면이 각각 정해져있기 때문에 무작위로 섞으면 안됨 .. 틀린 이유
    result = 0
    new = []
    
    if n == 1:    # 주사위가 1개일 때
        result = sum(dice) - max(dice)
        return result
    else:
        new.append(min(dice[0], dice[5]))
        new.append(min(dice[1], dice[4]))
        new.append(min(dice[2], dice[3]))
        new.sort()

        result += new[0]*(n**2) + new[1]*(n**2 - (n-2)**2) + new[2]*4   # 맨 꼭대기 층
        result += (new[0]*(n**2 - (n-2)**2) + new[1]*4) * (n-1)   # 모서리 4개 
        return result
            
n = int(stdin.readline())
dice = list(map(int, stdin.readline().split()))

result = findMin(n, dice)
print(result)
