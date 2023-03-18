import unittest
from square import Square

class TestSquare(unittest.TestCase):

	def test_area(self):
		square = Square(5)
		self.assertAlmostEqual(square.GetArea(), 25)

	def test_perimeter(self):
		square = Square(5)
		self.assertEqual(square.GetPerimeter(),20)
		
		
	def test_set_length(self):
		square = Square(7)
		square.set_length(7)
		self.assertEqual(square.side_length, 7)

		self.assertEqual(square.corners, ((0,0), (7, 0), (7, 7), (0, 7)))


	def test_set_corners(self):
		square = Square(7)
		square.set_corners((0,0), (7,7))
		self.assertEqual(square.get_corners(), ((0,0), (7,0), (7,7), (0,7)))
		self.assertEqual(square.side_length, 7)

if __name__ == '__main__':
    unittest.main()
