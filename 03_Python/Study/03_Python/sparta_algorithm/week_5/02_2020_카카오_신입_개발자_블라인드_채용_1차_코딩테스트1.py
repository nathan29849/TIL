import math
input = "abcabcabcabcdededededede"
# 모든 경우의 수를 파악하여 최솟값을 도출해내는 문제임

def search(string, start, end):
    
    if string[start:end] == string[end:2*end]:
        

def string_compression(string):
    n = len(string)
    compression_list = []
    mid = math.ceil(n//2)
    for bundle in range(1, mid): # i : 1 2 3 ... n-1
        # n =3일때부터 일단 생각해보자 / 왜냐면 1, 2일때는 문자열 압축의 의미가 없으니까
        flag = True
        while flag:
            count = 0
            start = 0
            new_bundle = start+bundle   # 0 + 3  # 3 + 3
            if new_bundle > n:  # 범위 초과
                continue
            elif string[start:new_bundle] == string[new_bundel:new_bundle+bundle]:
                # 0:3 == 3:6
                # 3:6 == 6:9
                count += 1
                start += bundle
            else:
                continue
            
            if count >= 1:
                first_bundle = string[start:bundle]
                second_bundle = 
                a = f'{count}{last_bundle}'
            
        
        
        
        
        k = bundle + 1
        
        if 2*k > n: # 2k = 2bundle + 2
            for j in range(n-(2*k)): # j : 1 2 3 ... n-i-1
                


        else:
            break


        if string[0:i+1] == string[i+1: 2(i+1)]


        string[2(i+1):3(i+1)] == string[3(i+1): 4(i+1)]...
    return


print(string_compression(input))  # 14 가 출력되어야 합니다!