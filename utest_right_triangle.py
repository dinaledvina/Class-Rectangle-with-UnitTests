import unittest
from rectangle import Rectangle
from right_triangle import RightTriangle


class TestRightTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = RightTriangle(3, 4)

    def test_get_area(self):
        self.assertEqual(self.triangle.GetArea(), 6.0)


        

if __name__ == '__main__':
    unittest.main()




