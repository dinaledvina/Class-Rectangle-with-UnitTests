from triangle import Triangle


class RightTriangle(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if self.a ** 2 + self.b ** 2 != self.c ** 2:
            raise ValueError("Not a right triangle")
        self.corners = ((0, 0), (self.a, 0), (0, self.b))



