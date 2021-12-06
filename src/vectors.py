import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def normalize(self):
        self.scale(1 / self.magnitude())

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y
