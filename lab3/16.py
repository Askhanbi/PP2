# Functions 1    Task 5

import itertools

def All_Permutations(string):
    a = list(itertools.permutations(string))
    for i in range(len(a)):
        print("".join(a[i]))

string = input("You're string: ")
All_Permutations(string)