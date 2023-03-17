from shape import Shape



class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
        self.corners = ((0,0), (self.length, 0), (self.length, self.width), (0, self.width))
    
    def GetLength(self):
        return self.length
    
    def GetWidth(self):
        return self.width
    
    def GetArea(self):
        return self.length * self.width
    
    def GetPerimeter(self):
        return 2 * (self.length + self.width)
    

    def set_corners(self, corner1, corner2):
        (x1, y1), (x2, y2) = corner1, corner2
        self.length = x2 - x1
        self.width = y2 - y1
        self.corners = (corner1, (x2, y1), corner2, (x1, y2))

    def get_corners(self):
        return self.corners

