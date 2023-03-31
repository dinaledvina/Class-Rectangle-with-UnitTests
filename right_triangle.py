
class RightTriangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        if self.a ** 2 + self.b ** 2 != self.c ** 2:
            raise ValueError("Not a right triangle")
        self.corners = ((0, 0), (self.a, 0), (0, self.b))

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def get_corners(self):
        return self.corners
