
import unittest
from shape import Shape

class TestShape(unittest.TestCase):
    
	def test_set_position(self):
   		shape = Shape()
   		shape.set_position(x_value = 1, y_value = 1)
   		self.assertEqual(shape.get_position(), (x_value, y_value))



if __name__ == '__main__':
    unittest.main()

        
        
        

