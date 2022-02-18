class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        return self.x, self.y


    def move(self, x, y):
        self.x += x
        self.y += y


    def dist(self, p):
        return ((p.x - self.x)** 2 + (p.y - self.y)** 2)**0.5


p1 = Point(4, 4)
p2 = Point(4, 3)

print(p1.show(), p2.show())

p1.move(3,1)

print(p1.show())

print(p1.dist(p2))