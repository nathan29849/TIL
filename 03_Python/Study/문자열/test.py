import sys

def kmp(string):
    j = 0
    table = [0] * len(string)
    for i in range(1,len(string)):
        while j > 0 and string[i] != string[j]:
            j = table[j-1]
        if string[i] == string[j]:
            j += 1
            table[i] = j
            print("table:", table)
    return max(table)

txt = sys.stdin.readline().rstrip()

ans = 0
for i in range(len(txt)):
    pattern = txt[i:len(txt)]
    print("pattern:", pattern)
    ans = max(ans, kmp(pattern))

print(ans)