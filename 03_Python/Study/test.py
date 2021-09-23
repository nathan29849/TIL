from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    arr = []
    string = input().rstrip()
    while True:
        temp = list(map(str, input().split()))
        if len(temp) == 1 and temp[0] == "END":
            break
        else:
            arr.append(temp)

    for i in arr:
        temp = ""
        command, a, b = i
        b = int(b)
        if command == "I":
            if b == len(string):
                temp = string + a
            else:
                for j in range(len(string)):
                    if j == b:
                        temp += a
                    temp += string[j]
            string = temp
        else:
            print(string[int(a):b+1])

