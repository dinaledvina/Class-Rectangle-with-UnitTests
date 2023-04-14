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
		
		
		
	def test_right_triangle_constructor(self):
	    a, b = 2, 2
	    c = (a**2 + b**2)**0.5
	    if a ** 2 + b ** 2 != c ** 2:
		with self.assertRaises(ValueError):
		    t = RightTriangle(a, b)
		

		
	



	    
	    



if __name__ == '__main__':
    unittest.main()


