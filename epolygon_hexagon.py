from e_polygon import EquilateralPolygon
import math


class Hexagon(EquilateralPolygon):
    def area(self):
        return 3 * self.side_length ** 2 * math.sqrt(3) / 2

    def perimeter(self):
        return 6 * self.side_length



hexagon = Hexagon(6)

print("Hexagon area:", hexagon.area())
print("Hexagon perimeter:", hexagon.perimeter())