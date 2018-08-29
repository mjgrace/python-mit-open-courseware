from graphics import *
from block import Block

class Shape(Block):
    def __init__(self, coords, color):
        self.blocks = []
        
        for coord in coords:
            self.blocks.append(Block(coord, color))
    
    def draw(self, win):
        for block in self.blocks: 
            block.draw(win) 
        
class I_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x, center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, color)
        
class J_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x, center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, color)
        
class L_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x, center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, color)
        
class O_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x, center.y),
                  Point(center.x - 1, center.y + 1),
                  Point(center.x, center.y + 1)]
        Shape.__init__(self, coords, color)
        
class S_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x, center.y + 1),
                  Point(center.x, center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, color)
        
class T_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x, center.y),
                  Point(center.x, center.y + 1),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, color)
        
class Z_shape(Shape):
    def __init__(self, center, color):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x, center.y),
                  Point(center.x, center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, color)
        
