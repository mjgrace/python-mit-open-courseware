from graphics import *

class Block(Rectangle):
    def __init__(self, point, color):
        Rectangle.__init__(self, Point(point.getX()*30, point.getY()*30), Point(point.getX()*30+30, point.getY()*30 + 30))
        self.set_outline('black')
        self.set_color(color)
    
    def set_outline(self, color):
        self.setOutline(color)
 
    def set_color(self, color):
        self.setFill(color) 
