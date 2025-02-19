import re

String = str(input())

def match(a):
    if re.fullmatch(r"ab{2,3}", a):
        return "Match"
    else:
        return "No Match"

print(match(String))