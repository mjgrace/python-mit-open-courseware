from graphics import *
from block import Block
from shape import *

def main():
    win = GraphWin("Tetrominoes", 900, 150)
    
#     block = Block(Point(1,1), 'red')
#     
#     block.draw(win)
    
#     shape = Shape([Point(1,1), Point(1,2), Point(1,3), Point(1,4)], 'red')
#     
#     shape.draw(win)
    
    # TODO - Get the code to test all shapes
    
    tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]

    x = 3
    
    for tetromino in tetrominoes:
        shape = tetromino(Point(x, 1), 'blue')
        shape.draw(win)
        x += 4
        
    
    #shape = J_shape(Point(2,2))
    
    #shape.draw(win)
    
    win.mainloop()

main()