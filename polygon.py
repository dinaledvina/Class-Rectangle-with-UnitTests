
class EquilateralPolygon:
   

    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def GetPerimeter(self):
        return self.num_sides * self.side_length

    def GetArea(self):
        apothem = self.side_length / (2 * (math.tan(math.pi / self.num_sides)))
        return (self.GetPerimeter() * apothem) / 2








