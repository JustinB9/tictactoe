WIDTH = 3
HEIGHT = 3

def initialize_board():
    board = [[' ' for x in range(WIDTH)] for y in range(HEIGHT)]
    return board


def check_for_spaces(board_array):
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
    # check columns
    for x in range(WIDTH):
        if board_array[x][0] == board_array[x][1] and board_array[x][1] == board_array[x][2]:
            if board_array[x][0] == 'X':
                return 1
            elif board_array[x][0] == 'O':
                return 2
    #
    # check rows
    for y in range(HEIGHT):
        if board_array[0][y] == board_array[1][y] and board_array[1][y] == board_array[2][y]:
            if board_array[0][y] == 'X':
                return 1
            elif board_array[0][y] == 'O':
                return 2
    #
    # check diagonals
    if board_array[0][0] == board_array[1][1] and board_array[1][1] == board_array[2][2]:
        if board_array[1][1] == 'X':
            return 1
        elif board_array[1][1] == 'O':
            return 2

    if board_array[2][0] == board_array[1][1] and board_array[1][1] == board_array[0][2]:
        if board_array[1][1] == 'X':
            return 1
        elif board_array[1][1] == 'O':
            return 2

    #
    # check for cat's game
    if not check_for_spaces(board_array):
        return 3

    return 0
