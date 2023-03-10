from e_polygon import EquilateralPolygon
import math

class Square(EquilateralPolygon):
    def __init__(self, num_sides, side_length):
        super().__init__(num_sides, side_length)

    def GetArea(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.num_sides * EquilateralPolygon.side_length


square = Square(4, 5)





