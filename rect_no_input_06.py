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


#### Added methods from super class Shape
    # def set_corners(self, top_left, bottom_right):
    #     self.top_left = top_left
    #     self.bottom_right = bottom_right
    
    # def get_corners(self):
    #     return (self.top_left, self.bottom_right)






rect = Rectangle(5, 10)

print("Length:", rect.GetLength())     
print("Width:", rect.GetWidth())       
print("Area:", rect.GetArea())        
print("Perimeter:", rect.GetPerimeter())   

