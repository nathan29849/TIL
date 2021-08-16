def factorial(n):
    # 이 부분을 채워보세요!
    if n == 1:
        return 1
    
    return n * factorial(n-1)
    

# RecursionError가 뜨면, 재귀함수 내의 탈출조건이 제대로 작성이 되었는지 확인해야 한다.

print(factorial(5))