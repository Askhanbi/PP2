# Directories and Files  ex3
import os

s = input()
exists = os.path.exists(s)
print(exists)

if exists:
    print("File name: ")
    print(os.path.basename(s))
    print("Directory portion: ")
    print(os.path.dirname(s))