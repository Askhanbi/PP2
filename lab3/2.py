# TASK2   class
class SHAPE:
    def area(self):
        return 0
    
class SQUARE(SHAPE):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
length = float(input("Lenght: "))

sq = SQUARE(length)
print(sq.area())