# Generators     Task 2

n = int(input())

"""
for i in range(n):
    if i % 2 == 0:
        print(i)
"""
k = [i for i in range(n) if i % 2 == 0]
print(k)