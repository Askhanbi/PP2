# Generators     Task 4

x = int(input())
y = int(input())

def squares(x, y):
    return [i * i for i in range(x,y)]
    

for square in squares(x, y + 1):
    print(square)