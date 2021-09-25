# def leaf_function(f):
#     result = f + 1
#     if f > 5:
#         return result
#     else:
#         temp = leaf_function(result)
#         print(temp)
#         return temp

    
# def main():
#     leaf_function(1)
#     return 0

# main()

def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n-1)