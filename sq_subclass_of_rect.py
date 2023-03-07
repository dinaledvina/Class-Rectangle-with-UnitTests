from rect_no_input_06 import Rectangle


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

square = Square(5)

print("Length:", square.GetLength())     
print("Width:", square.GetWidth())       
print("Area:", square.GetArea())        
print("Perimeter:", square.GetPerimeter())
