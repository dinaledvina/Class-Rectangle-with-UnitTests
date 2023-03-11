from e_polygon import EquilateralPolygon
import math

class Square(EquilateralPolygon):
    def __init__(self, side_length):
        super().__init__(4, side_length)

    def GetArea(self):
        return self.side_length ** 2








