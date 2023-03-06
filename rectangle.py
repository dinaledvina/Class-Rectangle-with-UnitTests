class Rectangle:
    def __init__(self, length, width):
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

rect = Rectangle(5, 10)

print("Length:", rect.GetLength())     
print("Width:", rect.GetWidth())       
print("Area:", rect.GetArea())        
print("Perimeter:", rect.GetPerimeter())   

