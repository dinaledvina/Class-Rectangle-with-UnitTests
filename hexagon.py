from rectangle import Rectangle



class Hexagon(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def GetArea(self):
        return self.length * self.width
    
    def GetPerimeter(self):
        return 2 * (self.length + self.width)

hexagon = Hexagon(5)

print("Side:", hexagon.side)
print("Length:", hexagon.GetLength())     
print("Width:", hexagon.GetWidth())       
print("Area:", hexagon.GetArea())        
print("Perimeter:", hexagon.GetPerimeter())









