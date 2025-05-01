# Classes and Objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point1 = Point(1, 3)
print(point1.x)
point1.draw()
