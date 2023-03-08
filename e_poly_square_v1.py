
from e_polygon import EquilateralPolygon
import math

class Square(EquilateralPolygon):
    def __init__(self, num_sides):
        super().__init__(num_sides)

    def area(self):
        return self.side_length ** 2



square = Square(4)
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())
