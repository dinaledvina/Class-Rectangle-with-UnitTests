from e_polygon import EquilateralPolygon
import math


class Hexagon(EquilateralPolygon):
	def __init__(self, num_sides, side_length):
		super().__init__(num_sides, side_length)



	def GetArea(self):
		hexagon = Hexagon(6, 5)
		return 3 * self.side_length ** 2 * math.sqrt(3) / 2















