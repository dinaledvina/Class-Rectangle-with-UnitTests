import unittest


class TestShape(unittest.TestCase):

    def test_shape_position(self):
        shape = Shape()
        
        
        
        shape.set_position(shape.x, shape.y)
        
        self.assertEqual(shape.get_position(), (shape.x, shape.y))

        
        
        

