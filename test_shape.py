
import unittest
from shape import Shape

class TestShape(unittest.TestCase):
    
	def test_set_position(self):
   		shape = Shape()
		x_value = 0
		x_value = 0
   		shape.set_position(x_value, y_value)
   		self.assertEqual(shape.get_position(), (x_value, y_value))



if __name__ == '__main__':
    unittest.main()

        
        
        

