from triangle import Triangle 



class RightTriangle(Triangle):
    def __init__(self, a, b):
        c = (a ** 2 + b ** 2) ** 0.5
        if a ** 2 + b ** 2 != c ** 2:
        #if not math.isclose(a ** 2 + b ** 2, c ** 2, rel_tol=1e-9):   
            raise ValueError("Not a right triangle")
        super().__init__(a, b, c)
        
    def is_right_triangle(self):
        return True

    def area(self):
        return (self.a * self.b) / 2

    def perimeter(self):
        return self.a + self.b + self.c

    def get_corners(self):
        return self.corners
    


    





