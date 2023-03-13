import unittest
from shape import Shape

class TestShape(unittest.TestCase):
    def test_init(self):
        
        shape = Shape()

       
        self.assertEqual(shape.x, 10)
        self.assertEqual(shape.y, 10)

if __name__ == '__main__':
    unittest.main()

        
        
        

