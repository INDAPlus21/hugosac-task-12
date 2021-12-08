import math

class Vector:
    '''Simple class for a 2D vector'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.limit = 0

    def pos(self):
        return (self.x, self.y)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def set_magnitude(self, mag):
        self.normalize()
        self.scale(mag)

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

        if self.limit > 0 and self.magnitude() > self.limit :
            self.set_magnitude(self.limit)

    def normalize(self):
        self.scale(1 / self.magnitude())

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

        if self.limit > 0 and self.magnitude() > self.limit :
            self.set_magnitude(self.limit)
    
    def subtract(self, vector):
        self.x -= vector.x
        self.y -= vector.y

        if self.limit > 0 and self.magnitude() > self.limit:
            self.set_magnitude(self.limit)

    def set_limit(self, lim):
        self.limit = lim

    def __str__(self):
        return f' ({self.x}, {self.y}), {self.magnitude()}'


def dot_product(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y

def vector_from_points(vec1, vec2):
    vec1.subtract(vec2)
    return vec1

def projection(vec1, vec2):
    '''Project vec1 onto vec2'''
    return vec2.scale(dot_product(vec1, vec2) / vec2.magnitude()**2)