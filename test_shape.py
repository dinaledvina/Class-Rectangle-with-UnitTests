import unittest


class TestShape(unittest.TestCase):

    def test_shape_position(self):
        shape = Shape()
        shape.x = 0
        shape.y = 0

        shape.set_position(shape.x, shape.y)
       
        self.assertEqual(shape.get_position(), (shape.x, shape.y))
        
        
        

