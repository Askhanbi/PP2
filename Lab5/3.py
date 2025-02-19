import re

String = str(input())

if re.fullmatch("^[a-z]+_[a-z]+$", String):
    print("Match")
else:
    print("UnmatCh")