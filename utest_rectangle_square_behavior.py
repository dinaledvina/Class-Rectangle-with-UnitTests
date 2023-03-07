# import unittest
# from rectangle import Rectangle
# from square import Square

# class TestSquare(unittest.TestCase):
#     def test_same_behavior_as_rectangle(self):
#         rect = Rectangle(5, 10)
#         square = Square(5)

#         self.assertEqual(rect.GetLength(), square.GetLength())
#         self.assertEqual(rect.GetWidth(), square.GetWidth())
#         self.assertEqual(rect.GetArea(), square.GetArea())
#         self.assertEqual(rect.GetPerimeter(), square.GetPerimeter())


# if __name__ == '__main__':
#     unittest.main()








import unittest
from rect_no_input_06 import Rectangle
from sq_subclass_of_rect import Square


class TestRectangleAndSquare(unittest.TestCase):
    def test_rectangle_and_square(self):
        rect = Rectangle(5, 10)
        square = Square(5)
        self.assertEqual(rect.GetLength(), 5)
        self.assertEqual(rect.GetWidth(), 10)
        self.assertEqual(rect.GetArea(), 50)
        self.assertEqual(rect.GetPerimeter(), 30)
        self.assertEqual(square.GetLength(), 5)
        self.assertEqual(square.GetWidth(), 5)
        self.assertEqual(square.GetArea(), 25)
        self.assertEqual(square.GetPerimeter(), 20)


if __name__ == '__main__':
    unittest.main()
