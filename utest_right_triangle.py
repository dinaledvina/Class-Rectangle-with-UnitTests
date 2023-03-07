import unittest
from rectangle import Rectangle
from right_triangle import RightTriangle


class TestRightTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = RightTriangle(3, 4)

    def test_get_area(self):
        self.assertEqual(self.triangle.GetArea(), 6.0)

#     def test_get_perimeter(self):
#         self.assertEqual(self.triangle.GetPerimeter(), 12.0)

#     def test_get_length(self):
#         self.assertEqual(self.triangle.GetLength(), 3)

#     def test_get_width(self):
#         self.assertEqual(self.triangle.GetWidth(), 4)
        

if __name__ == '__main__':
    unittest.main()




