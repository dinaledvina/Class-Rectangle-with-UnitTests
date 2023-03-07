import unittest
from rect_no_input_06 import Rectangle
from right_triangle_sub_of_rectangle import RightTriangle

# class TestRightTriangle(unittest.TestCase):
#     def test_get_length(self):
#         rt = RightTriangle(3, 4)
#         self.assertEqual(rt.GetLength(), 3)
    
#     def test_get_width(self):
#         rt = RightTriangle(3, 4)
#         self.assertEqual(rt.GetWidth(), 4)
    
#     def test_get_area(self):
#         rt = RightTriangle(3, 4)
#         self.assertEqual(rt.GetArea(), 12)
    
#     def test_get_perimeter(self):
#         rt = RightTriangle(3, 4)
#         self.assertEqual(rt.GetPerimeter(), 12 + (3 ** 2 + 4 ** 2) ** 0.5)




class TestRightTriangle(unittest.TestCase):
    def setUp(self):
        self.rt = RightTriangle(3, 4)
    
    def test_get_length(self):
        self.assertEqual(self.rt.GetLength(), 3)
    
    def test_get_width(self):
        self.assertEqual(self.rt.GetWidth(), 4)
    
    def test_get_area(self):
        self.assertEqual(self.rt.GetArea(), 6.0)
    
    def test_get_perimeter(self):
        self.assertEqual(self.rt.GetPerimeter(), 12.0 )


if __name__ == '__main__':
    unittest.main()

