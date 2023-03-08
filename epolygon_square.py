from e_polygon import EquilateralPolygon

class Square(EquilateralPolygon):
    def __init__(self):
        super().__init__(4)

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.num_sides * EquilateralPolygon.side_length


square = Square()
print("Square area:", square.area())
print("Square perimeter:", square.perimeter())
