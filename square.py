
from e_polygon import EquilateralPolygon
import math

class Square(EquilateralPolygon):
    def __init__(self):
        super().__init__(4)

    def GetArea(self):
        return self.side_length ** 2

    def GetPerimeter(self):
        return self.num_sides * EquilateralPolygon.side_length


square = Square()
print("Square area:", square.GetArea())
print("Square perimeter:", square.GetPerimeter())
