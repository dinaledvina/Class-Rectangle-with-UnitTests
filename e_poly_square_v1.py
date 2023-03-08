
from e_polygon import EquilateralPolygon
import math

class Square(EquilateralPolygon):
    def __init__(self, num_sides):
        super().__init__(num_sides)

    def GetArea(self):
        return self.side_length ** 2



square = Square(4)
print("Square area:", square.GetArea())
print("Square perimeter:", square.GetPerimeter())
