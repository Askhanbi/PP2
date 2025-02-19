import re

string = str(input())

if re.fullmatch(r"[A-Z]+[a-z]+",string):
    print("Match")
else:
    print("UnMatch")