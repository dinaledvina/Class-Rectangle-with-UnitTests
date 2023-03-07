from rectangle import Rectangle


class RightTriangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def GetArea(self):
        return 0.5 * self.length * self.width
    
    def GetPerimeter(self):
        return self.length + self.width + (self.length ** 2 + self.width ** 2) ** 0.5

triangle = RightTriangle(3, 4)

print("Base:", triangle.GetLength())
print("Height:", triangle.GetWidth())
print("Area:", triangle.GetArea())
print("Perimeter:", triangle.GetPerimeter())
