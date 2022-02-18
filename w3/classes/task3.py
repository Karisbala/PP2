class Shape():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

s = Rectangle(12, 3)

print(s.area())

print(Rectangle().area())  
