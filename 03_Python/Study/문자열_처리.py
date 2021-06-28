# param = [0, "INT", "BOOL", "BOOL", "SHORT", "LONG"]

# BOOL 1
# SHORT 2
# FLOAT 4
# INT 8
# LONG 16

def solution(param):
    arr = []
    for x in param:
        num = 0
        if x == "BOOL":
            num = 1
        elif x == "SHORT":
            num = 2
        elif x == "FLOAT":
            num = 4
        elif x == "INT":
            num = 8
        else: # x == "LONG"
            num = 16
    
        arr.append(num)
    
    print(arr)
    temp = ""
    result = ""
    for i in arr:
        while ((len(temp) + i)%i != 0):
            if len(temp) != 8:
                temp += "."
            else:
                result += temp + ","
                temp = ""
        temp += "#" * i
        print(temp)
        if len(temp) == 8:
            result += temp + ","
            temp = ""
        elif len(temp) == 16:
            result += temp[:8] + "," + temp[8:] + ","
            temp = ""

    if len(temp) > 0:   # 마지막에 8개보다 문자열이 적은 개수인 경우에는 "."을 추가해준다.
        while (len(temp)<8):
            temp += "."

        result += temp + ","

    if len(result) <= 144:  # 128 + 16 (마지막 쉼표까지 포함)
        print(result[:-1])
    else:
        print("HALT")
            

param = ["SHORT", "BOOL", "INT", "FLOAT"]
solution(param)    
