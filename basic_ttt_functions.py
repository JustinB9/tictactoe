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
    #check columns
    for x in range(3):
        if board_array[x][0] == board_array[x][1] and board_array[x][1] == board_array[x][2]:
            if board_array[x][0] == ' ':
                return 0
            else:
                if board_array[x][0] == 'X':
                    return 1
                else:
                    return 2
    #
    #check rows
    for y in range(3):
        if board_array[0][y] == board_array[1][y] and board_array[1][y] == board_array[2][y]:
            if board_array[0][y] == ' ':
                return 0
            else:
                if board_array[0][y] == 'X':
                    return 1
                else:
                    return 2
    #
    #check diagonals
    if board_array[0][0] == board_array[1][1] and board_array[1][1] == board_array[2][2]:
        if board_array[0][0] == 'X':
            return 1
        else:
            return 2
    #
    #check for cat's game
    if check_board(board_array) == False:
        return 3

    return 0