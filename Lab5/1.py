import re

string = str(input())

if re.fullmatch(r'ab*',string):
    print("String has letter a")
else:
    print("String has not letter a")