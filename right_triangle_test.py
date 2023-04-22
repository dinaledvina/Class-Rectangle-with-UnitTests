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
	
	

	
	
	def test_right_triangle(self):
	    #t = RightTriangle(1/3, 1/4)
	    t = RightTriangle(2, 2)
	    self.assertAlmostEqual(t.a ** 2 + t.b ** 2, t.c ** 2, delta = 1e-9)
		

		
	



	    
	    



if __name__ == '__main__':
    unittest.main()


