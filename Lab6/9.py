# Directories and Files  ex4
import os

path = input()

if not os.path.exists(path):
    print("File not find")
with open(path, "r") as a:
    print("Count lines: ", len(a.readlines()))

