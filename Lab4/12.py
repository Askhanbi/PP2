# math    Task 3

import math

side = int(input("Input number of sides: "))
length_of_side = int(input("Input the length of a side: "))

apothem = length_of_side / (2 * math.tan(math.pi / side))
area = int(side * length_of_side * apothem) / 2

print(area)