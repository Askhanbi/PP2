# Generators     Task 4

x = int(input())
y = int(input())

def squares(num):
    return pow(num, 2)

for i in range(x, y + 1):
    print(squares(i))