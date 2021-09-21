import math


class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_p(self):
        return (self.w + self.h) * 2

    def get_s(self):
        return self.w * self.h


r = Rectangle(4, 5)


# print(r.get_s())

class Circle():
    def __init__(self, r):
        self.r = r

    def get_circumference(self):
        return math.pi * 2 * self.r

    def get_area(self):
        return math.pi * self.r * self.r

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_p(self):
        return self.a + self.b + self.c

    def get_a(self):
        p = self.get_p() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))



c = Circle(5)

t = Triangle(3, 4, 6)

print(c.get_area())