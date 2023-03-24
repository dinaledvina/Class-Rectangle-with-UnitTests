
import unittest
from shape import Shape

class ShapeTest(unittest.TestCase):
    
	def test_get_position(self):
   		shape = Shape()
		
   		shape.set_position(10, 20)
   		self.assertEqual(shape.get_position(), (10, 20))
   		



if __name__ == '__main__':
    unittest.main()

        
        
        

