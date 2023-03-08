from rectangle import Rectangle



class Hexagon(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def GetArea(self):
    	return (3 * (3 ** 0.5) / 2) * self.side ** 2


hexagon = Hexagon(5)

print("Side:", hexagon.side)
print("Length:", hexagon.GetLength())     
print("Width:", hexagon.GetWidth())       
print("Area:", hexagon.GetArea())        
print("Perimeter:", hexagon.GetPerimeter())









