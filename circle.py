from rect_no_input_06 import Rectangle
import math


# class Circle(Rectangle):
#     def __init__(self, radius):
#         super().__init__(2 * radius, 2 * radius)
#         self.radius = radius

#     def GetLength(self):
#         return 2 * self.radius

#     def GetWidth(self):
#         return 2 * self.radius

#     def GetArea(self):
#         return math.pi * self.radius ** 2

#     def GetPerimeter(self):
#         return 2 * math.pi * self.radius




class Circle(Rectangle):
    def __init__(self, radius):
        super().__init__(2 * radius, 2 * radius)
        self.radius = radius

    def GetLength(self):
        return 2 * self.radius

    def GetWidth(self):
        return 2 * self.radius

    def GetArea(self):
        return math.pi * self.radius ** 2

    def GetPerimeter(self):
        return 2 * math.pi * self.radius



my_circle = Circle(5)

print(my_circle.GetLength())    
print(my_circle.GetWidth())     
print(my_circle.GetArea())      
print(my_circle.GetPerimeter()) 

