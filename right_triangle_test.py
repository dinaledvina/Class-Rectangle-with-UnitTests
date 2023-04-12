import unittest
from right_triangle import RightTriangle

class TestRightTriangle(unittest.TestCase):

	def test_perimeter(self):
	    t = RightTriangle(3, 4)
	    self.assertEqual(t.perimeter(), 12)

	def test_area(self):
	    t = RightTriangle(3, 4)
	    self.assertEqual(t.area(), 6.0)
		
	# test right triangle: setting sides length and asserting expected corners 
	def test_set_length_right(self):
	    t = RightTriangle(6, 8)
		
	    self.assertEqual(t.a, 6)
	    self.assertEqual(t.b, 8)
	    self.assertEqual(t.c, 10)

	    expected_corners = ((0,0), (6,0), (0,8))
	    self.assertEqual(t.get_corners(), expected_corners)
	
	
	def test_is_right_triangle(self):
	    with self.assertRaises(ValueError):
		t = RightTriangle(3, 6)
		
		
		
	def test_check_right_triangle(self):
	    t = RightTriangle(3, 4)
	    self.assertAlmostEqual(t.check_right_triangle(3, 4), 5)
	    with self.assertRaises(ValueError):
	        t.check_right_triangle(2, 2)
		
	



	    
	    



if __name__ == '__main__':
    unittest.main()


