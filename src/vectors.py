import math

class Vector:
    '''Simple class for a 2D vector'''
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


def dot_product(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y


def projection(vec1, vec2):
    '''Project vec1 onto vec2'''
    return vec2.scale(dot_product(vec1, vec2) / vec2.magnitude()**2)