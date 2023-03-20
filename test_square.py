
import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_get_length(self):
        self.assertEqual(self.square.GetLength(), 5)

    def test_get_width(self):
        self.assertEqual(self.square.GetWidth(), 5)

    def test_get_area(self):
        self.assertEqual(self.square.GetArea(), 25)

    def test_get_perimeter(self):
        self.assertEqual(self.square.GetPerimeter(), 20)

    def test_set_length(self):
    	self.square = Square(10)
    	self.square.set_length(10)
    	self.assertEqual(self.square.GetPerimeter(), 40)

    def test_set_corners(self):
    	self.square = Square(10)
    	self.square.set_corners((0,0), (10,10))
    	self.assertEqual(self.square.get_corners(), ((0,0), (10, 0), (10, 10), (0, 10)))

if __name__ == '__main__':
    unittest.main()
