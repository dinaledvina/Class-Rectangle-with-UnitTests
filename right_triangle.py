

class RightTriangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.corners = ((0,0), (self.a, 0), (0, self.b))

    def perimeter(self):
    	return (self.a + self.b + self.c)

    def area(self):
    	s = (self.a + self.b + self.c) / 2
    	return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
     def get_corners(self):
        return self.corners

    def set_length(self, a, b, c):
    	self.corners = ((0,0), (self.a, 0), (0, self.b))
