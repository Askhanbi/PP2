# Directories and Files  ex2

import os
path = input()

print("Existence: ", os.access(path, os.F_OK))
print("readability: ", os.access(path,  os.R_OK))
print("writability: ", os.access(path, os.W_OK))
print("Executability: ", os.access(path, os.X_OK))