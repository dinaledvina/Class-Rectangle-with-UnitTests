from triangle import Triangle 



class RightTriangle(Triangle):
    def __init__(self, a, b, c):
        if a ** 2 + b ** 2 != c ** 2:
            raise ValueError("Not a right triangle")
        super().__init__(a, b, c)

    def area(self):
        return (self.a * self.b) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def get_corners(self):
        return self.corners



