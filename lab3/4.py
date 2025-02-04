#TASK 4   class

import math

class POINT:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dest(self1, self2):
        return math.sqrt((self1.x - self2.x)**2 + (self1.y - self2.y))
    
#x1 = int(input("First x coordinate: "))
#y1 = int(input("First y coordinate: "))

x1,y1 = map(int, input("Coordinate of the First place: ").split())
P1 = POINT(x1,y1)

x2,y2 = map(int, input("Coordinate of the Second place: ").split())
P2 = POINT(x2,y2)

P1.show()
P2.show()

print(P1.dest(P2))