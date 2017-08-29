def initialize_board():
    w, h = 3, 3
    board = [[' ' for x in range(w)] for y in range(h)]
    return board

def check_board(board_array):
    for x in board_array:
        for y in x:
            if y == ' ':
                return True
    return False


def print_board(board_array):
    str_one = "{} | {} | {}\n".format(board_array[0][0], board_array[0][1], board_array[0][2])
    str_fill = '- + - + -\n'
    str_two = "{} | {} | {}\n".format(board_array[1][0], board_array[1][1], board_array[1][2])
    str_three = "{} | {} | {}\n".format(board_array[2][0], board_array[2][1], board_array[2][2])
    print str_one + str_fill + str_two + str_fill + str_three

def win_check(board_array):
    victory = False
    #check rows (3)
    for x in board_array:
        for y in x:

    #check columns (3)
    #check diagonals (2)
    #determines whether someone has won.
    #if someone wins, display and quit

def basic_AI(board_array):
    #randomly chooses coordinates
    # assign numbers to empty spots and randomly choose one

def moderate_AI(board_array):
    #blocks twos

def impossible_AI(board_array):
    #forces a tie at worst

#main body start

board = initialize_board()

# select difficulty: Basic, Moderate, or Impossible
difficulty = 0 #basic by default

while check_board(board):
    #itenerant

    #check
    print_board(board)
    win_check(board)

#a tie has been reached

print "telos"