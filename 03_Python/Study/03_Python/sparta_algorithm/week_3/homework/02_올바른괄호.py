# Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 
# 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 
# 예를 들어
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.

# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 
# 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.

# "(())()" # True
# "(((("   # False

# s = "(())()"
s = "()())(()" # 첫번째 풀이는 이 테스트 케이스를 통과하지 못함.
# 중간에 틀린값이 나오면 찾아낼 수 없음 -> 고로 내 풀이는 틀렸다.
# def is_correct_parenthesis(string):
#     left = 0
#     right = 0
#     if string[0] ==")" or string[-1] == "(":
#         return False

#     for i in string:
#         if i == "(":
#             left += 1
#         else:
#             right += 1

#     if left != right:
#         return False
#     else:
#         return True

# 문제 해설(Stack이용)
def is_correct_parenthesis(string):
    start_list = []
    for i in string:
        if i == "(":
            start_list.append(i)
        else:   # ")"
            if len(start_list) == 0:
                return False
            start_list.pop()

    if len(start_list) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!