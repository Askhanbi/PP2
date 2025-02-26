# Directories and Files  ex8

import os

path = input()

if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
    os.remove(path)
else:
    print("File not remove")