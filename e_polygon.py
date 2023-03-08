import math

# class EquilateralPolygon:
#     def __init__(self, num_sides, side_length):
#         self.num_sides = num_sides
#         self.side_length = side_length

#     def GetPerimeter(self):
#         return self.num_sides * self.side_length

#     def GetArea(self):
#         apothem = self.side_length / (2 * (math.tan(math.pi / self.num_sides)))
#         return (self.GetPerimeter() * apothem) / 2


# my_epoly = EquilateralPolygon(3, 5)

# print(my_epoly.GetArea())      
# print(my_epoly.GetPerimeter())





class EquilateralPolygon:
    side_length = 0

    def __init__(self, num_sides):
        self.num_sides = num_sides

    def perimeter(self):
        return self.num_sides * self.side_length

    def area(self):
        apothem = self.side_length / (2 * (math.tan(math.pi / self.num_sides)))
        return (self.perimeter() * apothem) / 2


EquilateralPolygon.side_length = 5

triangle = EquilateralPolygon(3)
print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())
