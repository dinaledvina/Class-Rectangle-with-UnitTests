
import unittest
from shape import Shape

class TestShape(unittest.TestCase):
    def test_init(self):
       
        shape = Shape()
        x_value = 0
        y_value = 0

    def test_set_position(self):
   
        shape.set_position(x_value, y_value)
        self.assertEqual(shape.set_position(), (x_value, y_value))

    def test_get_position(self):
      
        self.assertEqual(shape.get_position(), (x_value, y_value))

if __name__ == '__main__':
    unittest.main()

        
        
        

