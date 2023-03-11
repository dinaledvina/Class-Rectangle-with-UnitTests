from e_polygon import EquilateralPolygon
import math


class Hexagon(EquilateralPolygon):
	def __init__(self, num_sides, side_length):
		super().__init__(6, side_length)



	def GetArea(self):
		return 3 * self.side_length ** 2 * math.sqrt(3) / 2


	def GetPerimeter(self):
		return super().GetPerimeter()















