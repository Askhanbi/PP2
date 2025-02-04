# TASK3     class
class SHAPE:
    def area(self):
        return 0
    
class RECTANGLE(SHAPE):
    def __init__(self, length, width):
        self.Lenght = length
        self.Width = width

    def area(self):
        return self.Lenght * self.Width
    

write_to_length = int(input("Length: "))
write_to_width = int(input("Width: "))

rectangle = RECTANGLE(write_to_length, write_to_width)
print(rectangle.area())