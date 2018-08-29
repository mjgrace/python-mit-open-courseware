from graphics import *
from wheel import Wheel

class Car():

    def __init__(self, wheel_point1, wheel_radius1, wheel_point2, wheel_radius2, height):
        self.wheel1 = Wheel(wheel_point1, wheel_radius1*0.6, wheel_radius1)
        self.wheel2 = Wheel(wheel_point2, wheel_radius2*0.6, wheel_radius2)
        # TODO - Get the point coordinates to get the corners
        self.body = Rectangle(Point(wheel_point1.getX(), wheel_point1.getY()-height), Point(wheel_point2.getX(), wheel_point2.getY()))

    def draw(self, win): 
        self.wheel1.draw(win) 
        self.wheel2.draw(win)
        self.body.draw(win)

    def move(self, dx, dy): 
        self.wheel1.move(dx, dy) 
        self.wheel2.move(dx, dy)
        self.body.move(dx, dy)

    def set_color(self, tire_color, wheel_color, body_color):
        # TODO - Set the colors
        self.wheel1.set_color(wheel_color, tire_color) 
        self.wheel2.set_color(wheel_color, tire_color)
        self.body.setFill(body_color)

    def undraw(self): 
        self.wheel1.undraw() 
        self.wheel2.undraw()
        self.body.undraw() 

#     def get_size(self):
#         return self.tire_circle.getRadius()
# 
#     def get_center(self):
#         return self.tire_circle.getCenter()

    def animate(self, win, dx, dy, n):
        # TODO - Move the body and the wheels
        if n > 0:
            self.wheel1.move(dx, dy)
            self.wheel2.move(dx, dy)
            self.body.move(dx, dy)
            win.after(50, self.animate, win, dx, dy, n-1)


def main():
    new_win = GraphWin("A Car", 700, 300)
    
    car1 = Car(Point(50,50), 15, Point(100,50), 15, 40)
    
    car1.draw(new_win)
    
    car1.set_color('black', 'grey', 'pink')
    
    car1.animate(new_win, 1, 0, 400)
    
    new_win.mainloop()

# Comment this call to main() when you import this code into
#  your car.py file - otherwise the Wheel will pop up when you
#  try to run your car code.
main()