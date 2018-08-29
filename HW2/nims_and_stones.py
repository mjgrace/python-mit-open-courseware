# Name:
# Section:
# nims.py
from mhlib import isnumeric

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):

    while pile > 0:
        player1_input = ""
        player1_valid = False
        while (not(player1_valid)):
            player1_input = raw_input("Enter Player 1 input: ")
            if (isnumeric(player1_input)):
                player1_input = int(player1_input)
                player1_valid = True
                pile = pile - player1_input
                print pile
                print player1_input
                if pile <= 0:
                    print "Player 1 wins"
                    return

        player2_input = ""
        player2_valid = False
        while (not(player2_valid)):
            player2_input = raw_input("Enter Player 2 input: ")
            if (isnumeric(player2_input)):
                player2_input = int(player2_input)
                player2_valid = True
                pile = pile - player2_input
                print pile
                print player2_input
                if pile <= 0:
                    print "Player 2 wins"
                    return

    print "Game over"
    
play_nims(25, 5)
