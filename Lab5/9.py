import re

string = input()

p = re.sub(r"(?=[A-Z])" , " ", string)

print(p.strip())