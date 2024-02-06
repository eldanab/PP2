class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.l = length
    def area(self):
        return self.l**2
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w

sqr = Square(12)
print(sqr.area())

rec = Rectangle(8, 3)
print(rec.area())