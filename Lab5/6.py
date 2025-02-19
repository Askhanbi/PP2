import re

string = input()

p = re.sub("[\s,.]",":", string)

print(p)

