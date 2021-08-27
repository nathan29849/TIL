# 백준 2671번 잠수함 식별
from sys import stdin
import re
input = stdin.readline

string = input().rstrip()
p = re.compile("(100+1+|01)+")
if p.fullmatch(string) is not None:
    print("SUBMARINE")
else:
    print("NOISE")

