# Directories and Files  ex7

path1 = input()
path2 = input()

with open(path1) as i:
    with open(path2, "w") as j:
        for k in i:
            j.write(k)