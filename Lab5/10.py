import re

string = input()

def to_camel(s):
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == "_":
            s[i + 1] = s[i + 1].upper()
    SSS = "".join(a for a in s if a != "_")
    return SSS

print(to_camel(string))

