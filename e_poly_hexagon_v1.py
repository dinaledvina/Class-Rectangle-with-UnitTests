from e_polygon import EquilateralPolygon
import math


class Hexagon(EquilateralPolygon):
	def __init__(self, num_sides):
		super().__init__(num_sides)



	def GetArea(self):
		return 3 * self.side_length ** 2 * math.sqrt(3) / 2


	def GetPerimeter(self):
		return self.num_sides * self.side_length



hexagon = Hexagon(6)

print("Hexagon area:", hexagon.GetArea())
print("Hexagon perimeter:", hexagon.GetPerimeter())









