# 백준 5052번 전화번호 목록
from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, node):
        self.node = node
        self.next = [None]*10
        self.flag = False

class Graph:
    def __init__(self):
        self.adjList = [0] * 10
    
    def insertEdge(self, string):
        x = int(string[0])
        if self.adjList[x] == 0:
            new = Node(x)
            self.adjList[x] = new
   
        
        temp = self.adjList[x]
        if len(string) == 1:
            temp.flag = True
        else:
            if temp.flag == True:
                return 
        for i in range(1, len(string)):
            S = int(string[i])
            if temp.next[S] is None:
                w = Node(S)
                temp.next[S] = w
            else:
                if temp.next[S].flag != False:
                    return False
            if i == len(string)-1: # 마지막 원소라면
                temp.next[S].flag = True
            temp = temp.next[S]
        return True
                

def solution(phonebook):
    phonebook.sort()
    n = len(phonebook)
    g = Graph()
    for number in phonebook:
        result = g.insertEdge(number)
        if result != True:
            return "NO"
    return "YES"


    # 시간 초과
    # for i in range(n):
    #     for j in range(i+1, n):
    #         m = len(phonebook[i]) 
    #         if len(phonebook[i]) < len(phonebook[j]):
    #             if phonebook[j][:m] == phonebook[i]:
    #                 return "NO"
    # return "YES"


t = int(input())
for x in range(t):
    n = int(input())
    phonebook = []
    for i in range(n):
        phonebook.append(input().rstrip())
    print(solution(phonebook))
