class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates: x =", self.x, "y =", self.y)
    def move(self, x1, y1):
        self.x = x1
        self.y = y1
    def dist(self, second):
        x2 = second.x
        y2 = second.y
        dist = ((x2 - self.x)**2 + (y2 - self.y)**2)**0.5
        return dist

A = Point(2, 3)
B = Point(-1, 4)
A.show()
A.move(1, 5)
A.show()
print(A.dist(B))
