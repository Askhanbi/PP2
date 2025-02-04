# Fucntion 1   Task 12

def HestoGramm(numbers):
    for i in numbers:
        print("*" * i)

a = [int(y) for y in input().split()]
HestoGramm(a)