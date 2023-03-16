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
        self.corners = (corner1, corner2)

    def get_corners(self):
        return self.corners
    
   def test_set_get_corners(self):
        self.rect.set_corners((0,0), (7,12))
        self.assertEqual(self.rect.get_corners(), ((0,0), (7,0), (7,12), (0,12)))
        self.assertEqual(self.rect.GetLength(), 7)
        self.assertEqual(self.rect.GetWidth(), 12)
