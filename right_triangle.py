from triangle import Triangle 



class RightTriangle(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def area(self):
        return (self.a * self.b) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def get_corners(self):
        return self.corners
    
    def is_right_triangle(self):
        if self.a ** 2 + self.b ** 2 != self.c ** 2:
            return "Error: This is not a right triangle."
    

    





