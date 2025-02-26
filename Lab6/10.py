# Directories and Files  ex5
anylist = map(int, input().split())

path_to_file = input('Where to write?: ')

with open(path_to_file, 'w') as a:
    for i in anylist:
        a.write("%s\n" % i)