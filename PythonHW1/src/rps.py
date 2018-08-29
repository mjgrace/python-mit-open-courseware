player1 = raw_input("Enter player 1 selection: ")

if (player1 != "rock" and player1 != "paper" and player1 != "scissors"):
    print "Invalid selection"

player2 = raw_input("Enter player 2 selection: ")

if (player2 != "rock" and player2 != "paper" and player2 != "scissors"):
    print "Invalid selection"

if ((player1 == 'rock' and player2 == 'scissors')
    or (player1 == 'scissors' and player2 == 'paper')
    or (player1 == 'paper' and player2 == 'rock')):
    print "Player 1 wins"

if ((player2 == 'rock' and player1 == 'scissors')
    or (player2 == 'scissors' and player1 == 'paper')
    or (player2 == 'paper' and player1 == 'rock')):
    print "Player 2 wins"

if (player1 == player2):
    print "Tie"
    