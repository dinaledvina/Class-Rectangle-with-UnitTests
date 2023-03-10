from e_polygon import EquilateralPolygon
import math

class Square(EquilateralPolygon):
    def __init__(self, num_sides, side_length):
        super().__init__(num_sides, side_length)

    def GetArea(self):
        square = Square(4, 5)
        return self.side_length ** 2

    def perimeter(self):
        square = Square(4, 5)
        return self.num_sides * self.side_length







