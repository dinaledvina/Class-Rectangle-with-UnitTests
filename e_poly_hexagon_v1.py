from e_polygon import EquilateralPolygon
import math


class Hexagon(EquilateralPolygon):
	def __init__(self):
		super().__init__(6)



	def GetArea(self):
		return 3 * self.side_length ** 2 * math.sqrt(3) / 2


	def GetPerimeter(self):
		return 6 * self.side_length



hexagon = Hexagon()

print("Hexagon area:", hexagon.GetArea())
print("Hexagon perimeter:", hexagon.GetPerimeter())









