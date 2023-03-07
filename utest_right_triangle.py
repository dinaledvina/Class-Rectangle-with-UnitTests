import unittest
from rectangle import Rectangle
from right_triangle import RightTriangle


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

