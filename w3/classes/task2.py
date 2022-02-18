class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        self.length = length
        super(Square, self).__init__()
        
    def area(self):
        return self.length**2

s = Square(12)

print(s.area())

print(Square().area())  
