from shape import Shape



class Rectangle(Shape):
    def __init__(self, length, width, x = 0, y = 0):
        super().__init__(x, y)
        self.length = length
        self.width = width
    
    def GetLength(self):
        return self.length
    
    def GetWidth(self):
        return self.width
    
    def GetArea(self):
        return self.length * self.width
    
    def GetPerimeter(self):
        return 2 * (self.length + self.width)


