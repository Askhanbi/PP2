import re

string = str(input())

def matches(a):
    if re.fullmatch(r"^a.*b$",a):
        return "Match"
    else:
        return "UnMatch"
    
print(matches(string))