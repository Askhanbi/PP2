# Generators     Task 1

n = int(input())

"""
for i in range(n):
    if i * i < n and i != 0:
        print(i * i)
"""
k = [i**2 for i in range(n)]
print(k)