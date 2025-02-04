# Function 1     Task 10

"""
input: 
apple, banana, apple, cherry

output:
apple, banana, cherry
"""

def unique(a):
    b = [a[0]]
    for i in a:
        Qwerty = True
        for j in b:
            if i == j:
                Qwerty = False
                break
        if Qwerty:
            b.append(i)
    return b

Thislist = [str(i) for i in input().split()]
print(unique(Thislist))