from tictactoe_ai import *
from basic_ttt_functions import *

#main body start
print "Welcome to Tic-Tac-Toe"
board = initialize_board()

# select difficulty: Basic, Moderate, or Impossible
# basic by default
difficulty = 1
print "Choose your difficulty:\n"
print "\t1 - Basic\n"
print "\t2 - Moderate\n"
print "\t3 - Impossible\n"

#insert choose statement here later

while win_check(board) == 0:
    print "active"
    board = basic_AI(board)
    #check
    print_board(board)

    #terminate dummy plug


    print win_check(board)

print "telos"