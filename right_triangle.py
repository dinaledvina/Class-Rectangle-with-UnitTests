from triangle import Triangle 



class RightTriangle(Triangle):
    def __init__(self, a, b):
        c = (a ** 2 + b ** 2) ** 0.5
        super().__init__(a, b, c)
        
    def is_right_triangle(self):
        return True

    def area(self):
        return (self.a * self.b) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def get_corners(self):
        return self.corners
    


    





